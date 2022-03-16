import Distance

try:
    import queue
except ImportError:
    import Queue as queue

from queue import PriorityQueue
import getGraph


# graph3 = {
#     'a': {'b':2,'c':2},
#     'b': {'a':2,'d':1},
#     'c': {'a':2,'d':8,'f':3},
#     'd': {'b':1,'c':8,'e':2,'s':3},
#     'e': {'d':2,'h':8,'r':2,'s':9},
#     'f': {'c':3,'g':2,'r':2},
#     'g': {'f':2},
#     'h': {'e':8,'p':4,'q':4},
#     'p': {'h':4,'q':15,'s':1},
#     'q': {'h':4,'p':15},
#     'r': {'e':2,'f':2},
#     's': {'d':3,'e':9,'p':1}
# }
#
# heuristic = {'s': 0, 'a': 5, 'b': 7, 'c': 4, 'd': 7, 'e': 5, 'f': 2, 'g': 0, 'h':11, 'p': 14, 'q': 12, 'r': 3}

def Greedy(graph, start, goal):
    log2 = lat2 = ''
    for raw in open("cities2.txt", "rt"):
        a, b, c = raw.split()
        if a.casefold() == goal.casefold():
            x = b
            y = c
            break

    start = start.strip()
    goal = goal.strip()
    visited = set()
    expanded = []
    queue = PriorityQueue()
    queue.put((0, [start], start))

    max = 0
    mycost = 0

    while queue:
        # node = []
        cost, node, tempNode = queue.get()
        # print(x)
        # if type(x) == list:
        #     for r in x:
        #         node.append(x)
        # else:
        #     node.append(x)
        # print(node)
        # if type(node) == str:
        #     current = node
        # else:
        #     current = node[len(node)-1]
        current = node[len(node) - 1]
        if current not in visited:
            visited.add(current)
            expanded.append(current)
            if current.casefold() == goal.casefold():
                # print(node)
                for x in range(len(node) - 1):
                    print(graph[node[x]][node[x + 1]])
                    try:
                        mycost += graph[node[x]][node[x + 1]]
                    except:
                        print(node[x])

                return node, mycost, len(visited), max

            neighbours = graph[current]
            total_cost = 0
            for i in neighbours:
                if i not in visited:
                    for raw in open("cities2.txt", "rt"):
                        a, b, c = raw.split()
                        if a.casefold() == i.casefold():
                            try:
                                total_cost = Distance.haversine(b, c, log2, lat2)
                                break
                            except:
                                total_cost = 0

                    # total_cost = heuristic[i]
                    # node.append(i)
                    queue.put((total_cost, node + [i], i))
                    if queue.qsize() > max:
                        max = queue.qsize()

# print(Greedy(getGraph.dict_graph, 'Abha', 'Ad-Dawadimi'))
