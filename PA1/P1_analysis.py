import sys

import matplotlib.pyplot as plt
import networkx as nx
from random_graph import *
import json
import collections
import matplotlib.pyplot as plt
from pagerank import *

str_format='u: {} || N : {} || average page length : {}'

u_list=[0, 0.2, 0.4, 0.6, 0.8, 1.0]
N_list=[2000, 4000, 6000, 8000, 10000]

# result=[]
# for u in u_list:
#     G = nx.Graph(preferential_attachment(u=u))
#     degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
#     # print "Degree sequence", degree_sequence
#     degreeCount = collections.Counter(degree_sequence)
#     deg, cnt = zip(*degreeCount.items())
#
#     fig, ax = plt.subplots()
#     plt.plot(deg, cnt, color='b')
#
#     plt.title("Degree Histogram")
#     plt.ylabel("Count")
#     plt.xlabel("Degree")
#     ax.set_xticks([d + 0.4 for d in deg])
#     ax.set_xticklabels(deg)
#
#     plt.savefig('u_{}_figure.png'.format(u))
#     print('{} done'.format(u))

# result=[]
# for u in u_list:
#     for N in N_list:
#         graph = nx.Graph(preferential_attachment(u=u, N=N))
#         avg_p_len=nx.average_shortest_path_length(graph)
#         result.append(str_format.format(u,N,avg_p_len))
#         print(result[-1])
#
#
# with open('P1_result_average_path_length.json', 'w') as f:
#     # pdb.set_trace()
#     json.dump(result, f)

#
# str_format='u: {} || N : 10000 || average clustering coeff : {}'
# result=[]
# u_list=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# for u in u_list:
#     graph = nx.Graph(preferential_attachment(u=u))
#     c_eff=nx.average_clustering(graph)
#     result.append(str_format.format(u, c_eff))
#
# with open('P1_result_average_c_eff.json', 'w') as f:
#     # pdb.set_trace()
#     json.dump(result, f)




################################### PA1-2 #################################################
# webStanford='web-Stanford.txt'
#
# nodes = {}
# id2node={}
# graph=[]
# with open(webStanford,'rt',encoding='UTF8') as f:
#     for line in f:
#         (from_, to_) = line.split()
#         graph.append((from_,to_))
#
# f.close()
#
# with open('WebStanford.json', 'w') as f:
#     # pdb.set_trace()
#     json.dump(graph, f)

webStan=json.load(open('WebStanford.json'))
webStan=[tuple(edge) for edge in webStan]
damping_list =[0.1, 0.3, 0.5, 0.7, 0.9]
result=[]
str_format='damp factor : {}  ||   top-10: {}'

for dmp in damping_list:
    tmp=pagerank(webStan,damping_factor=dmp)
    result.append(str_format.format(dmp,str(tmp[:10])))
    print('dmp : {} done'.format(dmp))

with open('WebStan_result.json', 'w') as f:
    # pdb.set_trace()
    json.dump(result, f)
