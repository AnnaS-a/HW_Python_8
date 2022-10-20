from logger import get_columns, read_data, find, add_column, write_data, del_contact
from input_data import input_column, add_contact


def menu():
    data = read_data()
    columns = get_columns(data)
    flag = True
    while flag: 
        print("**СПРАВОЧНИК**\n Выберете действие:")
        while True:
            print("1 - добавить контакт")
            print("2 - просмотреть всю адресную книгу")
            print("3 - найти контакт")
            print("4 - добавить солбец")
            print("5 - удалить контакт")
            print("6 - Выход")
            choice = input()
            if choice not in ["1", "2", "3","4", "5", "6"]:
                print("Выбран неверный пункт меню")
                continue
            if choice == "1": 
                add_contact(data, columns)
                break
            elif choice == "2": 
                print(columns)
                print(data)
                break
            elif choice == "3":
                find(data)
                break
            elif choice == "4":
                column = input_column()
                data = add_column(data, column, columns)
                break
            if choice == "5": 
                del_contact(data, columns)
                break    
            else: 
                flag = False
                write_data(data, columns)
                break
    