from fileinput import close
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
            print('Данные удалены:',f[j])
            f.pop(j)
            break
    file = open('NumbersBook.txt','w')
    for i in range(len(f)):
        file.write(f[i])