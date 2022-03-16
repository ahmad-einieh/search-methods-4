
import Distance
import queue
from queue import PriorityQueue

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
    queue = PriorityQueue()
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
                    #total_cost = cost + graph[node].get(i)
                    for raw in open("cities2.txt", "rt"):
                        a, b, c = raw.split()
                        if a.casefold() == i.casefold():
                            try:
                                h1 = Distance.haversine(b, c, log2, lat2)
                                break
                            except:
                                h1 = 0

                    queue.put((h1, i, node))
                    if queue.qsize() > max:
                        max = queue.qsize()

print(astar(getGraph.dict_graph,"Abha",'Afif'))