from statemachine import StateMachine, State, Transition
import time
import matplotlib.pyplot as plt
import networkx as nx

class Generator(StateMachine):
    states = []
    transitions = []
    states_map = {}
    current_state = None

    def __init__(self, states, transitions):

        # creating each new object needs clearing its variables (otherwise they're duplicated)
        self.states = []
        self.transitions = []
        self.states_map = {}
        self.current_state = states[0]

        # create fields of states and transitions using setattr()
        # create lists of states and transitions
        # create states map - needed by StateMachine to map states and its values
        for s in states:
            setattr(self, str(s.name).lower(), s)
            self.states.append(s)
            self.states_map[s.value] = str(s.name)

        for key in transitions:
            setattr(self, str(transitions[key].identifier).lower(), transitions[key])
            self.transitions.append(transitions[key])

        # super() - allows us to use methods of StateMachine in our Generator object
        super(Generator, self).__init__()

    # define a printable introduction of a class
    def __repr__(self):
        return "{}(model={!r}, state_field={!r}, current_state={!r})".format(
            type(self).__name__, self.model, self.state_field,
            self.current_state.identifier,
        )

    # method of creating objects in a flexible way (we can define multiple functions
    # which will create objects in different ways)
    @classmethod
    def create_master(cls, states, transitions) -> 'Generator':
        return cls(states, transitions)

def main():

    plt.ion()
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


    edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
    pos = nx.spring_layout(G)

    options = [
        {"name": "B0", "initial": True, "value": "b0"},  # 0
        {"name": "B1", "initial": False, "value": "b1"},  # 1
        {"name": "B2", "initial": False, "value": "b2"},  # 2
        {"name": "B3", "initial": False, "value": "b3"},  # 3
        {"name": "B4", "initial": False, "value": "b4"},  # 4
        {"name": "B5", "initial": False, "value": "b5"},  # 5
        {"name": "B6", "initial": False, "value": "b6"}]  # 6

    master_states = [State(**opt) for opt in options]

    form_to = [
        [0, [1]],
        [1, [2, 3, 4, 5, 6]],
        [2, [1]],
        [3, [1]],
        [4, [1]],
        [5, [1]],
        [6, []]
    ]

    # create transitions for a master (as a dict)
    master_transitions = {}
    for indices in form_to:
        from_idx, to_idx_tuple = indices  # unpack list of two elements into separate from_idx and to_idx_tuple
        for to_idx in to_idx_tuple:  # iterate over destinations from a source state
            op_identifier = "t_{}_{}".format(from_idx, to_idx)  # parametrize identifier of a transition

            # create transition object and add it to the master_transitions dict
            transition = Transition(master_states[from_idx], master_states[to_idx], identifier=op_identifier)
            master_transitions[op_identifier] = transition

            # add transition to source state
            master_states[from_idx].transitions.append(transition)

    path_1 = ["t_0_1", "t_1_2", "t_2_1", "t_1_3", "t_3_1"]
    path_2 = ["t_0_1", "t_1_3", "t_3_1", "t_1_6"]
    path_3 = ["t_0_1", "t_1_3", "t_3_1", "t_1_4", "t_4_1", "t_1_5", "t_5_1"]

    paths = [path_1, path_2, path_3]

    for path in paths:

        # create a supervisor
        supervisor = Generator.create_master(master_states, master_transitions)
        print('\n' + str(supervisor))

        # run supervisor for exemplary path
        nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=0.2')
        nx.draw_networkx_nodes(G, pos, nodelist=range(1, 7), node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=range(0, 1), node_size=400, node_color='r')
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=(0.4), font_size=9)
        plt.show()
        plt.pause(0.001)
        time.sleep(2)
        print("Executing path: {}".format(path))
        prev = "b0"
        print("Inicjalizacja")
        for event in path:

            # launch a transition in our supervisor
            master_transitions[event]._run(supervisor)
            print(supervisor.current_state)

            if supervisor.current_state.value == "b1":
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

                plt.show()
                plt.pause(0.001)
                time.sleep(2)
                prev = "b1"

            if supervisor.current_state.value == "b2":
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

            if supervisor.current_state.value == "b3":
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

            if supervisor.current_state.value == "b4":
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

            if supervisor.current_state.value == "b5":
                print("Robot układa produkt na 3 miejscu, pudełko pełne")
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

            if supervisor.current_state.value == "b6":
                print("Awaria, DEADLOCK")
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

        plt.close()

if __name__ == '__main__':
    main()