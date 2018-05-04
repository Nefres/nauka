import random
# pobieraod uzytkownika dane
ileliczb  = int(input('podaj ilosc typowanych liczb: '))
maxliczba = int(input('podaj maksymalna losowana liczbe: '))

# wypisuje zmienne podane przez uzytkownika
print('wytypuj %s z %s liczb: ' % (ileliczb, maxliczba))

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maxliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

print('wylosowane liczby to: ', liczby)
