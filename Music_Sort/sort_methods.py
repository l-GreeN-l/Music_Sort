import os
import shutil
from  itertools import groupby
from collections import OrderedDict

from methods import get_files


path = 'D:\Downloads\Music_VK'
dictination = 'D:\Downloads'


def get_group(filename):
    buf = os.path.basename(filename).split(' - ')
    return buf[0].upper()



def sort_in_folders(path):
    os.chdir(path)

    files = get_files()



    add_names = []
    buffer = []
    catalog = []
    folder = []



    for sel_file in files:
        sel_group = get_group(sel_file.name)
        # print(sel_group)
        # Есть ли группа уже в сортированных
        #  Удалять файлы из files во время прохода мы не можем - нарушит итерацию
        if sel_group in add_names:
            continue
        else:
            #  Идем по списку и ищем файлы с похожими муз группами
            for file in files:
                if file.name == sel_file.name:
                    continue
                group = get_group(file.name)
                if sel_group == group:
                    # Проверка - если наша папка пустая , то добавить туда и файл селектор
                    if len(folder) ==0:
                        folder.append(sel_file.name)
                        add_names.append(sel_group)
                    # Добавление сравниваемого файла
                    folder.append(file.name)

                pass
            # Если ничего не нашли похожего - в буффер , для записи в основной каталог без папки
            if len(folder) ==0:
                buffer.append(sel_file.name)

                pass
            else:
                # Если папку сформировали - добавить в каталог и очистить  папку
                # print('I create folder:', folder)
                catalog.append(folder)
                folder = []
                pass

            pass

    # Добавляем в каталог файлы без папок ????? надо делать слияние
    catalog.extend(buffer)

    # print('add names: ', add_names)
    # print('buffer: ', buffer)
    # print('len catalog: ', len(catalog))
    print('Catalog building !')



    return catalog




def create_folder(name):
    try:
        os.mkdir(name)



    except FileExistsError as erF:
        print('Директория уже есть')
    pass





#  Перемещение файлов и создание каталога
def transfer(catalog, dist):

    catalog_name = 'Sorted_music'
    if len(catalog) !=0:
        os.chdir(dist)

        create_folder(catalog_name)
        os.chdir(catalog_name)
        koren = os.getcwd()

        for elem in catalog:
            if type(elem) == type([]):
                print("------>\n")
                create_folder(get_group(elem[0]))
                os.chdir(get_group(elem[0]))

                for item in elem:
                    print('\t', item)
                    print(os.getcwd())
                    shutil.move(item, os.getcwd())

                    pass
                os.chdir(koren)
            else:
                print(elem)
                shutil.move(elem, os.getcwd())



    #     for file in delFiles:
    #         shutil.move(file, distination_del + os.path.basename(file))
    #         pass
    #
    #     for file in vishFiles:
    #         shutil.move(file, distination_vish + os.path.basename(file))
    #         pass
    #
    # pass










catalog  = sort_in_folders(path)
transfer(catalog, dictination)



# for elem in catalog:
#     if type(elem) == type([]):
#         print("------>\n")
#
#         for item in elem:
#             print('\t',item)
#     else:
#         print(elem)










