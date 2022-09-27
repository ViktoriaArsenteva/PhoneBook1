from model import writestring

def createhtml(result):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}>  {} </p>\n'\
        .format(style,result)
    html += '</body\n</html>'

    with open('NumbersBook.html','a') as file:
        file.write(html)

    return html



