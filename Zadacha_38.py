# Задача 38: Дополнить телефонный справочник возможностью изменения 
# и удаления данных. Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи 
# (например имя или фамилию)
# 4. Использование функций. Ваша програма не должна быть линейной.


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу\n")
    choice = int (input())
    return choice

def Work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')

    while(choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print (find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print (find_by_number(phone_book, number))        
        elif choice == 4:
            user_data = get_new_user()
            add_user ((phone_book, user_data))
        elif choice == 5:
            File_name = get_file_name()
            write_txt (File_name, phone_book)
        choice = show_menu


def read_txt (filename):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open (filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
    return data
        

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)
    print(data)

def Write_txt(filename: str, data: list):
   with open(filename, "w", encoding="utf-8") as fout:
       for i in range(len(data)):
           s = ''
           for v in data[i].values():
               s += v + ','
           fout.write(f'{s[:-1]}\n')   



def find_by_name(data: list, name):
    for j in data:
        if j.get("фамилия") == name:
            return j.get ("Телефон")
        else :
            return ("нет такого значения")
        
def find_by_number(data: list, number):
    for j in data:
        if j.get("фамилия") == number:
            return j.get ("Телефон")
        else :
            return ("нет такого значения")


Work_with_phonebook()