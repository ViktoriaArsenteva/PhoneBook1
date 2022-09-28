
def writestring(name,number):
    result = name +' '+ number
    return result

def txtsort (num):
    file = open('NumbersBook.txt').readlines()
    if num == 1:
        file.sort()
        for i in range(len(file)):
            print(file[i])
    elif num == 2:
        file.sort()
        file.reverse()
        for i in range(len(file)):
            print(file[i])
    elif num == 3:
        file.reverse()
        for i in range(len(file)):
            print(file[i])
    elif num == 4:
        for i in range(len(file)):
            print(file[i])




