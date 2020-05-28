import stateMachine
import networkX
import roboPy
import matplotlib.pyplot as plt

def main():
    plt.ion()
    path_1 = ["t_0_1", "t_1_3", "t_3_1", "t_1_4", "t_4_1", "t_1_2", "t_2_1", "t_1_5", "t_5_1", "t_1_3", "t_3_1",
              "t_1_6"]
    path_2 = ["k_0_1", "k_1_2", "k_2_1", "k_1_3", "k_3_0"]
    path_3 = ["t_6_1", "t_1_3", "t_3_1", "t_1_4", "t_4_1"]
    paths = [path_1,  path_3]
    supervisor, master_transitions = stateMachine.create()
    G, edge_labels, pos = networkX.create()

    start = input('start: ')
    finish = input('finish: ')
    path = networkX.search(G, start, finish)
    print('path: ', path)


    subordinate, subordinate_transitions = stateMachine.createH()
    H, edge_labels2, pos2 = networkX.createH()
    prev = None
    for path in paths:
        for event in path:
            cur_state = stateMachine.run(supervisor, master_transitions, event)
            plt.cla()
            prev = networkX.draw(G, cur_state, prev, edge_labels, pos)
        if prev == "b6":
            for eve in path_2:
                cur_state = stateMachine.runH(subordinate, subordinate_transitions, eve)
                plt.cla()
                prev = networkX.drawH(H, cur_state, prev, edge_labels2, pos2)
    plt.close()
    roboPy.run()


if __name__ == '__main__':
    main()
