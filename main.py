from transport import Client
from transport import Vehicle
from transport import Train, Airplane, TransportCompany

"""def sec_menu():
    pass

def menu(data, num_op): #функция "меню"
    print("1 - Работа с клиентами\n2 - Работа с транспортом\n3 - Работа с транспортной компанией\n4 - Выход из программы\n")
    c = int(input("Выберите действие(введите число): ")) #запрашивает действие пользователя в переменную
    
    if c == 1: #выводит все записи
        display_all_records(data)

    elif c == 2:#выводит поле записи, id которой ввел пользователь
        display_one_record(data)
    
    elif c == 3: #ввод всех данных, запись их в множество и добавление множество в data
        new_record(data)
        
    elif c == 4: #находится id в файле, после чего запись с нужным id удаляется
        delete_record(data)
    
    elif c == 5: #завершается цикл
        closing_prog(data, num_op)
        
    else: #при вводе некорректного значения
        print('Введите корректное значение')

def main(): #главная функция #открывается файл json и записывается в data
    while True: #цикл повторяется постоянно
        menu() #запускается функция "меню"""


A = Client.Client("Aiaia", 95, False)
B = Vehicle.Vehicle(35)
C = TransportCompany.TransportCompany("Akkki")
C.add_vehicle(B)
C.add_client(A)

D = Train.Train(123, 45)

C.add_vehicle(D)


C.optimize_cargo_distribution()

#B.load_cargo(A)
#print(B.__str__(), D.__str__())

#for i in C.list_vehicles():
#    print(i)'''