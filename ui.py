from logger import *

def interfase():
    print('Добрый день! Вы попали на специальный бот справочник. \n 1 - запись данных \n 2 - вывод данных')
    command=int(input())

    while command !=1 and command !=2:
        print('Неправильный ввод')
        command=int(input('Введите число '))
    
    if command ==1:
        input_data()
    elif command ==2:
        print_data()    

       