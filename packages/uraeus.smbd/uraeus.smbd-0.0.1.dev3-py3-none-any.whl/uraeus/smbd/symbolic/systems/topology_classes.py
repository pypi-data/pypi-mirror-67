# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:31:35 2019

@author: khale
"""

# Standard library imports
import itertools

# 3rd party libraries imports
import sympy as sm
import matplotlib.pyplot as plt
import networkx as nx

# Local application imports
from ..components.matrices import (global_frame, reference_frame,
                                         zero_matrix)
from ..components import bodies
from ..components.joints import absolute_locator
from ..components.algebraic_constraints import joint_actuator
from ..components.forces import abstract_force, gravity_force, centrifugal_force

###############################################################################

class abstract_topology(object):
    
    def __init__(self, name):
        self.name = name
        self.graph = nx.MultiDiGraph(name=name)
        self._edges_map = {}
        self._edges_keys_map = {}
        self.variants = {'base':self.graph}
        self._selected_variant = self.graph
        self._insert_ground()
        self._set_global_frame()
    
    def create_subvariant(self, name, parent=None):
        if parent is None:
            parent = 'base'
        parent_graph = self.variants[parent]
        graph = nx.MultiDiGraph(name = name)
        graph.add_nodes_from(parent_graph.nodes(data=True))
        graph.add_edges_from(parent_graph.edges(data=True, keys=True))
        self.variants[name] = graph
        self.selected_variant = name
        
    
    @property
    def selected_variant(self):
        return self._selected_variant
    @selected_variant.setter
    def selected_variant(self, name):
        self._selected_variant = self.variants[name]
    
    @property
    def nodes(self):
        return self.selected_variant.nodes
    @property
    def edges(self):
        return self.selected_variant.edges
    
    @property
    def constraints_graph(self):
        graph = self.selected_variant
        edges = self.edges
        condition = lambda e : issubclass(edges[e]['class'], abstract_force)
        filtered = itertools.filterfalse(condition, edges)
        return graph.edge_subgraph(filtered)

    @property
    def forces_graph(self):
        graph = self.selected_variant
        edges = self.edges
        condition = lambda e : issubclass(edges[e]['class'], abstract_force)
        filtered = filter(condition, edges)
        return graph.edge_subgraph(filtered)

    @property
    def bodies(self):
        bodies = itertools.filterfalse(self._is_virtual_node, self.nodes)
        return list(bodies)
    
    @property
    def virtual_bodies(self):
        condition = self._is_virtual_node
        virtuals  = filter(condition, self.nodes)
        return set(virtuals)
    
    @property
    def virtual_edges(self):
        condition = self._is_virtual_edge
        virtuals  = filter(condition, self.edges)
        return set(virtuals)
    
    @property
    def nodes_indicies(self):
        node_index = dict([(n, i) for i,n in enumerate(self.nodes)])
        return node_index
    @property
    def edges_indicies(self):
        edges_index = dict([(n, i) for i,n in enumerate(self.edges)])
        return edges_index

    @property
    def n(self):
        return self._get_topology_attr('n')
    @property
    def nc(self):
        return self._get_topology_attr('nc')
    @property
    def nve(self):
        return self._get_topology_attr('nve')
    
    @property
    def arguments_symbols(self):
        return self._get_topology_attr('arguments_symbols')
    @property
    def runtime_symbols(self):
        return self._get_topology_attr('runtime_symbols')
    @property
    def constants_symbols(self):
        return self._get_topology_attr('constants_symbols')
    @property
    def constants_symbolic_expr(self):
        return self._get_topology_attr('constants_symbolic_expr')
    @property
    def constants_numeric_expr(self):
        return self._get_topology_attr('constants_numeric_expr')
    
    @property
    def mapped_gen_coordinates(self):
        return self._coordinates_mapper('q')
    @property
    def mapped_gen_velocities(self):
        return self._coordinates_mapper('qd')
    @property
    def mapped_gen_accelerations(self):
        return self._coordinates_mapper('qdd')
    @property
    def mapped_lagrange_multipliers(self):
        return self._lagrange_multipliers_mapper()
    @property
    def virtual_coordinates(self):
        q_virtuals = []
        nodes = self.nodes
        for n in self.virtual_bodies:
            obj = nodes[n]['obj']
            q_virtuals += [obj.R, obj.P, obj.Rd, obj.Pd]
        return q_virtuals

    @property
    def reactions_equalities(self):
        graph = self.selected_variant
        eq = [self.edges[e]['obj'].reactions_equalities for e in self.graph.edges]
        return sum(eq,[])
    
    @property
    def reactions_symbols(self):
        graph = self.selected_variant
        eq = [self.edges[e]['obj'].reactions_symbols for e in self.graph.edges]
        return sum(eq,[])
    
    def draw_constraints_topology(self):
        plt.figure(figsize=(10, 6))
        graph = nx.Graph(self.constraints_graph)
        nx.draw(graph,with_labels=True)
        plt.show()
        
    def draw_forces_topology(self):
        plt.figure(figsize=(10, 6))
        nx.draw_spring(self.forces_graph, with_labels=True)
        plt.show()
    
    def assemble_model(self):
        self._set_global_frame()
        self._assemble_nodes()
        self._assemble_edges()
        self._remove_virtual_edges()
        self._assemble_constraints_equations()
        self._assemble_forces_equations()
        self._assemble_mass_matrix()
        self._perform_cse()
                
    def save(self):
        import cloudpickle
        file = '%s.stpl'%self.name
        with open(file,'wb') as f:
            cloudpickle.dump(self, f)


    def _perform_cse(self):
        self.pos_rep, self.pos_exp = self._generate_cse(self.pos_equations, 'x')
        self.vel_rep, self.vel_exp = self._generate_cse(self.vel_equations, 'v')
        self.acc_rep, self.acc_exp = self._generate_cse(self.acc_equations, 'a')
        self.jac_rep, self.jac_exp = self._generate_cse(self.jac_equations, 'j')
        self.frc_rep, self.frc_exp = self._generate_cse(self.frc_equations, 'f')
        self.mass_rep, self.mass_exp = self._generate_cse(self.mass_equations, 'm')

    def _get_topology_attr(self, name):
        graph = self.selected_variant
        nodes_attr = nx.get_node_attributes(graph, name).values()
        edges_attr = nx.get_edge_attributes(graph, name).values()
        container  = itertools.chain(nodes_attr, edges_attr)
        try:
            return sum(container)
        except TypeError:
            container  = itertools.chain(nodes_attr, edges_attr)
            return sum(container, [])

    def _set_global_frame(self):
        self.global_instance = global_frame(self.name)
        reference_frame.set_global_frame(self.global_instance)        
        
    def _insert_ground(self):
        typ_dict = self._typ_attr_dict(bodies.ground)
        self.grf = 'ground'
        self.graph.add_node(self.grf, **typ_dict)
    
    def _is_force_edge(self, e):
        return issubclass(self.edges[e]['class'], abstract_force)

    def _is_virtual_node(self, n):
        virtual_flag = self.nodes[n].get('virtual', False)
        return virtual_flag

    def _is_virtual_edge(self, e):
        virtual_flag = self.edges[e].get('virtual', False)
        return virtual_flag


    def _coordinates_mapper(self, sym):
        q_sym  = sm.MatrixSymbol(sym, self.n, 1)
        q = []
        i = 0
        bodies = self.bodies
        nodes  = self.nodes
        for b in bodies:
            q_block = getattr(nodes[b]['obj'], sym)
            for qi in q_block.blocks:
                s = qi.shape[0]
                q.append(sm.Eq(qi,q_sym[i:i+s, 0]))
                i+=s
        return q
    
    def _lagrange_multipliers_mapper(self):
        l = []
        lamda = sm.MatrixSymbol('Lambda', self.nc, 1)
        i = 0
        edges = self.constraints_graph.edges
        for e in itertools.filterfalse(self._is_virtual_edge, edges):
            obj = edges[e]['obj']
            nc = obj.nc
            eq = sm.Eq(obj.L, lamda[i:i+nc])
            l.append(eq)
            i += nc
        return l
    
    def _assemble_nodes(self):
        for n in self.nodes : self._assemble_node(n) 
    
    def _assemble_edges(self):
        for e in self.edges : self._assemble_edge(e)
    
    def _assemble_node(self,n):
        nodes = self.nodes
        node_class = nodes[n]['class']
        body_instance = node_class(n)
        nodes[n].update(self._obj_attr_dict(body_instance))
        if nodes[n]['virtual']:
            nodes[n]['arguments_symbols'] = []
            nodes[n]['constants_symbols'] = []
            nodes[n]['constants_symbolic_expr'] = []
            
        
    def _assemble_edge(self, e):
        nodes = self.nodes
        edges = self.edges
        edge_class = edges[e]['class']
        name = edges[e]['name']
        b1, b2, key = e
        b1_obj = nodes[b1]['obj'] 
        b2_obj = nodes[b2]['obj'] 
        
        if issubclass(edge_class, joint_actuator):
            joint_key     = self._edges_keys_map[edges[e]['joint_name']]
            joint_object  = edges[(b1, b2, joint_key)]['obj']
            edge_instance = edge_class(name, joint_object)
        
        elif issubclass(edge_class, absolute_locator):
            coordinate    = edges[e]['coordinate']
            edge_instance = edge_class(name, b1_obj, b2_obj, coordinate)
        
        else:
            edge_instance = edge_class(name, b1_obj, b2_obj)
        
        edges[e].update(self._obj_attr_dict(edge_instance))
    

    def _remove_virtual_edges(self):
        graph = self.selected_variant
        graph.remove_edges_from(self.virtual_edges)
    
    def _store_constaints_index(self):
        self._actuators_indicies = {}
        edges   = self.constraints_graph.edges
        row_ind = 0
        for e in edges:
            if self._is_virtual_edge(e):
                continue
            constraint_name = edges[e]['name']
            constraint_nve  = edges[e]['nve']
            rows = slice(row_ind, row_ind + constraint_nve, 1)
            self._actuators_indicies[constraint_name] = rows
            row_ind += constraint_nve
    
    def _assemble_constraints_equations(self):
        
        edges = self.constraints_graph.edges
        nodes = self.nodes
        node_index = self.nodes_indicies

        cols = 2*len(nodes)
        nve  = self.nve
        
        equations = sm.MutableSparseMatrix(nve, 1, None)
        vel_rhs   = sm.MutableSparseMatrix(nve, 1, None)
        acc_rhs   = sm.MutableSparseMatrix(nve, 1, None)
        jacobian  = sm.MutableSparseMatrix(nve, cols, None)
                
        row_ind = 0
        for e in edges:
            if self._is_virtual_edge(e):
                continue
            eo  = edges[e]['obj']
            u,v = e[:-1]
            
            # tracker of row index based on the current joint type and the history
            # of the loop
            eo_nve = eo.nve + row_ind
            
            ui = node_index[u]
            vi = node_index[v]

            # assigning the joint jacobians to the propper index in the system jacobian
            # on the "constraint vector equations" level.
            jacobian[row_ind:eo_nve,ui*2:ui*2+2] = eo.jacobian_i.blocks
            jacobian[row_ind:eo_nve,vi*2:vi*2+2] = eo.jacobian_j.blocks
            
            equations[row_ind:eo_nve,0] = eo.pos_level_equations.blocks
            vel_rhs[row_ind:eo_nve,0] = eo.vel_level_equations.blocks
            acc_rhs[row_ind:eo_nve,0] = eo.acc_level_equations.blocks
           
            row_ind += eo.nve
        
        for i,n in enumerate(nodes):
            if self._is_virtual_node(n):
                continue
            b = nodes[n]['obj']
            if isinstance(b, bodies.ground):
                jacobian[row_ind:row_ind+2,i*2:i*2+2] = b.normalized_jacobian.blocks
                equations[row_ind:row_ind+2,0] = b.normalized_pos_equation.blocks
                vel_rhs[row_ind:row_ind+2,0]   = b.normalized_vel_equation.blocks
                acc_rhs[row_ind:row_ind+2,0]   = b.normalized_acc_equation.blocks
            else:
                jacobian[row_ind,i*2]   = b.normalized_jacobian[0]
                jacobian[row_ind,i*2+1] = b.normalized_jacobian[1]

                equations[row_ind,0] = b.normalized_pos_equation
                vel_rhs[row_ind,0]   = b.normalized_vel_equation
                acc_rhs[row_ind,0]   = b.normalized_acc_equation
            row_ind += b.nve
                
        self.pos_equations = equations
        self.vel_equations = vel_rhs
        self.acc_equations = acc_rhs
        self.jac_equations = jacobian
                
    def _assemble_mass_matrix(self):
        nodes  = self.nodes
        bodies = self.bodies
        n = 2*len(bodies)
        matrix = sm.MutableSparseMatrix(n, n, None)
        mass_matricies = [[nodes[i]['obj'].M, nodes[i]['obj'].J] for i in bodies]
        mass_matricies = sum(mass_matricies, [])
        for i,m in enumerate(mass_matricies):
            matrix[i,i] = m
        self.mass_equations = matrix
    
    def _assemble_forces_equations(self):
        graph = self.forces_graph
        nodes = self.bodies
        nrows = 2*len(nodes)
        F_applied = sm.MutableSparseMatrix(nrows, 1, None)
        for i,n in enumerate(nodes):
            if self._is_virtual_node(n):
                continue
            in_edges  = graph.in_edges([n], data='obj')
            if len(in_edges) == 0 :
                Q_in_R = zero_matrix(3, 1)
                Q_in_P = zero_matrix(4, 1)
            else:
                Q_in_R = sm.MatAdd(*[e[-1].Qj.blocks[0] for e in in_edges])
                Q_in_P = sm.MatAdd(*[e[-1].Qj.blocks[1] for e in in_edges])
            
            out_edges = graph.out_edges([n], data='obj')
            if len(out_edges) == 0 :
                Q_out_R = zero_matrix(3, 1)
                Q_out_P = zero_matrix(4, 1)
            else:
                Q_out_R = sm.MatAdd(*[e[-1].Qi.blocks[0] for e in out_edges])
                Q_out_P = sm.MatAdd(*[e[-1].Qi.blocks[1] for e in out_edges])
            
            Q_t_R = Q_in_R + Q_out_R
            Q_t_P = Q_in_P + Q_out_P
            
            F_applied[i*2]   = Q_t_R
            F_applied[i*2+1] = Q_t_P
            
        self.frc_equations = F_applied
    
        
    @staticmethod
    def _typ_attr_dict(typ):
        attr_dict = {'n':typ.n, 'nc':typ.nc, 'nve':typ.nve, 'class':typ,
                     'mirr':None, 'align':'s', 'virtual':False}
        return attr_dict
    
    @staticmethod
    def _obj_attr_dict(obj):
        attr_dict = {'obj':obj,
                     'arguments_symbols':obj.arguments_symbols,
                     'runtime_symbols':obj.runtime_symbols,
                     'constants_symbolic_expr':obj.constants_symbolic_expr,
                     'constants_numeric_expr':obj.constants_numeric_expr,
                     'constants_symbols':obj.constants_symbols}
        return attr_dict
    
    @staticmethod
    def _generate_cse(equations, symbol):
        t = sm.symbols('t', real=True)
        cse_symbols = sm.iterables.numbered_symbols(symbol)
        reduced_equations = sm.cse(equations, symbols=cse_symbols, ignore=(t,))
        return reduced_equations

            
###############################################################################
###############################################################################

class topology(abstract_topology):
        
    def add_body(self, name):
        variant = self.selected_variant
        if name not in variant.nodes():
            attr_dict = self._typ_attr_dict(bodies.body)
            variant.add_node(name, **attr_dict)
            self._add_node_forces(name)
        
    def add_joint(self,typ, name, body_i, body_j):
        assert body_i in self.nodes, 'Body %r does not exist.'%body_i
        assert body_j in self.nodes, 'Body %r does not exist.'%body_j
        variant = self.selected_variant
        edge  = (body_i, body_j)
        if name not in self._edges_keys_map:
            attr_dict = self._typ_attr_dict(typ)
            attr_dict.update({'name':name})
            key = variant.add_edge(*edge, **attr_dict)
            self._edges_map[name] = (*edge, key)
            self._edges_keys_map[name] = key
    
    def add_joint_actuator(self, typ, name, joint_name):
        assert joint_name in self._edges_map, 'Joint %r does not exist!'%joint_name
        variant = self.selected_variant
        joint_edge = self._edges_map[joint_name]
        act_edge   = joint_edge[:2]
        if name not in self._edges_map:
            attr_dict = self._typ_attr_dict(typ)
            attr_dict.update({ 'name':name, 'joint_name':joint_name})
            key = variant.add_edge(*act_edge, **attr_dict)
            self._edges_map[name] = (*act_edge, key)
            self._edges_keys_map[name] = key
    
    def add_absolute_actuator(self, typ, name, body, body_j, coordinate):
        assert body in self.nodes, 'Body %r does not exist.'%body
        variant = self.selected_variant
        edge  = (body, body_j)
        if name not in self._edges_map:
            attr_dict = self._typ_attr_dict(typ)
            attr_dict.update({'name':name, 'coordinate':coordinate})
            key = variant.add_edge(*edge, **attr_dict)
            self._edges_map[name] = (*edge, key)
            self._edges_keys_map[name] = key
    
    def add_force(self, typ, name, body_i, body_j):
        assert body_i in self.nodes, 'Body %r does not exist.'%body_i
        assert body_j in self.nodes, 'Body %r does not exist.'%body_j
        variant = self.selected_variant
        edge  = (body_i, body_j)
        if name not in self._edges_map:
            attr_dict = self._typ_attr_dict(typ)
            attr_dict.update({'name':name})
            key = variant.add_edge(*edge, **attr_dict)
            self._edges_map[name] = (*edge, key)
            self._edges_keys_map[name] = key
    
    
    def _add_node_forces(self, n):
        grf = self.grf
        self.add_force(gravity_force, '%s_gravity'%n, n, grf)
        self.add_force(centrifugal_force, '%s_centrifuge'%n, n, grf)

###############################################################################
###############################################################################

class template_based_topology(topology):
    
    def add_body(self, name, mirror=False, virtual=False):
        variant = self.selected_variant
        if mirror:
            node1 = ('vbr_%s'%name if virtual else 'rbr_%s'%name)
            node2 = ('vbl_%s'%name if virtual else 'rbl_%s'%name)
            super().add_body(node1)
            super().add_body(node2)
            variant.nodes[node1].update({'mirr':node2, 'align':'r'})
            variant.nodes[node2].update({'mirr':node1, 'align':'l'})
            if virtual:
                self._set_body_as_virtual(node1)
                self._set_body_as_virtual(node2)
        else:
            node1 = node2 = ('vbs_%s'%name if virtual else 'rbs_%s'%name)
            super().add_body(node1)
            variant.nodes[node1]['mirr'] = node2
            if virtual:
                self._set_body_as_virtual(node1)
    
    
    def add_joint(self, typ, name, body_i, body_j, mirror=False, virtual=False):
        variant = self.selected_variant
        if mirror:
            body_i_mirr = variant.nodes[body_i]['mirr']
            body_j_mirr = variant.nodes[body_j]['mirr']
            name1 = 'jcr_%s'%name
            name2 = 'jcl_%s'%name
            super().add_joint(typ,name1,body_i,body_j)
            super().add_joint(typ,name2,body_i_mirr,body_j_mirr)
            joint_edge1 = self._edges_map[name1]
            joint_edge2 = self._edges_map[name2]
            variant.edges[joint_edge1].update({'mirr':name2, 'align':'r'})
            variant.edges[joint_edge2].update({'mirr':name1, 'align':'l'})
            if virtual:
                self._set_joint_as_virtual(joint_edge1)
                self._set_joint_as_virtual(joint_edge2)
        else:
            name = 'jcs_%s'%name
            super().add_joint(typ,name,body_i,body_j)
            joint_edge = self._edges_map[name]
            variant.edges[joint_edge].update({'mirr':name})
            if virtual:
                self._set_joint_as_virtual(joint_edge)
    
    def add_joint_actuator(self, typ, name, joint_name, mirror=False):
        variant = self.selected_variant
        if mirror:
            joint_edge1 = self._edges_map[joint_name]
            joint_name2 = variant.edges[joint_edge1]['mirr']
            name1 = 'mcr_%s'%name
            name2 = 'mcl_%s'%name
            super().add_joint_actuator(typ,name1,joint_name)
            super().add_joint_actuator(typ,name2,joint_name2)
            act_edge1 = self._edges_map[name1]
            act_edge2 = self._edges_map[name2]
            variant.edges[act_edge1].update({'mirr':name2, 'align':'r'})
            variant.edges[act_edge2].update({'mirr':name1, 'align':'l'})
        else:
            name = 'mcs_%s'%name
            super().add_joint_actuator(typ,name,joint_name)
            act_edge = self._edges_map[name]
            variant.edges[act_edge].update({'mirr':name})
    
    def add_absolute_actuator(self, typ, name, body_i, body_j, coordinate, mirror=False):
        variant = self.selected_variant
        if mirror:
            body_i_mirr = variant.nodes[body_i]['mirr']
            body_j_mirr = variant.nodes[body_j]['mirr']
            name1 = 'mcr_%s'%name
            name2 = 'mcl_%s'%name
            super().add_absolute_actuator(typ, name1, body_i, body_j, coordinate)
            super().add_absolute_actuator(typ, name2, body_i_mirr, body_j_mirr, coordinate)
            act_edge1 = self._edges_map[name1]
            act_edge2 = self._edges_map[name2]
            variant.edges[act_edge1].update({'mirr':name2, 'align':'r'})
            variant.edges[act_edge2].update({'mirr':name1, 'align':'l'})
        else:
            name = 'mcs_%s'%name
            super().add_absolute_actuator(typ, name, body_i, body_j, coordinate)
            act_edge = self._edges_map[name]
            variant.edges[act_edge].update({'mirr':name})
    
    def add_force(self, typ, name, body_i, body_j=None, mirror=False):
        body_j = self.grf if body_j is None else body_j
        variant = self.selected_variant
        if mirror:
            body_i_mirr = self.nodes[body_i]['mirr']
            body_j_mirr = self.nodes[body_j]['mirr']
            name1 = 'far_%s'%name
            name2 = 'fal_%s'%name
            super().add_force(typ, name1, body_i, body_j)
            super().add_force(typ, name2, body_i_mirr, body_j_mirr)
            force_edge1 = self._edges_map[name1]
            force_edge2 = self._edges_map[name2]
            variant.edges[force_edge1].update({'mirr':name2, 'align':'r'})
            variant.edges[force_edge2].update({'mirr':name1, 'align':'l'})
        else:
            name = 'fas_%s'%name
            super().add_force(typ, name, body_i, body_j)
            force_edge = self._edges_map[name]
            variant.edges[force_edge].update({'mirr':name})
    
    
    def _insert_ground(self):
        typ_dict = self._typ_attr_dict(bodies.body)
        self.grf = 'vbs_ground'
        self.graph.add_node(self.grf, **typ_dict)
        self.nodes[self.grf]['mirr'] = self.grf
        self._set_body_as_virtual(self.grf)
        
    def _set_joint_as_virtual(self,edge):
        variant = self.selected_variant
        d = {'nc':0,'nve':0,'virtual':True}
        variant.edges[edge].update(d)
    
    def _set_body_as_virtual(self,node):
        variant = self.selected_variant
        d = {'n':0, 'nc':0, 'nve':0, 'virtual':True}
        variant.nodes[node].update(d)
        try:
            variant.remove_edge(*self._edges_map['fas_%s_gravity'%node])
            variant.remove_edge(*self._edges_map['fas_%s_centrifuge'%node])
            del self._edges_map['fas_%s_gravity'%node]
            del self._edges_map['fas_%s_centrifuge'%node]
            del self._edges_keys_map['fas_%s_gravity'%node]
            del self._edges_keys_map['fas_%s_centrifuge'%node]
        except KeyError:
            pass

###############################################################################
###############################################################################

class standalone_topology(template_based_topology):
    
    def add_body(self, name, mirror=False):
        super().add_body(name, mirror)
    
    def add_joint(self, typ, name, body_i, body_j, mirror=False):
        super().add_joint(typ, name, body_i, body_j, mirror)
        
    def add_force(self, typ, name, body_i, body_j=None, mirror=False):
        body_j = self.grf if body_j is None else body_j
        super().add_force(typ, name, body_i, body_j, mirror)
    
    def _insert_ground(self):
        typ_dict = self._typ_attr_dict(bodies.ground)
        self.grf = 'ground'
        self.graph.add_node(self.grf, **typ_dict)
        self.nodes[self.grf]['mirr'] = self.grf

###############################################################################
###############################################################################

class subsystem(abstract_topology):
    
    def __init__(self, name, template):
        if not isinstance(template, template_based_topology):
            raise ValueError('Entry should be instance of template class.')
        self.name = name
        self._set_global_frame()
        self.template = template
        self.graph = self.template.graph.copy()
        self.variants = {'base':self.graph}
        self._selected_variant = self.graph
        self._virtual_bodies = []
        if name != '':
            self._relable()
    
    def _relable(self):
        graph = self._selected_variant
        def label(x): return '%s.%s'%(self.name, x)
        labels_map = {i:label(i) for i in self.template.nodes}
        graph = nx.relabel_nodes(graph, labels_map)
        
        mirr_maped = {k:label(v) for k, v in graph.nodes(data='mirr')}
        nx.set_node_attributes(graph, mirr_maped, 'mirr')
        self.graph = self._selected_variant = graph
    
###############################################################################
###############################################################################

class assembly(abstract_topology):
    
    def __init__(self, name):
        self.name  = name
        self.graph = nx.MultiDiGraph(name=name)
        self.interface_graph = nx.MultiDiGraph(name=name)
        self.subsystems = {}
        self.assemblies = {}
        self._interface_map = {}
        self.variants = {'base':self.graph}
        self._selected_variant = self.graph
        self._set_global_frame()
        self._insert_ground()

    @property
    def interface_map(self):
        return self._interface_map
    
    def add_assembly(self, assm):
        if not isinstance(assm, assembly):
            raise ValueError('Entry should be instance of assembly class.')
        assm_graph = assm.graph
        self.assemblies[assm.name] = assm
        self.graph.add_nodes_from(assm_graph.nodes(data=True))
        self.graph.add_edges_from(assm_graph.edges(data=True, keys=True))
        self.global_instance.merge_global(assm.global_instance)
    
    def add_subsystem(self, sub):
        if not isinstance(sub, subsystem):
            raise ValueError('Entry should be instance of subsystem class.')
        self.subsystems[sub.name] = sub
        subsystem_graph = sub.selected_variant
        self.graph.add_nodes_from(subsystem_graph.nodes(data=True))
        self.graph.add_edges_from(subsystem_graph.edges(data=True, keys=True))
        self._update_interface_map(sub)
        self.global_instance.merge_global(sub.global_instance)
    
    def assign_virtual_body(self, virtual_node, actual_node):
        virtual_node_1 = virtual_node
        virtual_node_2 = self.nodes[virtual_node]['mirr']
        actual_node_1 = actual_node
        actual_node_2 = self.nodes[actual_node]['mirr']
        self.interface_map[virtual_node_1] = actual_node_1
        self.interface_map[virtual_node_2] = actual_node_2
    
    def assemble_model(self):
        self._initialize_interface()
        self._assemble_constraints_equations()
        self._assemble_forces_equations()
        self._assemble_mass_matrix()
        
    def draw_interface_graph(self):
        plt.figure(figsize=(10,6))
        nx.draw_spring(self.interface_graph, with_labels=True)
        plt.show()


    def _insert_ground(self):
        typ_dict = self._typ_attr_dict(bodies.ground)
        self.grf = 'ground'
        self.graph.add_node(self.grf, **typ_dict)
        self._assemble_node(self.grf)
        
    def _update_interface_map(self, subsystem):
        new_virtuals = subsystem.virtual_bodies
        new_virtuals = {i: self.grf for i in new_virtuals}
        self._interface_map.update(new_virtuals)
        
    def _initialize_interface(self):
        self._set_virtual_equalities()
        for virtual, actual in self.interface_map.items():
            self._replace_nodes(virtual, actual)
        self.interface_graph.remove_nodes_from(self.interface_map.keys())
    
    def _set_virtual_equalities(self):
        self.mapped_vir_coordinates = []
        for v,a in self.interface_map.items():
            self._assemble_node(v)
            if a!= self.grf : self._assemble_node(a)
            R_v,P_v = self.nodes[v]['obj'].q.blocks
            R_a,P_a = self.nodes[a]['obj'].q.blocks
            R_eq = sm.Eq(R_v, R_a, evaluate=False)
            P_eq = sm.Eq(P_v, P_a, evaluate=False)
            self.mapped_vir_coordinates += [R_eq, P_eq]
        
        self.mapped_vir_velocities = []
        for v,a in self.interface_map.items():
            self._assemble_node(v)
            if a!= self.grf : self._assemble_node(a)
            R_v,P_v = self.nodes[v]['obj'].qd.blocks
            R_a,P_a = self.nodes[a]['obj'].qd.blocks
            R_eq = sm.Eq(R_v, R_a, evaluate=False)
            P_eq = sm.Eq(P_v, P_a, evaluate=False)
            self.mapped_vir_velocities += [R_eq, P_eq]
        
        self.mapped_vir_accelerations = []
        for v,a in self.interface_map.items():
            self._assemble_node(v)
            if a!= self.grf : self._assemble_node(a)
            R_v,P_v = self.nodes[v]['obj'].qdd.blocks
            R_a,P_a = self.nodes[a]['obj'].qdd.blocks
            R_eq = sm.Eq(R_v, R_a, evaluate=False)
            P_eq = sm.Eq(P_v, P_a, evaluate=False)
            self.mapped_vir_accelerations += [R_eq, P_eq]

            
    def _replace_nodes(self, virtual,actual):
        a = actual
        v = virtual
        H = self.graph
        new_edges1 = [(w, a, d) for w, x, d in H.in_edges(v, data=True)]
        new_edges2 = [(a, w, d) for x, w, d in H.out_edges(v, data=True)]
        H.remove_node(v)
        new_edges = new_edges1 + new_edges2
        H.add_edges_from(new_edges)
        self.interface_graph.add_edges_from(new_edges)
            
    
    def _assemble_edges(self):
        for e in self.interface_graph.edges:
            self._assemble_edge(e)
    
    def _assemble_constraints_equations(self):
        
        nodelist = self.nodes
        cols = 2*len(nodelist)
        nve  = 2
        
        equations = sm.MutableSparseMatrix(nve, 1, None)
        vel_rhs   = sm.MutableSparseMatrix(nve, 1, None)
        acc_rhs   = sm.MutableSparseMatrix(nve, 1, None)
        jacobian  = sm.MutableSparseMatrix(nve, cols, None)
        
        row_ind = 0
        b = self.nodes['ground']['obj']
        i = self.nodes_indicies['ground']
        jacobian[row_ind:row_ind+2,i*2:i*2+2] = b.normalized_jacobian.blocks
        equations[row_ind:row_ind+2,0] = b.normalized_pos_equation.blocks
        vel_rhs[row_ind:row_ind+2,0]   = b.normalized_vel_equation.blocks
        acc_rhs[row_ind:row_ind+2,0]   = b.normalized_acc_equation.blocks
            
        self.pos_equations = equations
        self.vel_equations = vel_rhs
        self.acc_equations = acc_rhs
        self.jac_equations = jacobian
    
    def _assemble_mass_matrix(self):
        ground_obj  = self.nodes['ground']['obj']
        matrix = sm.MutableSparseMatrix(2, 2, None)
        matrix[0,0] = ground_obj.M
        matrix[1,1] = ground_obj.J
        self.mass_equations = matrix

    
    def _assemble_forces_equations(self):
        node = 'ground'
        nrows = 2
        F_applied = sm.MutableSparseMatrix(nrows,1,None)
        in_edges  = self.forces_graph.in_edges([node], data='obj')
        if len(in_edges) == 0 :
            Q_in_R = zero_matrix(3,1)
            Q_in_P = zero_matrix(4,1)
        else:
            Q_in_R = sm.MatAdd(*[e[-1].Qj.blocks[0] for e in in_edges])
            Q_in_P = sm.MatAdd(*[e[-1].Qj.blocks[1] for e in in_edges])
        
        out_edges = self.forces_graph.out_edges([node], data='obj')
        if len(out_edges) == 0 :
            Q_out_R = zero_matrix(3,1)
            Q_out_P = zero_matrix(4,1)
        else:
            Q_out_R = sm.MatAdd(*[e[-1].Qi.blocks[0] for e in out_edges])
            Q_out_P = sm.MatAdd(*[e[-1].Qi.blocks[1] for e in out_edges])
        
        Q_t_R = Q_in_R + Q_out_R
        Q_t_P = Q_in_P + Q_out_P
        
        F_applied[0] = Q_t_R
        F_applied[1] = Q_t_P
        
        self.frc_equations = F_applied
    
###############################################################################
###############################################################################

