from os.path import exists

def write_contact(user, data):
    data.append(user)


def write_data(data, columns):
    with open(FILE_NAME, "w", encoding="UTF-8") as f:
        f.write(', '.join(columns) + '\n')
        for user in data:
            f.write(', '.join(user.values()) + '\n')


def add_column(data, column, columns):
    for user in data:
        user[column] = ""
    columns.append(column)    
    return data    

def read_data():
    valid = exists(FILE_NAME)
    if not valid:
        return []
    with open(FILE_NAME, "r+", encoding="UTF-8") as f: 
        data = f.read()
        if len(data.split()) < 2:
            return[]          #если файл пустой(данных нет), возвращается пустой список
        columns = data[0].strip().split(", ")                 # строка с заголовками(столбцы), стрип убирает пустые символы
        data = [{columns[i]: user.strip().split(", ")[i] for i in range(len(columns))} for user in data.split()[1:]] 
                                        #user это одна строка(фамилия имя и тд), делаем из этого cписок словарей 
        return data


def get_columns(data):
    if not data:
        return ['Фамилия', 'Имя']
    columns = data[0].keys()    
    return columns


def find(data):
    column = input('Введите столбец поиска: ')
    val = input('Введите значение для поиска: ')
    flag = False   #ущу никого не нашли
    for user in data:
        if column not in user:
            return 'Такого столбца нет'
        if user[column] == val:
            print(user)
            flag = True #нашли
    if not flag:
        print('Такого контакта нет')     

def del_contact(data, column):
    column = input('Введите столбец поиска: ')
    val = input('Введите данные контакта: ')
    flag = False
    for user in data:
        if column not in user:
            return 'Такого столбца нет'
        if user[column] == val:
            confirm = input('Введите 2 для удаления контакта: ')
            if confirm == "2":
                data.remove(user)
                flag = True            
    if not flag:
        print('Такого контакта нет')

       
FILE_NAME = "inform_log.csv" 



