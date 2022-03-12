import pyvis.network

nameOfGraph = "temp.html"
pyvis_graph = pyvis.network.Network(notebook=True, height="100%", width="100%", bgcolor="#222222", font_color="#FFFFFF")

graph3 = {
    'a': {'b':2,'c':2},
    'b': {'a':2,'d':1},
    'c': {'a':2,'d':8,'f':3},
    'd': {'b':1,'c':8,'e':2,'s':3},
    'e': {'d':2,'h':8,'r':2,'s':9},
    'f': {'c':3,'g':2,'r':2},
    'g': {'f':2},
    'h': {'e':8,'p':4,'q':4},
    'p': {'h':4,'q':15,'s':1},
    'q': {'h':4,'p':15},
    'r': {'e':2,'f':2},
    's': {'d':3,'e':9,'p':1}
}
heuristic = {'s': 0, 'a': 5, 'b': 7, 'c': 4, 'd': 7, 'e': 5, 'f': 2, 'g': 0, 'h':11, 'p': 14, 'q': 12, 'r': 3}


for i in graph3:
    pyvis_graph.add_node(i,label=i,title=str(heuristic[i]))

for i in graph3:
    for j in graph3[i]:
        pyvis_graph.add_edge(i,j ,label=graph3[i].get(j), title=graph3[i].get(j))


pyvis_graph.force_atlas_2based()
pyvis_graph.show(nameOfGraph)