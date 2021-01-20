from graph import UndirectedGraph
from collections import deque


def PathTo(graph, a, b):
    flag = 0
    visited = set()
    dic = dict()
    stack = deque()

    a_obj = graph.get_vertex(a)
    stack.append(a_obj)
    while stack:
        if flag == 1:
            break
        vertex = stack.pop()
        if vertex in visited:
            continue

        visited.add(vertex)
        for i in vertex.get_neighbour():
            if i not in visited:
                stack.append(i)
                dic[i.get_key()] = vertex.get_key()
                if i.get_key() == b:
                    flag = 1
                    break
        if flag == 1:
            break

    if dic.get(b, None) == None:
        return f'No link Between two node'
    k = b
    # print(dic)
    lst = list()
    while 1:
        lst.append(k)
        if k == a:
            break
        k = dic[k]


    return lst[::-1]


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
        12: []
    }

    undirectedgraph = UndirectedGraph()
    for i in nodes:
        undirectedgraph.add_vertex(i)

    for i in nodes:
        k = nodes[i]
        for j in k:
            undirectedgraph.add_edge(i, j)

    src = 1
    des = 4
    print(f'{src} to {des}: ', end="")
    print(PathTo(undirectedgraph, src, des))


if __name__ == '__main__':
    main()

