from statemachine import StateMachine, State, Transition
import time
import matplotlib.pyplot as plt
from robopy import *
import numpy as np

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

def create():
   


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


