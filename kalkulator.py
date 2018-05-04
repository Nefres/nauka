def dodawanie (x, y):
    return x + y
def odejmowanie (x, y):
    return x - y
def mnozenie (x, y):
    return x * y
def dzielenie (x, y):
    return x / y

print('co chcesz zrobic')
print('1 - dodawanie')
print('2 - odejmowanie')
print('3 - mnozenie')
print('4 - dzielenie')
print()

choice = input('wybieraj ')

num1 = float(input('pierwsza liczba: '))
num2 = float(input('druga liczba: '))

if choice == '1':
    print(dodawanie(num1, num2))
if choice == '2':
    print(odejmowanie(num1, num2))
if choice == '3':
    print(mnozenie(num1, num2))
if choice == '1':
    print(dzielenie(num1, num2))
