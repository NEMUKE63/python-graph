from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import maximum_flow

gr = digraph()
gr.add_nodes([0,1,2,3,4,5,6,7,8,9,10])

gr.add_edge((0, 1), wt=15)
gr.add_edge((0, 2), wt=7)
gr.add_edge((1, 2), wt=1)
gr.add_edge((1, 3), wt=8)
gr.add_edge((1, 4), wt=4)
gr.add_edge((2, 3), wt=6)
gr.add_edge((2, 5), wt=2)
gr.add_edge((3, 5), wt=3)
gr.add_edge((3, 6), wt=8)
gr.add_edge((4, 6), wt=7)
gr.add_edge((5, 4), wt=7)
gr.add_edge((5, 6), wt=1)
gr.add_edge((5, 7), wt=3)
gr.add_edge((5, 9), wt=4)
gr.add_edge((6, 8), wt=4)
gr.add_edge((6,10), wt=8)
gr.add_edge((7, 8), wt=5)
gr.add_edge((7, 9), wt=2)
gr.add_edge((8,10), wt=6)
gr.add_edge((9,10), wt=3)

flows,cuts = maximum_flow(gr,0,10)
print('flow is:' + str(flows))
print('cut is:'  + str(cuts))