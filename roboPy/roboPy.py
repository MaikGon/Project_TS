
import time
import matplotlib.pyplot as plt

from robopy import *
import numpy as np
from .moves import move_j


def run(paths):
    model = Puma560()
    actions, whole_path = [], []
    for path in paths:
        for p in path:
            actions.append(p)

    hold = ["t_0_1", "k_0_1", "k_1_2", "k_2_1", "k_1_3", "k_3_0", "t_1_6", "t_6_1"]
    leave_good_arr = ["t_1_3", "t_1_4", "t_1_5"]
    leave_bad_arr = ["t_1_2"]
    come_back_good = ["t_3_1", "t_4_1", "t_5_1"]
    come_back_bad = ["t_2_1"]

    # define joint positions
    pick = [0.0, 180.0, 0.0, 0.0, 0.0, 0.0]                 # pick the product
    wait = [0.0, 90.0, 0.0, 0.0, 0.0, 0.0]                  # home position
    to_leave_good = [180.0, 90.0, 0.0, 0.0, 0.0, 0.0]       # spin the robot arm
    leave_good = [180.0, 180.0, 0.0, 0.0, 0.0, 0.0]         # leave the product on the pallete
    to_leave_bad = [-90.0, 90.0, 0.0, 0.0, 0.0, 0.0]        # spin the robot arm
    leave_bad = [-90.0, 180.0, 0.0, 0.0, 0.0, 0.0]          # reject the product

    # create path
    for ind, act in enumerate(actions):
        if act in hold:
            path = move_j(model, wait, wait, path_length=50)
            whole_path.append(path)

        elif act in leave_good_arr:
            path0 = move_j(model, wait, pick, path_length=80)
            path1 = move_j(model, pick, wait, path_length=50)
            path2 = move_j(model, wait, to_leave_good, path_length=40)
            path3 = move_j(model, to_leave_good, leave_good, path_length=80)
            path4 = move_j(model, leave_good, to_leave_good, path_length=50)
            whole_path.append(path0)
            whole_path.append(path1)
            whole_path.append(path2)
            whole_path.append(path3)
            whole_path.append(path4)

        elif act in leave_bad_arr:
            path0 = move_j(model, wait, pick, path_length=80)
            path1 = move_j(model, pick, wait, path_length=50)
            path2 = move_j(model, wait, to_leave_bad, path_length=40)
            path3 = move_j(model, to_leave_bad, leave_bad, path_length=80)
            path4 = move_j(model, leave_bad, to_leave_bad, path_length=50)
            whole_path.append(path0)
            whole_path.append(path1)
            whole_path.append(path2)
            whole_path.append(path3)
            whole_path.append(path4)

        elif act in come_back_good:
            path = move_j(model, to_leave_good, wait, path_length=40)
            whole_path.append(path)

        elif act in come_back_bad:
            path = move_j(model, to_leave_bad, wait, path_length=40)
            whole_path.append(path)

    print("\nSymulacja robopy")
    print("1. Inicjalizacja systemu (oczekiwanie)")
    print("2. Podniesienie przedmiotu")
    print("3. Odstawienie 1 przedmiotu na paletę")
    print("4. Powrót do pozycji home")
    print("5. Podniesienie przedmiotu")
    print("6. Odstawienie 2 przedmiotu na paletę")
    print("7. Powrót do pozycji home")
    print("8. Podniesienie przedmiotu")
    print("9. Odrzucenie wadliwego produktu")
    print("10. Powrót do pozycji home")
    print("11. Podniesienie przedmiotu")
    print("12. Odstawienie 3 przedmiotu na paletę")
    print("13. Powrót do pozycji home")
    print("14. Podniesienie przedmiotu")
    print("15. Odstawienie 1 przedmiotu na paletę")
    print("16. Powrót do pozycji home")
    print("17. Obsługa awarii (oczekiwanie)")
    print("18. Podniesienie przedmiotu")
    print("19. Odstawienie 1 przedmiotu na paletę")
    print("20. Powrót do pozycji home")
    print("21. Podniesienie przedmiotu")
    print("22. Odstawienie 2 przedmiotu na paletę")
    print("23. Powrót do pozycji home")

    path = np.concatenate(whole_path, axis=0)
    model.animate(stances=path, frame_rate=30, unit='deg')

