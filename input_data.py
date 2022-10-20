from logger import write_contact 

def add_contact(data, columns):
    print("Введите данные контакта: ")
    flag = True
    while flag: 
        user = {}
        for column in columns:
            user[column] = input(column + ": ")
            confirm = input('Введите 1 для сохранения контакта: ')
        if confirm == "1":
            write_contact(user, data)
        flag = False    


def input_column():
    return input('Введите наименование нового столбца: ')


