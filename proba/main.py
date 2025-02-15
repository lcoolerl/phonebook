from csv import DictWriter, DictReader
from os.path import exists

filename = 'phone.csv'
newfile = 'new_phone.csv'

class NameError (Exception):
    def __init__(self, txt):
        self.txt = txt

def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя :")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию :")
            if len(last_name) < 2:
                raise NameError("Слишком короткая фамилия")
            phone = input("Введите номер : +7")
            if len(phone) < 10:
                raise NameError("Введен короткий номер")
        except NameError as err:
            print(err)
        else:
            flag = True
    # first_name = "Иван"
    # last_name = "Иванов"
    # phone = "+73287282037"
    return [first_name, last_name, phone]


def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    standard_write(filename, res)


def row_search(filename):
    last_name = input("Введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return "Запись не найдена"


def delete_row(filename):
    res = read_file(filename)
    res.pop(row_number-1)
    standard_write(filename, res)


def standard_write(filename, res):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def edit_row(filename):
    row_number = int(input("Введите номер строки: "))
    
    data = get_data()
    res[row_number-1]["Имя"] = data[0]
    res[row_number-1]["Фамилия"] = data[1]
    res[row_number-1]["Телефон"] = data[2]
    standard_write(filename, res)

def copy_to_new_file(filename, newfile):
    if not exists(newfile):
        create_file(newfile)
    row_number = int(input("Введите номер строки: "))
    res1 = read_file(filename)
    res2 = read_file(newfile)
    # obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res2.append(res1[row_number-1])
    standard_write(newfile, res2)

# def exam_file(filename): # функция проверки существования файла
#     if not exists(filename):
#         print("Файл не существует. Создайте его.321")
#         return (continue)

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":  # команда выход
            break
        elif command == "w": # команда записи данных или создания файла
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":    # команда считывания и вывода файла
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            out_d = read_file(filename)
            for row in out_d:
                print ("Имя :",row['Имя']," ","Фамилия :",row['Фамилия']," ","Телефон :",row['Телефон'])
        elif command == "f":    # команда поиска по фамилии
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(row_search(filename))
        elif command == "d":    # команда удаления строки с №
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            delete_row(filename)
        elif command == "e":    # команда редактирования строки с №
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            edit_row(filename)
        elif command == "c":    # команда копирования строки в новый справочник
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            copy_to_new_file(filename, newfile)


main()