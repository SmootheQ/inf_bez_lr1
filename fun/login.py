from tkinter import *
from tkinter import messagebox
import pickle

def login():
    bg_color = "#6A5ACD"
    label_color = "#000000"
    button_color = "#7B68EE"
    font_style = ("Comic Sans MS", 14 )
    font_style2 = ("Comic Sans MS", 10)
    frame = Frame(borderwidth=2, relief="solid")
    frame.pack(pady=10)



    text_log = Label(frame , text='WWW', bg=bg_color, fg=label_color, font=font_style)
    text_enter_login = Label(text='Введите логин', bg=bg_color, fg=label_color, font=font_style)
    enter_login = Entry(font=font_style2)
    text_enter_password = Label(text='Введите пароль', bg=bg_color, fg=label_color, font=font_style)
    enter_password = Entry(show='*' , font=font_style2)
    button_enter = Button(text='Войти', command=lambda: log_password(), bg=button_color, font=font_style)

    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack(pady=10)


    def log_password():
        f = open('login_main.txt', 'rb')
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]['password']:
                messagebox.showinfo('Привет!', 'Автоизация успешна!')
            else:
                messagebox.showerror("Ошибка!", "Неверный логин или пароль")
        else:
            messagebox.showerror('Ошибка!', 'Удостоверьтесь в правильности логина')