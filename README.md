#Project_TS

Projekt na zajęcia z Teorii Sterowania w Robotyce.

Projekt obejmuje stanowisko zrobotyzowane, w którym robot umieszcza produkty w opakowaniu lub odrzuca produkty uszkodzone. Produkty ułożone są na poruszającej się taśmie. Kolejne produkty pojawiają się na taśmie dopiero w momencie ukończenia poprzedniego działania przez robota i powrót do pozycji home. Oceny uszkodzenia produktu dokonuje czujnik optyczny, który składa się z nadajnika i odbiornika. Dodatkowo odmierzany jest czas przerwania wiązki światła. W sytuacji, gdy czas ten jest dłuższy niż średni czas przejazdu produktu na taśmie, stanowisko wchodzi w tryb awarii i wymagana jest reakcja człowieka. Zbyt długie przerwanie wiązki może oznaczać uszkodzenie czujnika lub przejazd dwóch produktów zaraz po sobie. Obie te sytuacje wymagają kontroli człowieka. W jednym opakowaniu można umieścić 3 produkty. Po zapełnieniu opakowania jest ono zabierane i w jego miejsce podstawiane jest nowe, puste opakowanie. 

Po uruchomieniu skryptu "StateMachine + NetworkX.py" najpierw wyświetlany jest graf stanów dla zaplanowanej przez nas sekwencji zdarzeń. Następnie uruchamiana jest wizualizacja robota wykonującego zadania odpowiadające wcześniejszej sekwencji.

![alt text](https://github.com/MaikGon/Project_TS/blob/renovation/images/graf-1.jpg?raw=true)

![alt text](https://github.com/MaikGon/Project_TS/blob/renovation/images/graf_nadrzędny.jpg?raw=true)
