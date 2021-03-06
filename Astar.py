import queue as Q

# g3 = {
#     'a': {'b': 2, 'c': 2},
#     'b': {'a': 2, 'd': 1},
#     'c': {'a': 2, 'd': 8, 'f': 3},
#     'd': {'b': 1, 'c': 8, 'e': 2, 's': 3},
#     'e': {'d': 2, 'h': 8, 'r': 2, 's': 9},
#     'f': {'c': 3, 'g': 2, 'r': 2},
#     'g': {'f': 2},
#     'h': {'e': 8, 'p': 4, 'q': 4},
#     'p': {'h': 4, 'q': 15, 's': 1},
#     'q': {'h': 4, 'p': 15},
#     'r': {'e': 2, 'f': 2},
#     's': {'d': 3, 'e': 9, 'p': 1}
# }
# heuristic = {'s': 0, 'a': 5, 'b': 7, 'c': 4, 'd': 7, 'e': 5, 'f': 2, 'g': 0, 'h': 11, 'p': 14, 'q': 12, 'r': 3}
import Distance
import getGraph


def astar(graph, start, goal):
    log2 = lat2 = ''
    for raw in open("cities2.txt", "rt"):
        a, b, c = raw.split()
        if a.casefold() == goal.casefold():
            x = b
            y = c
            break

    start = start.strip()
    goal = goal.strip()

    visited = []
    path = []
    prev = {}
    queue = Q.PriorityQueue()
    queue.put((0, start, None))
    h2 = 0
    h1 = 0
    max = queue.qsize()
    mycost = 0

    while queue:
        cost, node, prev_n = queue.get()
        if node not in visited:
            visited.append(node)
            prev[node] = prev_n
            if node == goal:
                while prev[node] != None:
                    path += [node]
                    node = prev[node]
                path += [start]
                for x in range(len(path) - 1):
                    mycost += graph[path[x]][path[x + 1]]
                return path[::-1], mycost, len(visited), max
            for i in graph[node]:
                if i not in visited:
                    total_cost = cost + graph[node].get(i)
                    for raw in open("cities2.txt", "rt"):
                        a, b, c = raw.split()
                        if a.casefold() == i.casefold():
                            try:
                                h1 = Distance.haversine(b, c, log2, lat2)
                                break
                            except:
                                h1 = 0
                    tempH = 0
                    for raw in open("cities2.txt", "rt"):
                        a, b, c = raw.split()
                        if a.casefold() == node.casefold():
                            try:
                                tempH = Distance.haversine(b, c, log2, lat2)
                                break
                            except:
                                tempH = 0

                    # h1 = heuristic[i]
                    total = total_cost + h1 - tempH  # heuristic[node]
                    queue.put((total, i, node))
                    if queue.qsize() > max:
                        max = queue.qsize()

#print(astar(getGraph.dict_graph, 'Abha', 'Afif'))
