
import model
import User_interface
import html_creater
import txt_creater
import xls_creater


def button_click():
    User_interface.actions()
    number = User_interface.action_choice()
    if number == 1:
        name, num = User_interface.add_number()
        res = model.writestring(name,num)
        html_creater.createhtml(res)
        txt_creater.createtxt(res)
        xls_creater.create_xls(res)
    elif number == 2:
        data = User_interface.deletedata()
        txt_creater.deletetxt(data)
        xls_creater.deletexls(data)
        html_creater.deletehtml(data)
    elif number == 3:
        nam = User_interface.name_empty()
        User_interface.find(nam)
    elif number == 4:
        n = User_interface.number_empty()
        User_interface.find(n)
    elif number == 5:
        User_interface.printtxt()



