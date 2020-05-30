import stateMachine
import networkX
import roboPy
import matplotlib.pyplot as plt


def main():
    plt.ion()
    # create 3 different paths
    path_1 = ["t_0_1", "t_1_3", "t_3_1", "t_1_4", "t_4_1", "t_1_2", "t_2_1", "t_1_5", "t_5_1", "t_1_3", "t_3_1",
              "t_1_6"]
    path_2 = ["k_0_1", "k_1_2", "k_2_1", "k_1_3", "k_3_0"]
    path_3 = ["t_6_1", "t_1_3", "t_3_1", "t_1_4", "t_4_1"]
    paths = [path_1, path_3]
    roboPy_paths = [path_1, path_2, path_3]

    # create stateMachines
    supervisor, master_transitions = stateMachine.create()
    subordinate, subordinate_transitions = stateMachine.createH()

    # create DiGraphs
    G, edge_labels, pos = networkX.create()
    H, edge_labels2, pos2 = networkX.createH()

    # check the graph
    print("Provide the first and the last state of the path:")
    start = input('start: ')
    finish = input('finish: ')
    graph = input('graph (G or H): ')
    if graph == "H":
        path = networkX.search(H, start, finish)
    elif graph == "G":
        path = networkX.search(G, start, finish)
    print('path: ', path)

    # launch the system
    prev = None
    for path in paths:
        for event in path:
            cur_state = stateMachine.run(supervisor, master_transitions, event)
            plt.cla()
            prev = networkX.draw(G, cur_state, prev, edge_labels, pos)
        if prev == "b6":
            for eve in path_2:
                cur_state = stateMachine.run(subordinate, subordinate_transitions, eve)
                plt.cla()
                prev = networkX.drawH(H, cur_state, prev, edge_labels2, pos2)
    plt.close()
    roboPy.run(roboPy_paths)


if __name__ == '__main__':
    main()
