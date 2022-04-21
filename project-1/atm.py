from sys import exit

clients = {"Петър" : [100.10, 1111], 
          "Георги": [200.33, 2222],
          "Васил" : [300, 3333],
          "Калоян" : [400, 4444],
          "Трендафил" : [500, 5555] }




def get_pin():
    i = 0
    while i <= 3:
        pin = input("Моля въведете пин:")
        if pin == str(clients[name][1]):
            break
        else:
            print("Wrong pin")
        i+=1
        if i == 3:
            print("Card is blocked")
            exit()

def withdraw():
    i = 1
    while i <= 3:
        amount = input("Въведете сума за теглене:")

        try:
            amount = float(amount)
        except ValueError:
            print("Не сте въвели валидна сума!")
            exit()

        if amount > clients[name][0]:
            print("Няма достатъчна наличност!")
            i+=1
        else:
            clients[name][0] = clients[name][0] - amount
            print(f'Наличност: {clients[name][0]:.2f}')
            exit()
        
def deposit():
    amount = input("Въведете сума за внасяне:")
    try:
        amount = float(amount)
    except ValueError:
        print("Не сте въвели валидна сума!")
        exit()
    
    clients[name][0] = clients[name][0] + amount
    print(f'Наличност: {clients[name][0]:.2f}')
    exit()



name = input("Моля въведете име:")

if name not in clients:
    print("Name is unknown")
    exit()

get_pin()

print(f'Наличност {clients[name][0]:.2f}')
action = input("За теглене въведете Т, за Внасяне въведете В, за Баланс въведете Б:")

if action == 'Б':
    print(f'Наличност {clients[name][0]:.2f}')
    exit()
elif action == 'Т':
    withdraw()
elif action == 'В':
    deposit()
else:
    print("Невалидна операция!")
    exit()

