#-----------------------------------------------------------------------------------------------------------------------
#
#           Набор методов для проверки каталога музыки на левые файлы по названиям
#               get_catalogs() - возвращает список полных имен папок в каталоге
#               get_files() - возвращает список полных имен файлов в каталоге
#               check() - проверка есть ли в списке файлы на удаление
#                   выдает 2 списка полных имен файлов в одном словаре
#                   vishlist - то с чем сравнивал
#                   dellist - список кандидатов на удаление
#               move - создает папки vishlist и dellist в директории и распихивает туда файлы кандидатов
#
#           Запуск:
#                   через  logic(<путь до папки с музыкой>)
#                По каталогам бродит с помощью рекурсии logic() 
#                И с помощью терминала через os.chdir(path)
#
# ----------------------------------------------------------------------------------------------------------------------

import os
import shutil


# Получить список папок
def get_catalogs(path):
    cataloglist = []
    for elem in os.listdir(path):
        if os.path.isfile(elem):
            continue
        else:
            cataloglist.append(path+'\\'+elem)
    return cataloglist

 # Получить список файлов
def get_files():
    path = os.getcwd()
    filelist = []
    for filename in os.listdir(path):
        if os.path.isfile(filename):
            try:
                file = open(path +'\\'+ filename)
                # print(os.path.basename(file.name))
                filelist.append(file)

            except PermissionError as ex:
                print(ex)
        # else:
        #     print('Это не файл')
    try:
        assert filelist != [], 'Нет файлов'
    except AssertionError as ass:
        print()
        # print(ass)
    return filelist

# Проверить - есть ли в каталоге файлы на удаление
def check(filelist):
    delist = []
    vishlist = []

    for sort_file in filelist:
        sort_file_name = os.path.basename(sort_file.name).split('.mp3')[0]
        tr = False
        for file in filelist:
            # if sort_file != file:
            file_name = os.path.basename(file.name).split('.')[0]
            if sort_file_name != file_name:
                if sort_file_name in file_name:
                    print('1- ', file_name)
                    print('2- ', sort_file_name)
                    tr = True
                    delist.append(file.name)
                    
        if tr : vishlist.append(sort_file.name)  
    print(delist)
    print(vishlist)
    for file in filelist:
        file.close()
    return [delist, vishlist]

#  Перемещение файлов в каталог на удаление
def move(path, list):
    delFiles = list[0]
    vishFiles = list[1]

    if len(delFiles) != 0:
        distination_del = path + '\Del_List\\'
        distination_vish = path + '\Vish_List\\'
        try:
            os.mkdir(distination_del)
            
        except FileExistsError as erF:
            print('DEL директория уже есть')

        try:

            os.mkdir(distination_vish)
        except FileExistsError as erF:
            print('VISH директория уже есть')
        # print(path)
        # print(distination)
        for file in delFiles:
            shutil.move(file, distination_del + os.path.basename(file))
            
        for file in vishFiles:
            shutil.move(file, distination_vish + os.path.basename(file))
            
# Логика проверки музыки на похожие файлы
def logic(path):
    
    print('Я нашел в ', path, ' папки :', get_catalogs(os.getcwd()))
    for elem in get_catalogs(os.getcwd()):
        if elem == 'Del_List':
            continue
        if elem == 'Vish_List':
            continue
        else:
            print('-->', elem)
            os.chdir(elem)
            logic(elem)
            os.chdir(path)
        
    print('Выполнил логику  - ', os.getcwd())
    move(os.getcwd(),check(get_files()))
 
