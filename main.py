from tkinter import *
from tkinter import messagebox
from fun.registration import registration 
from fun.login import login
import pickle
import uuid
import sys
import os
import subprocess

root = Tk()
root.geometry("300x300")
root.title('Войти в систему')


bg_color = "#6A5ACD"
label_color = "#483D8B"
button_color = "#7B68EE"
font_style = ("Comic Sans MS", 14)

root.configure(bg=bg_color)



def compare_uuids(filename):
    
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            user_uuid = str(subprocess.run('wmic csproduct get UUID/value', capture_output=True, text=True))
            file.write(user_uuid)
            uuid_main = user_uuid
    else:
        with open(filename, 'r') as file:
            uuid_main = file.read().strip()
    uuid_1 = str(subprocess.run('wmic csproduct get UUID/value',capture_output=True, text=True))
    #print(uuid_1 , uuid_main)


    if uuid_1 != uuid_main:
        messagebox.showerror('Ошибка', 'Ваш UUID не соответствует стандартному, убедитесь, что устройство зарегестрированно и повторите попытку.')
        sys.exit()



compare_uuids('uuid.txt')
login(root)


button_frame = Frame(bg=bg_color)
button_frame.pack(pady=0)



button_registr = Button(button_frame, text='Зарегистрироваться', command=lambda: registration(root) ,font=font_style, bg=button_color)
button_registr.pack()


root.mainloop()