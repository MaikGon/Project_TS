# Projekt na zajęcia z Teorii Sterowania w Robotyce.

### Opis zaprojektowanego systemu

Projekt obejmuje stanowisko zrobotyzowane, w którym robot umieszcza produkty w opakowaniu lub odrzuca produkty uszkodzone. Produkty, podjeżdżając na taśmie, podegają kontroli. Jeżeli wiązka światła nie będzie docierać do czujnika przez okres dłuższy niż określony, produkt zostanie uznany za wadliwy (AWARIA).

Kolejny produkt pojawia się dopiero po obsłużeniu poprzedniego. Produkty wykonane prawidłowo umieszczane są do opakowań zbiorczych. Każde opakowanie mieści trzy produkty, na trzech kolejnych miejscach. 
Po zapełnieniu jednego opakowania, na jego miejsce wstawiane jest kolejne, puste. 

![alt text](/images/graf-1.jpg?raw=true)


W przypadku wystąpienia awarii, wykonywany jest sekwencja obsługująca tę awarię. Po udanym naprawieniu usterki, maszyna wraca do pracy. 

![alt text](/images/graf_nadrzędny.jpg?raw=true)


### Użycie 
Po uruchomieniu 'main.py', w pierwszej kolejności pojawia się możliwość sprawdzenia najkrótszej ścieżki pomiędzy konkretnymi stanami głównej maszyny stanów. 
Następnie uruchamiana jest przykładowa sekwencja. Jest ona prezentowana na odpowiednich grafach, po czym wyświetlana zostaje symulacja robota wykonującego tę sekwencję. 



