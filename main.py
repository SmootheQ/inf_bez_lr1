from tkinter import *
from tkinter import messagebox
from fun.registration import registration 
from fun.login import login
import pickle
import uuid
import sys
import os

root = Tk()
root.geometry("300x300")
root.title('Войти в систему')


bg_color = "#6A5ACD"
label_color = "#483D8B"
button_color = "#7B68EE"
font_style = ("Comic Sans MS", 14)

root.configure(bg=bg_color)

def compare_uuids():
    filename = 'uuid.txt'
    if os.path.getsize(filename) == 0:
        with open(filename, 'wb') as file:
            user_uuid = str(uuid.getnode())
            pickle.dump(user_uuid, file)
            uuid_main = user_uuid
    else:
        with open(filename, 'rb') as file:
            try:
                uuid_main = pickle.load(file)
            except (pickle.UnpicklingError, EOFError):
                user_uuid = uuid.getnode()
                file.seek(0)
                pickle.dump(user_uuid, file)
                uuid_main = user_uuid


    f = open('uuid.txt', 'wb')
    pickle.dump(uuid_main, f)
    f.close()

    uuid_1 = str(uuid.getnode())
    #uuid_1 = str(uuid.uuid4())
    #print(uuid_1 , uuid_main)

    if uuid_1 != uuid_main:
        print (uuid)
        messagebox.showerror('Ошибка','Ваш UUID не соответсвет стандартному, убедитесь, что устройство является основным и повторите попытку.')
        sys.exit()


compare_uuids()
login()


button_frame = Frame(bg=bg_color)
button_frame.pack(pady=0)


button_registr = Button(button_frame, text='Зарегистрироваться', command=lambda: registration(), font=font_style, bg=button_color)
button_registr.pack()

root.mainloop()