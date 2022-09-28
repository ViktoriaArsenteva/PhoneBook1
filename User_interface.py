


def actions():
    print('Выберите необходимую позицию из списка ')
    print('1. Добавить номер')
    print('2. Удалить номер')
    print('3. Найти данные по ФИО')
    print('4. Найти данные по номеру телефона')
    print('5. Вывести весь справочник')


def action_choice():
    num = int(input('Введите номер действия: '))
    return num

def add_number():
    name = input('Введите ФИО: ')
    number = input('Введите номер телефона: ')
    return name,number

def deletedata():
    data = input('Введите номер или ФИО человека, данные которого нужно удалить: ')
    return data

def number_empty():
    num = input('Введите номер: ')
    return num

def name_empty():
    name = input('Введите имя: ')
    return name

def printtxt():
    f = open('NumbersBook.txt').readlines()
    for i in range(len(f)):
        print(f[i])

def find(num):
    f = open('NumbersBook.txt').readlines()
    for j in range(len(f)):
        if f[j].find(num) != -1:
            print(f[j])

def output_selection():
    print('Выберите способ сортировки:')
    print('1. По алфавиту(А - Я)')
    print('2. По алфавиту(Я - А)')
    print('3. По новизне (сначала новые)')
    print('4. По новизне (сначала старые)')




