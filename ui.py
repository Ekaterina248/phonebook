from logger import *

def interfase():
    print(f'Добрый день! Вы попали на специальный бот справочник.'
          f'\n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных')
    command=int(input('Введите номер от 1 до 4: '))

    while command !=1 and command !=2 and command!=3 and command !=4:
        print('Неправильный ввод')
        command=int(input('Введите число от 1 до 4: '))
    
    if command ==1:
        input_data()
    elif command ==2:
        print_data()   
    elif command ==3:
        change_data()   
    elif command ==4:
        del_data()        


       