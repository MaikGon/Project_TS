import matplotlib.pyplot as plt
import networkx as nx
import time

def create():
    G = nx.DiGraph()
    G.add_nodes_from([0, 1, 2, 3, 4, 5, 6])
    G.add_edges_from([(0, 1)], label='t0')
    G.add_edges_from([(1, 2)], label='t1')
    G.add_edges_from([(2, 1)], label='t2')
    G.add_edges_from([(1, 3)], label='t3')
    G.add_edges_from([(3, 1)], label='t4')
    G.add_edges_from([(1, 4)], label='t5')
    G.add_edges_from([(4, 1)], label='t6')
    G.add_edges_from([(1, 5)], label='t7')
    G.add_edges_from([(5, 1)], label='t8')
    G.add_edges_from([(1, 6)], label='t9')
    G.add_edges_from([(6, 1)], label='t10')
    edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
    pos = nx.spring_layout(G)
    return G, edge_labels, pos


def draw(G, cur_state, prev, edge_labels, pos):

    if prev == None:
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_nodes(G, pos, nodelist=range(1, 7), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 1), node_size=400, node_color='r')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b0"
        print("Inicjalizacja")
    if prev == "a0":
        print("Obsługa awarii")
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 6), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(6, 7), node_size=400, node_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b6"

    if cur_state == "b1":
        print("Oczekiwanie na produkt")
        nx.draw_networkx_nodes(G, pos, nodelist=range(2, 7), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 1), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(1, 2), node_size=400, node_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        if prev == "b0":
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(0, 1):'t0'}, label_pos=(0.4), font_size=11, font_color='r')
            nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.edges(0, 1), edge_color='r',width=1.2)

        if prev == "b2":
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(2, 1): 't2'}, label_pos=(0.4), font_size=11, font_color='r')
            nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.edges(2, 1),
                                   edge_color='r', width=1.2)

        if prev == "b3":
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(3, 1): 't4'}, label_pos=(0.4), font_size=11,
                                         font_color='r')
            nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.edges(3, 1),
                                   edge_color='r',width=1.2)

        if prev == "b4":
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(4, 1): 't6'}, label_pos=(0.4), font_size=11,
                                         font_color='r')
            nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.edges(4, 1),
                                   edge_color='r',width=1.2)
        if prev == "b5":
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(5, 1): 't8'}, label_pos=(0.4), font_size=11,
                                         font_color='r')
            nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.edges(5, 1),
                                   edge_color='r',width=1.2)
        if prev == "b6":
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(6, 1): 't10'}, label_pos=(0.4), font_size=11,
                                         font_color='r')
            nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.edges(6, 1),
                                   edge_color='r', width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b1"

    if cur_state == "b2":
        print("Robot odrzuca produkt")
        nx.draw_networkx_nodes(G, pos, nodelist=range(3, 7), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 2), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(2, 3), node_size=400, node_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(1, 2): 't1'}, label_pos=(0.4), font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.in_edges(2),
                               edge_color='r',width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b2"

    if cur_state == "b3":
        print("Robot układa produkt na 1 miejscu")
        nx.draw_networkx_nodes(G, pos, nodelist=range(4, 7), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 3), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(3, 4), node_size=400, node_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(1, 3): 't3'}, label_pos=(0.4), font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.in_edges(3),
                               edge_color='r',width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b3"

    if cur_state == "b4":
        print("Robot układa produkt na 2 miejscu")
        nx.draw_networkx_nodes(G, pos, nodelist=range(5, 7), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 4), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(4, 5), node_size=400, node_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(1, 4): 't5'}, label_pos=(0.4), font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.in_edges(4),
                               edge_color='r',width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b4"

    if cur_state == "b5":
        print("Robot układa produkt na 3 miejscu, pudełko pełne, podstawienie nowego pudełka")
        nx.draw_networkx_nodes(G, pos, nodelist=range(6, 7), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 5), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(5, 6), node_size=400, node_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(1, 5): 't7'}, label_pos=(0.4), font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.in_edges(5),
                               edge_color='r',width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b5"

    if cur_state == "b6":
        print("Obsługa awarii")
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 6), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(6, 7), node_size=400, node_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(1, 6): 't9'}, label_pos=(0.4), font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2', edgelist=G.in_edges(6),
                               edge_color='r', width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "b6"

    return prev

def createH():
    H = nx.DiGraph()
    H.add_nodes_from([0, 1, 2, 3])
    H.add_edges_from([(0, 1)], label='k0')
    H.add_edges_from([(1, 2)], label='k1')
    H.add_edges_from([(2, 1)], label='k2')
    H.add_edges_from([(1, 3)], label='k3')
    H.add_edges_from([(3, 0)], label='k4')

    edge_labels2 = {(n1, n2): d['label'] for n1, n2, d in H.edges(data=True)}
    pos2 = nx.spring_layout(H)
    return H, edge_labels2, pos2

