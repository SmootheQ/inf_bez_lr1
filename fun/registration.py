from tkinter import *
from tkinter import messagebox, ttk
import pickle
import uuid
import re


def registration (root):
     root.withdraw()

     root_reg = Tk()
     root_reg.geometry("450x520")
     root_reg.title('Регистрация')
     bg_color = "#6A5ACD"
     label_color = "#000000"
     button_color = "#7B68EE"
     font_style = ("Comic Sans MS", 14)
     font_style_bold = ("Comic Sans MS", 14, 'bold')
     font_style2 = ("Comic Sans MS", 10)
     root_reg.configure(bg=bg_color)
     frame = Frame(root_reg ,borderwidth=3, relief="solid")
     frame.pack(pady=10)


     text = Label (frame, text = 'Для входа в систему - зарегестрируйтесь', bg=bg_color, fg=label_color, font=font_style_bold)
     text_name = Label(root_reg,text = 'Введите Ваше имя', bg=bg_color, fg=label_color, font=font_style)
     registr_name = Entry(root_reg, font=font_style2)
     text_number = Label(root_reg, text = 'Введите Ваш номер', bg=bg_color, fg=label_color, font=font_style)
     registr_number = Entry(root_reg, font=font_style2)
     text_address = Label(root_reg, text = 'Введите Ваш адрес', bg=bg_color, fg=label_color, font=font_style)
     registr_address = Entry(root_reg, font=font_style2)
     registr_log = Label(root_reg, text = 'Введите Ваш логин(эд.адрес)', bg=bg_color, fg=label_color, font=font_style) 
     registr_login = Entry(root_reg, font=font_style2 )
     text_password_1 = Label(root_reg, text = "Введите Ваш пароль", bg=bg_color, fg=label_color, font=font_style)
     registr_password_1 = Entry(root_reg, font=font_style2 )
     text_password_2 = Label(root_reg, text = "Повторите Ваш пароль", bg=bg_color, fg=label_color, font=font_style)
     registr_password_2 = Entry(root_reg, show ='*', font=font_style2)
     reg_uuid = uuid.getnode()
     button_registr = Button(root_reg, text = 'Зарегестрироваться', command=lambda: save(), font=font_style, bg=button_color)
     button_exit = Button(root_reg, text = 'Вернуться в меню', command=lambda: exit(), font=font_style, bg=button_color)

     text.pack()


     text_name.pack()
     registr_name.pack()

     text_number.pack()
     registr_number.pack()

     text_address.pack()
     registr_address.pack()

     registr_log.pack()     
     registr_login.pack()

     text_password_1.pack()
     registr_password_1.pack()
     
     text_password_2.pack()
     registr_password_2.pack()
     button_registr.pack(pady=15)
     button_exit.pack()
     




     def check_uuid_exists(uuid):
          try:
               with open('login_main.txt', 'rb') as f:
                    login_pass_save = pickle.load(f)
                    if uuid in login_pass_save.values():
                         return True
          except FileNotFoundError: 
               return False
          return False

     def generate_unique_uuid():
          while True:
               new_uuid = uuid.uuid4()
               if not check_uuid_exists(new_uuid):
                    return new_uuid


     def validate_email(email):
          pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
          if re.match(pattern, email):
               return True
          else:
               return False

     def exit():
          root_reg.destroy()
          root.deiconify()
          return

     def save():
          with open('login_main.txt', 'rb') as f:
               try:
                    existing_data = pickle.load(f)
               except EOFError:
                    existing_data = {}

          if registr_name.get() == '':
               messagebox.showerror("Ошибка", "Введите имя", parent=root_reg)
               return
          if registr_number.get() == '':
               messagebox.showerror("Ошибка", "Введите номер телефона", parent=root_reg)
               return
          if not registr_number.get().isdigit():
               messagebox.showerror("Ошибка", "Проверьте корректность номера телефона", parent=root_reg)
               return
          if registr_address.get() == '':
               messagebox.showerror("Ошибка", "Введите адрес", parent=root_reg)
               return
          if registr_login.get() == '':
               messagebox.showerror("Ошибка", "Введите логин", parent=root_reg)
               return
          if registr_password_1.get() == '':
               messagebox.showerror("Ошибка", "Введите пароль", parent=root_reg)
               return
          if registr_password_2.get() == '':
               messagebox.showerror("Ошибка", "Введите пароль еще раз", parent=root_reg)
               return
          if registr_password_2.get() != registr_password_1.get():
               messagebox.showerror("Ошибка", "Пароли не совпадают", parent=root_reg)
               return

          password = registr_password_1.get()
          if len(password) < 6:
               messagebox.showerror("Ошибка", "Пароль должен содержать минимум 6 символов", parent=root_reg)
               return
          if sum(1 for c in password if c.isupper()) < 1:
               messagebox.showerror("Ошибка", "Пароль должен содержать заглавную букву", parent=root_reg)
               return
          if sum(1 for c in password if c.islower()) < 1:
               messagebox.showerror("Ошибка", "Пароль должен содержать строчную букву", parent=root_reg)
               return


          reg_uuid = generate_unique_uuid()
          #print (reg_uuid)



          if not validate_email (registr_login.get()):
               messagebox.showerror("Ошибка","Логин введен некорректно", parent=root_reg)
               return

          if registr_login.get() in existing_data:
               messagebox.showerror("Ошибка", "Логин уже занят", parent=root_reg)
               return
          else:
               login_pass_save = existing_data
               login_pass_save[registr_login.get()] = {'password': registr_password_1.get(),'name': registr_name.get(), 'uuid' : reg_uuid, 'number' : registr_number.get() , 'address': registr_address.get()}
               #print (login_pass_save)
               f = open('login_main.txt', 'wb')
               pickle.dump(login_pass_save, f)
               f.close()
               with open('login_main.txt', 'r', encoding='latin-1') as file:
                    content = file.read()
                    #print(content)

               messagebox.showinfo('Поздравляем!', 'Регистрация Успешна')

               root_reg.destroy()
               root.deiconify()
               



     root_reg.mainloop()