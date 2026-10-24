# Search Methods 4

A Python/PyQt5 graph-search experiment comparing A*-style and greedy best-first search over a Saudi city graph, with PyVis visualizations and geographic-distance helper code.

## Run

Use Python 3 and a graphical desktop. Create and activate a virtual environment, then run from the repository directory:

```bash
python -m pip install PyQt5 PyQtWebEngine pyvis
python SEARCH_GUI.py
```

Select source/destination cities and a search action in the GUI. Working-directory data files must remain available. Graph visualization generates HTML files that may replace earlier outputs with the same names.

## Source and data

- [`SEARCH_GUI.py`](SEARCH_GUI.py): GUI and embedded graph view.
- [`Astar.py`](Astar.py), [`Greedy.py`](Greedy.py): experimental search implementations.
- [`Distance.py`](Distance.py): haversine-distance helper.
- [`getGraph.py`](getGraph.py): hardcoded weighted city adjacency map.
- [`cities2.txt`](cities2.txt): city-coordinate rows used by heuristic code.
- Other scripts and text files contain alternate data/experiments, not one unified application.

## Important limitations

These implementations should not be treated as verified A* or route planning. Destination-coordinate variables used in heuristic calls remain empty strings, and coordinate values are read as strings; exceptions fall back to zero heuristics. Both searches loop on a queue object's truthiness and can block when an unreachable search exhausts its queue.

City spelling/data consistency and graph costs are not independently validated. PyQt/PyVis APIs are unpinned, and build/runtime/service behavior has not been tested for this documentation refresh.
