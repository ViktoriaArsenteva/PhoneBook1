
from model import writestring

def createhtml(result):
    style = 'style="font-size:20px;"'
    html = '<html>\n <head>'
    html += '<meta charset = "utf-8">'
    html += '    <p {}>  {} </p>\n'\
        .format(style,result)
    html += '</body\n</html>'

    with open('NumbersBook.html','a') as file:
        file.write(html)

    return html

def deletehtml(n):
    f = open('NumbersBook.html').readlines()
    for j in range(len(f)):
        if f[j].find(n) != -1:
            f.pop(j)
            break
    file = open('NumbersBook.html','w')
    for i in range(len(f)):
        file.write(f[i])



