from model import writestring

def create_xls(res):
    res = res.split()
    with open ('NumbersBook.xls','a') as file:
        file.write('{};{}'
                    .format(res[0],res[1]))
        file.write('\n')
        


def deletexls(n):
    f = open('NumbersBook.xls').readlines()
    for j in range(len(f)):
        if f[j].find(n) != -1:
            f.pop(j)
            break
    file = open('NumbersBook.xls','w')
    for i in range(len(f)):
        file.write(f[i])