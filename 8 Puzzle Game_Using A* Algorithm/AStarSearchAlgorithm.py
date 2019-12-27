from PriorityQueue import PriorityQueue as Queue
from puzzle import Puzzle
import pydot


initial_state= [2, 8, 3,
                1, 6, 4,
                7, 0, 5]

def draw_legend(graph):
    graphlegend = pydot.Cluster(graph_name="legend", label="Legend", fontsize="20", color="red",
                                fontcolor="blue", style="filled", fillcolor="white")

    legend1 = pydot.Node('Processed ', shape="plaintext")
    graphlegend.add_node(legend1)

    legend3 = pydot.Node('Goal', shape="plaintext")
    graphlegend.add_node(legend3)


    node1 = pydot.Node("1", style="filled", fillcolor="green", label="")
    graphlegend.add_node(node1)

    node3 = pydot.Node("3", style="filled", fillcolor="gold", label="")
    graphlegend.add_node(node3)

    graph.add_subgraph(graphlegend)
    graph.add_edge(pydot.Edge(legend1, legend3, style="invis"))

    graph.add_edge(pydot.Edge(node1, node3, style="invis"))



def AStarAlgorithm(initial_state):
    graph = pydot.Dot(graph_type='digraph', label="8 Puzzle State Space (A* Algorithm)", fontsize="30", color="red",
                  fontcolor="blue", style="filled", fillcolor="black")

    start_node = Puzzle(initial_state, None, None,0)

    if start_node.goal_test():
        return start_node.find_solution()

    s=Queue()
    s.push(start_node)
    explored=[]
    print("The starting node is \ndepth=%d\n" % start_node.depth)
    print(start_node.display())

    finished = False
    while not(s.isEmpty()):
        v = s.pop()
        node=v[-1]
        print(node.display())
        explored.append(node.state)
        graph.add_node(node.graph_node)

        if node.parent:
            graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node,label="h(n) = " + str(v[0]) + " g(n) = " + str(node.depth)))

        if not finished:
            children=node.generate_child()
            for child in children:
                if child.state not in explored :
                    print("depth=%d\n"%child.depth)
                    print(child.display())

                    if child.goal_test():
                        print("This is the goal state")
                        graph.add_node(child.graph_node)
                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node, label="h(n) = " + str(v[0]) + " g(n) = " + str(node.depth)))
                        draw_legend(graph)
                        finished=True
                    else:
                        s.push(child)
        else:
            graph.write_png('Solution_Original.png')
    return


AStarAlgorithm(initial_state)
