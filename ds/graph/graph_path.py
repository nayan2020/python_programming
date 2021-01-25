
from graph import UndirectedGraph
from collections import deque


def PathTo_dfs(graph, src_v, dst_v):
    """
    Time complexity O(V+E)
    space complexity O(V)
    :param graph:
    :param src_v:
    :param dst_v:
    :return: bool or list
    """
    # If the vertex is not present in the graph, return False
    if not (graph.get_vertex(src_v) and graph.get_vertex(dst_v)):
        return f'Two vertex is not in same graph'
    # Identify the visited node, which is visited already
    visited = set()

    # Tracing the path
    dic = dict()

    # add the graph vertex
    stack = deque()

    # find the destination and end the loop
    flag = 0

    src_v_obj = graph.get_vertex(src_v)
    stack.append(src_v_obj)
    while stack:

        vertex = stack.pop()
        if vertex in visited:
            continue

        visited.add(vertex)
        for neighbour in vertex.get_neighbour():
            # If the neighbour is not visited then add in stack
            if neighbour not in visited:
                stack.append(neighbour)
                dic[neighbour.get_key()] = vertex.get_key()
            # If the destination is find then flag become 1
            if neighbour.get_key() == dst_v:
                flag = 1
                # exit from the for loop
                break

        if flag == 1:
            # exit from the while loop
            break

    # same graph two node but not connected
    # if flag == 1 that's mean, destination node is present
    if flag == 1:
        k = dst_v
        lst = list()
        while k != src_v:
            lst.append(k)
            k = dic[k]
        lst.append(src_v)

        return lst[::-1]
    else:
        return f'No link Between two node'


def main():
    nodes = {
        0: [1, 2, 5, 6],
        1: [],
        2: [],
        3: [4, 5],
        4: [6],
        5: [],
        6: [],
        7: [8],
        8: [],
        9: [10, 11, 12],
        10: [],
        11: [12],
        12: [],

    }

    undirectedgraph = UndirectedGraph()
    for i in nodes:
        undirectedgraph.add_vertex(i)

    for i in nodes:
        k = nodes[i]
        for j in k:
            undirectedgraph.add_edge(i, j)

    src = 2
    des = 3
    print(f'{src} to {des}: ', end="")
    print(PathTo_dfs(undirectedgraph, src, des))


if __name__ == '__main__':
    main()

