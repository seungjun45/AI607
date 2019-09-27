import copy

def pagerank(graph, damping_factor=0.85):
    """
    Implement the variant of pagerank described in Section 2.2.
    Inputs:
    graph: directed input graph in the edge list format.
    That is, graph is a list of tuples of the form (u, v),
    which indicates that there is a directed link u -> v.
    You can assume that both u and v are integers, while you cannot
    assume that the integers are within a specific range.
    You can assume that there is no isolated node.
    damping_factor: damping factor of the variant of pagerank
    Output: a list of tuples of the form (v, score), which indicates node v
    and its pagerank score. The list should be sorted in the decreasing
    order of pagerank scores. If multiple nodes have the same pagerank
    score, then return them in any order.
    """
    in_deg = {}
    out_deg = {}
    M_ = {}
    ## initialization

    for edge in graph:
        if edge[0] not in out_deg:
            out_deg[edge[0]] = 0
        if edge[1] not in in_deg:
            in_deg[edge[1]] = 0
        out_deg[edge[0]] = out_deg[edge[0]] + 1
        in_deg[edge[1]] = in_deg[edge[1]] + 1

    pages = list(set(out_deg.keys()).union(set(in_deg.keys())))
    page_importance = {}
    for page in pages:
        page_importance[page] = 1 / len(pages)
        if page not in in_deg:
            in_deg[page] = 0
        if page not in out_deg:
            out_deg[page] = 0

    for edge in graph:
        M_[edge] = 1 / out_deg[edge[0]]

    error = 1
    page_importance_zeros = {}
    for page in pages:
        page_importance_zeros[page] = 0

    num_in_degrees = sum(list(in_deg.values()))
    num_in_degrees = num_in_degrees + len(pages)

    while error > 1e-7:
        page_importance_new = copy.deepcopy(page_importance_zeros)
        for edge in graph:
            page_importance_new[edge[1]] = page_importance_new[edge[1]] + page_importance[edge[0]] / out_deg[
                edge[0]] * damping_factor

        for page in pages:
            if page in out_deg:
                multi_coeff=(1 - damping_factor)
            else:
                multi_coeff=1.0
            page_importance_new[page] = page_importance_new[page] +  multi_coeff* (
                        1 + in_deg[page]) / num_in_degrees

        diff = [abs(page_importance_new[page] - page_importance[page]) for page in pages]
        error = max(diff)
        page_importance = page_importance_new
        print('max diff is : {}'.format(error))

    tmp = [(page, page_importance_new[page]) for page in pages]

    return sorted(tmp, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    # tmp=preferential_attachment()
    tmp=pagerank([(2,3),(3,2),(4,1),(4,2),(5,2),(5,4),(5,6),(6,2),(6,5),(7,2),(7,5),(8,2),(8,5),(9,2),(9,5),(10,5),(11,5)],damping_factor=0.85)
    print(tmp)
    # pdb.set_trace()