import queue as Q

queue = Q.PriorityQueue()

g3 = {
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

g3_2 = {'a': [('b', 2), ('c', 2)],
          'b': [('a', 2), ('d', 1)],
          'c': [('a', 2), ('d', 8), ('f', 3)],
          'd': [('b', 1), ('c', 8), ('e', 2), ('S', 3)],
          'e': [('d', 2,), ('h', 8), ('r', 2), ('S', 9)],
          'f': [('c', 3), ('G', 2), ('r', 2)],
          'G': [('f', 2)],
          'h': [('e', 8), ('p', 4), ('q', 4)],
          'p': [('h', 4), ('q', 15), ('S', 1)],
          'q': [('h', 4), ('p', 15)],
          'r': [('e', 2), ('f', 2)],
          'S': [('d', 3), ('e', 9), ('p', 1)]}


print(g3_2['a'])
print(g3['a'])

for i ,x in g3_2['a']:
    print(i)
    #print(x)

for i in g3['a']:
    print(i)
    #print(g3['a'].get(i))

queue.put((0, 'a', None))
print(['a'])
print(queue.get())
