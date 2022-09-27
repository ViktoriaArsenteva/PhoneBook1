from model import writestring

def createtxt(res):
    with open('NumbersBook.txt','a') as file:
        file.write(res)
        file.write('\n')

    return file

def deletetxt(n):
    f = open('NumbersBook.txt').readlines()
    for j in range(len(f)):
        if f[j].find(n) != -1:
            print('Данные', f[j], 'удалены')
            f.pop(j)
            break