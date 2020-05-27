
import time
import matplotlib.pyplot as plt

from robopy import *
import numpy as np
from .moves import move_j


def run():
    model = Puma560()
    # define joint positions
    pick = [0.0, 180.0, 0.0, 0.0, 0.0, 0.0]                 #podniesienie
    wait = [0.0, 90.0, 0.0, 0.0, 0.0, 0.0]                  #pozycja wyjsciowa
    to_leave_good = [180.0, 90.0, 0.0, 0.0, 0.0, 0.0]       #podejscie do zaladowania
    leave_good = [180.0, 180.0, 0.0, 0.0, 0.0, 0.0]         #zaladowanie
    to_leave_bad = [-90.0, 90.0, 0.0, 0.0, 0.0, 0.0]        #podejscie do odrzucenia
    leave_bad = [-90.0, 180.0, 0.0, 0.0, 0.0, 0.0]          #odrzucenie

    path1 = move_j(model, wait, pick, path_length=80)
    path2 = move_j(model, pick, wait, path_length=50)
    path3 = move_j(model, wait, to_leave_good, path_length=40)
    path4 = move_j(model, to_leave_good, leave_good, path_length=80)
    path5 = move_j(model, leave_good, to_leave_good, path_length=50)
    path6 = move_j(model, to_leave_good, wait, path_length=40)
    path7 = move_j(model, wait, to_leave_bad, path_length=40)
    path8 = move_j(model, to_leave_bad, leave_bad, path_length=80)
    path9 = move_j(model, leave_bad, to_leave_bad, path_length=50)
    path10 = move_j(model, to_leave_bad, wait, path_length=40)

    print("\n Symulacja robopy")
    print("1. Podniesienie przedmiotu")
    print("2. Odstawienie 1 przedmiotu na paletę")
    print("3. Powrót do pozycji home")
    print("4. Podniesienie przedmiotu")
    print("5. Odstawienie 2 przedmiotu na paletę")
    print("6. Powrót do pozycji home")
    print("7. Podniesienie przedmiotu")
    print("8. Odrzucenie wadliwego produktu")
    print("9. Powrót do pozycji home")
    print("10. Podniesienie przedmiotu")
    print("11. Odstawienie 3 przedmiotu na paletę")
    print("12. Powrót do pozycji home")
    print("13. Podniesienie przedmiotu")
    print("14. Odstawienie 1 przedmiotu na paletę")
    print("15. Powrót do pozycji home")
    print("16. Awaria")

    path = np.concatenate((path1, path2, path3, path4, path5, path6, path1, path2, path3, path4, path5, path6, path1, path2, path7, path8, path9, path10, path1, path2, path3, path4, path5, path6, path1, path2, path3, path4, path5, path6), axis=0)

    model.animate(stances=path, frame_rate=30, unit='deg')