def drawH(H, cur_state, prev, edge_labels2, pos2):

    if prev == "b6":
        nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_nodes(H, pos2, nodelist=range(1, 4), node_size=400)
        nx.draw_networkx_nodes(H, pos2, nodelist=range(0, 1), node_size=400, node_color='r')
        nx.draw_networkx_labels(H, pos2)
        nx.draw_networkx_edge_labels(H, pos2, edge_labels=edge_labels2, label_pos=(0.4), font_size=9)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)

        prev = "a0"
        print("Oczekiwanie na awarie")

    if cur_state == "a0" and prev == "a3":
        print("Oczekiwanie na awarie")
        nx.draw_networkx_nodes(H, pos2, nodelist=range(1, 4), node_size=400)
        nx.draw_networkx_nodes(H, pos2, nodelist=range(0, 1), node_size=400, node_color='r')
        nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(H, pos2)
        nx.draw_networkx_edge_labels(H, pos2, edge_labels=edge_labels2, label_pos=(0.4), font_size=9)
        nx.draw_networkx_edge_labels(H, pos2, edge_labels={(3, 0): 'k4'}, label_pos=(0.4),
                                     font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2', edgelist=H.in_edges(0),
                               edge_color='r', width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "a0"

    if cur_state == "a1":
        print("Testowanie systemu")
        if prev == "a0":
            nx.draw_networkx_nodes(H, pos2, nodelist=range(0, 1), node_size=400)
            nx.draw_networkx_nodes(H, pos2, nodelist=range(2, 4), node_size=400)
            nx.draw_networkx_nodes(H, pos2, nodelist=range(1, 2), node_size=400, node_color='r')
            nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2')
            nx.draw_networkx_labels(H, pos2)
            nx.draw_networkx_edge_labels(H, pos2, edge_labels=edge_labels2, label_pos=(0.4), font_size=9)
            nx.draw_networkx_edge_labels(H, pos2, edge_labels={(0, 1): 'k0'}, label_pos=(0.4),
                                         font_size=11,
                                         font_color='r')
            nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2', edgelist=H.out_edges(0),
                                   edge_color='r', width=1.2)
            plt.show()
            plt.pause(0.001)
            time.sleep(2)
        if prev == "a2":
            nx.draw_networkx_nodes(H, pos2, nodelist=range(0, 1), node_size=400)
            nx.draw_networkx_nodes(H, pos2, nodelist=range(2, 4), node_size=400)
            nx.draw_networkx_nodes(H, pos2, nodelist=range(1, 2), node_size=400, node_color='r')
            nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2')
            nx.draw_networkx_labels(H, pos2)
            nx.draw_networkx_edge_labels(H, pos2, edge_labels=edge_labels2, label_pos=(0.4),
                                         font_size=9)
            nx.draw_networkx_edge_labels(H, pos2, edge_labels={(2, 1): 'k2'}, label_pos=(0.4),
                                         font_size=11,
                                         font_color='r')
            nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2', edgelist=H.out_edges(2),
                                   edge_color='r', width=1.2)
            plt.show()
            plt.pause(0.001)
            time.sleep(2)
            prev = "a1"
    if cur_state == "a2":
        print("Obsługa awarii")
        nx.draw_networkx_nodes(H, pos2, nodelist=range(0, 2), node_size=400)
        nx.draw_networkx_nodes(H, pos2, nodelist=range(3, 4), node_size=400)
        nx.draw_networkx_nodes(H, pos2, nodelist=range(2, 3), node_size=400, node_color='r')
        nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(H, pos2)
        nx.draw_networkx_edge_labels(H, pos2, edge_labels=edge_labels2, label_pos=(0.4), font_size=9)
        nx.draw_networkx_edge_labels(H, pos2, edge_labels={(1, 2): 'k1'}, label_pos=(0.4),
                                     font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2', edgelist=H.in_edges(2),
                               edge_color='r', width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "a2"

    if cur_state == "a3":
        print("System działa prawidłowo")
        nx.draw_networkx_nodes(H, pos2, nodelist=range(0, 3), node_size=400)
        nx.draw_networkx_nodes(H, pos2, nodelist=range(3, 4), node_size=400, node_color='r')
        nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_labels(H, pos2)
        nx.draw_networkx_edge_labels(H, pos2, edge_labels=edge_labels2, label_pos=(0.4),
                                     font_size=9)
        nx.draw_networkx_edge_labels(H, pos2, edge_labels={(1, 3): 'k3'}, label_pos=(0.4),
                                     font_size=11,
                                     font_color='r')
        nx.draw_networkx_edges(H, pos2, connectionstyle='arc3,rad=0.2', edgelist=H.in_edges(3),
                               edge_color='r', width=1.2)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        prev = "a3"
    return prev



def search(G, start, finish):
    min_len = 100
    for path in nx.all_simple_paths(G, int(start), int(finish)):
        if len(path) <= min_len:
            shortest = path

    return shortest


