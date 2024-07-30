from csv import DictWriter, DictReader
from os.path import exists

filename = 'phone.csv'

def get_data():
    first_name = "Иван"
    last_name = "Иванов"
    phone = "+73287282037"
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
    row_number = int(input("Введите номер строки: "))
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
    res = read_file(filename)
    data = get_data()
    res[row_number-1]["Имя"] = data[0]
    res[row_number-1]["Фамилия"] = data[1]
    res[row_number-1]["Телефон"] = data[2]
    standard_write(filename, res)



def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":  # команда выход
            break
        elif command == "w": # команда записи данных или создания файла
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":    # команда считывания и вывода
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(read_file(filename))
        elif command == "f":    # команда поиска по фамилии
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(row_search(filename))
        elif command == "d":    # команда удаления строки по номеру
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            delete_row(filename)
        elif command == "e":    # команда редактирования строки
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            edit_row(filename)


main()