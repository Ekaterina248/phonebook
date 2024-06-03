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
    f'{name};{surname};{phone};{adress}\n\n'
    f'Выберите вариант: '))

    while var !=1 and var !=2:
        print('Неправильный ввод')
        var=int(input('Введите число '))

    if var==1:
        with open('data_first_variant.csv','a',encoding='utf-8') as f: # файл открываем в режиме 'a'-дописываем файл. Открываем как имя f
            f.write(f'\n{name}\n{surname}\n{phone}\n{adress}\n') # дописываем в файл информацию по варианту1

    elif var==2:
        with open('data_second_variant.csv','a',encoding='utf-8') as f: # файл открываем, как имя f
            f.write(f'{name};{surname};{phone};{adress}\n\n')      # дописываем в файл информацию по варианту2      


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv','r',encoding='utf-8') as f: # файл открываем поменяли на режим 'r'-чтение.
        data_first=f.readlines()        # читаем все наши строки. в переменную data_first
        #print(data_first) # ['name1\n', 'surname\n', 'phone\n', 'adress\n', '\n', 'name2\n', 'surname\n', 'phone\n', 'adress\n', '\n', 'ola\n', 'hj\n', '456\n', 'jhhb\n', '\n', 'lolo\n', 'kl\n', '456\n', 'kloiu\n', '\n']
        
        # ВАРИАНТ НА СЕМИНАРЕ //////////////////////////////////////////////////////////////////////
        # data_first_list=[]              # каждую строку будем добавлять в список
        # j=0
        # for i in range(len(data_first)):
            
        #     if data_first[i]=='\n' or i==len(data_first)-1: # i-тый элемент равен переходу на новую строку или i=последней записи
        #         data_first_list.append(''.join(data_first[j:i+1])) # в список добавляем элемент. Преобразовываем список в строку с помощью функции join
        #         j=i
        #     #print(f'i={i}, data_ferst{i}={data_first[i]}, data_first_list={data_first_list}  ')    
           
        # print(''.join(data_first_list))   
        
        # МОЙ ВАРИАНТ///////////////////////////////////////////////////////////////////////////////////////////////
        # for i in range(len(data_first)):
        #     print(str(data_first[i]), end="")
        print('',*data_first)
            
    
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv','r',encoding='utf-8') as f:
        data_second=f.readlines() 
        print('',*data_second)  
        #print(data_second)# ['name1;surname;phone;adress\n', '\n', 'name2;surname;phone;adress\n', '\n', 'kmmk;mjkm;4568;kli\n', '\n', 'длло;дльол;123456;олдлд\n', '\n', 'орпап;прнку;456987;ррол\n', '\n', 'лолд;длд;длоло;щщот\n']

def change_data():
    var=int(input('Введите номер справочника в которм будем вносить изменеия:'))
    while var !=1 and var !=2:
        print('Неправильный ввод')
        var=int(input('Введите число 1 или 2: '))
    if var==1:
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            data_first=f.readlines()  
            data_first_list=[]              # каждую строку будем добавлять в список
            j=0
            for i in range(1,len(data_first)):
                # if data_first[i]=='\n' or i==len(data_first)-1: # i-тый элемент равен переходу на новую строку или i=последней записи
                #     data_first_list.append(''.join(data_first[j:i])) # в список добавляем элемент. Преобразовываем список в строку с помощью функции join
                #     j=i
                if data_first[i]=='\n':  # i-тый элемент равен переходу на новую строку или i=последней записи
                    data_first_list.append(''.join(data_first[j:i])) # в список добавляем элемент. Преобразовываем список в строку с помощью функции join
                    j=i
                elif i==len(data_first)-1:
                    data_first_list.append(''.join(data_first[j:i+1]))   
                                        
        #print(data_first_list)
        
        num_zap=int(input(f'Всего записей {len(data_first_list)}. Введите номер записи в которой бдут изменения:')) 
        while num_zap>len(data_first_list) or num_zap<1:
            print('Неправильный ввод')
            num_zap=int(input(f'Введите число от 1 до {len(data_first_list)}: '))
        name=name_data()
        surname=surname_data()
        phone=phone_data()
        adress=adress_data()
        new_zap='\n'+name+'\n'+surname+'\n'+phone+'\n'+adress+'\n'
        data_first_list[num_zap-1]=new_zap
        #print(data_first_list)

        with open('data_first_variant.csv','w',encoding='utf-8') as f:
            f.write(''.join(data_first_list))
        
        # with open('data_first_variant.csv','w',encoding='utf-8') as f:               
        #     if num_zap==1:
        #         f.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
        #         f.write(''.join(data_first_list[1:len(data_first_list)]))
        #     else:   
        #         f.write(''.join(data_first_list[0:num_zap-1]))
        #         f.write(f'\n{name}\n{surname}\n{phone}\n{adress}\n')
        #         f.write(''.join(data_first_list[num_zap:len(data_first_list)]))
                
#change_data()

def del_data():
    pass

        
    



