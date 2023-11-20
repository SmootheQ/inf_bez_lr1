from tkinter import *
from tkinter import messagebox
import pickle
import hashlib
import time
from fun.text import text

def login(root):
    bg_color = "#6A5ACD"
    label_color = "#000000"
    button_color = "#7B68EE"
    font_style = ("Comic Sans MS", 14 )
    font_style2 = ("Comic Sans MS", 10)
    frame = Frame(borderwidth=2, relief="solid")
    frame.pack(pady=10)
    global attempts
    attempts = 0
    LOCKOUT_TIME = 5 





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


    def generate_challenge():
    	challenge = "random_challenge"
    	return challenge
    
    def generate_response(challenge, password):
    	response = hashlib.sha256((password ).encode()).hexdigest() + hashlib.sha256((challenge ).encode()).hexdigest()
    	print(password , challenge)
    	return response

    def start_timer():
    	global locked
    	locked = True
    	root.after(LOCKOUT_TIME * 1000, unlock)  # Разблокировка через LOCKOUT_TIME секунд


    def unlock():
    	global locked, attempts
    	locked = False
    	button_enter.config(state='normal')
    	messagebox.showinfo("Разблокировка", "Теперь вы можете ввести пароль")
    	attempts = 0





    def log_password():
        f = open('login_main.txt', 'rb')
        a = pickle.load(f)
        f.close()
        global locked , attempts
        MAX_ATTEMPTS = 3  # Максимальное количество попыток ввода пароля
        locked = False  # Флаг блокировки
        challenge = generate_challenge()
        response = generate_response(challenge, enter_password.get())
        #print("Ответ:", response)
        #print(a[enter_login.get()]['password'] + hashlib.sha256(( challenge).encode()).hexdigest())
        if enter_login.get() in a:
            if response == a[enter_login.get()]['password'] + hashlib.sha256(( challenge).encode()).hexdigest():
                messagebox.showinfo('Привет!', 'Автоизация успешна!')
                text(root , enter_login.get())
                attempts = 0
            else:
            	messagebox.showerror("Ошибка!", "Неверный логин или пароль")
            	attempts+=1
            	print(attempts)
            	if attempts >= MAX_ATTEMPTS:
            		locked = True
            		attempts = 10
            		messagebox.showerror("Ошибка!", f"Превышено количество попыток. Попробуйте снова через {LOCKOUT_TIME} секунд")
            		start_timer()
            		button_enter.config(state='disabled')  
        else:
            messagebox.showerror('Ошибка!', 'Удостоверьтесь в правильности логина')
            attempts+=1
            print(attempts)
            if attempts >= MAX_ATTEMPTS:
            		locked = True
            		attempts = 10
            		messagebox.showerror("Ошибка!", f"Превышено количество попыток. Попробуйте снова через {LOCKOUT_TIME} секунд")
            		start_timer()
            		button_enter.config(state='disabled')