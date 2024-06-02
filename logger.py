from data_create import *
#from data_create import name_data, surname_data, phone_data, adress_data

def input_data():
    name=name_data()
    surname=surname_data()
    phone=phone_data()
    adress=adress_data()
    var=int(input(f'В каком формате записать данные\n\n'
    f'1 Вариант: \n'
    f'{name}\n{surname}\n{phone}\n{adress}\n\n'
    f'2 Вариант:\n'
    f'{name};{surname};{phone};{adress}\n'
    f'Выберите вариант: '))

    while var !=1 and var !=2:
        print('Неправильный ввод')
        var=int(input('Введите число '))

    if var==1:
        with open('data_first_variant.csv','a',encoding='utf-8') as f: # файл открываем в режиме 'a'-дописываем файл. Открываем как имя f
            f.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')

    elif var==2:
        with open('data_second_variant.csv','a',encoding='utf-8') as f: # файл открываем, как имя f
            f.write(f'{name};{surname};{phone};{adress}\n')            


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv','r',encoding='utf-8') as f: # файл открываем поменяли на режим 'r'-чтение.
        data_first=f.readlines()        # читаем все наши строки. в переменную data_first
        #print(data_first) # ['name1\n', 'surname\n', 'phone\n', 'adress\n', '\n', 'name2\n', 'surname\n', 'phone\n', 'adress\n', '\n', 'ola\n', 'hj\n', '456\n', 'jhhb\n', '\n', 'lolo\n', 'kl\n', '456\n', 'kloiu\n', '\n']
        
        data_first_list=[]              # каждую строку будем добавлять в список
        j=0
        for i in range(len(data_first)):
            if data_first[i]=='\n' or i==len(data_first)-1: # i-тый элемент равен переходу на новую строку или i=последней записи
                data_first_list.append(''.join(data_first[j:i+1])) # в список добавляем элемент. Преобразовываем список в строку с помощью функции join
                j=i
        print(''.join(data_first_list))   
            
    
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv','r',encoding='utf-8') as f:
        data_second=f.readlines() 
        print(*data_second)

        
    



