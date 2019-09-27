import numpy as np
import random
import pdb
import itertools
import copy


def preferential_attachment(m=8, u=0.1, N=10000):
    """
    Preferential attachment with long-range connections model.
    Inputs:
    m: number of initial active nodes
    u: the probability in our model
    N: the number of nodes
    Output: undirected output graph in the edge list format.
    That is, return a list of tuples of the form (u, v), which
    indicates that there is an edge between nodes u and v.
    Both u and v should be integers between 1 and N.
    For example, if the generated graph is a triangle,
    then the output should be [(1,2), (2,3), (3,1)].
    The tuples do not have to be sorted in any order.
    """

    #init acti nodes
    node_new=m
    nodes_act=list(range(m))
    graph =[]
    for pair in itertools.combinations(nodes_act, 2):
        graph.append(pair)
    deg_dict={}
    for node in nodes_act:
        deg_dict[node]=7


    # nodes_all=set(list(range(N)))
    while node_new < N:
        node_new=node_new+1




        #PREF ATTACH FROM ALL NODES
        nodes_candid=list(deg_dict.keys())
        p_=[]
        inv_pref=np.array([1/deg_dict[node] for node in nodes_candid])
        inv_pref=inv_pref/np.sum(inv_pref)
        for pref_coeff,node in zip(inv_pref,nodes_candid):
            tmp=u*pref_coeff
            if(node in nodes_act):
                tmp=tmp+(1-u)/m
            p_.append(tmp)
        p_nodes = np.array(p_)
        nodes_to_connect=np.random.choice(nodes_candid, m, p=p_nodes)
        deg_dict[node_new] = 0
        for node in nodes_to_connect:
            graph.append((node_new,node))
            deg_dict[node]=deg_dict[node]+1
            deg_dict[node_new]=deg_dict[node_new]+1

        nodes_candid=nodes_act
        p_inactive=np.array([1/deg_dict[node] for node in nodes_act])
        p_inactive=p_inactive/np.sum(p_inactive)
        node_to_inact=np.random.choice(nodes_act,1,p=p_inactive)
        nodes_act.remove(node_to_inact)
        nodes_act.append(node_new)

        # del nodes_act[inact_idx]
        # nodes_act.append(node_new)


    return graph



