from tkinter import *
from tkinter import filedialog
import pickle
from tkinter import messagebox

def text(root , login_main):
	root.withdraw()

	def exit():
		 root_txt.destroy()
		 root.deiconify()
		 return


	def save_file():
		file_path = filedialog.asksaveasfilename(defaultextension=".txt")
		if file_path:
			with open(file_path, "w") as file:
				file.write(text_fild.get("1.0", "end-1c"))


	def open_file():
		file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
		if file_path:
			with open(file_path, "r") as file:
				text_fild.delete("1.0", "end")
				text_fild.insert("1.0", file.read())
				if a[login_main]['role'] == 'user':
					text_fild.config(state = DISABLED)



	def role_change(login,button ):
		if a[login]['role'] != 'moderator':
			a[login]['role'] = 'moderator'
			role = 'moderator'
		else:
			a[login]['role'] = 'user'
			role = 'user'
		f = open('login_main.txt', 'wb')
		pickle.dump(a, f)
		f.close()

		messagebox.showinfo('Роль изменена' , f"Роль для пользователя {login} была измененена на {role}.")
		button.configure(text = [login , a[login]['role']])
		



	def tk_chan():
		root_chan = Tk()
		root_chan.geometry("300x300")
		root_chan.title('Изменение прав')
		root_chan.configure(bg="#6A5ACD")
		for login in a:
			if a[login]['role'] != 'admin':
				button_mod = Button(root_chan, text=[login, a[login]['role']], command=lambda login=login: role_change(login, button_mod), font=font_style, bg=button_color)
				button_mod.configure(command=lambda login=login, button_mod=button_mod: role_change(login, button_mod),)
				button_mod.pack(pady=5)



	bg_color = "#E6E6FA"
	label_color = "#000000"
	button_color = "#7B68EE"
	font_style = ("Comic Sans MS", 14 )
	root_txt = Tk()
	root_txt.geometry("500x750")
	root_txt.title('Текстовый редактор')
	root_txt.configure(bg="#6A5ACD")

	frame = Frame(root_txt,borderwidth=2, relief="solid")
	text_log = Label(frame, text='WWW', bg="#6A5ACD", fg=label_color, font=font_style)
	f_text = Frame(root_txt, borderwidth=5, relief="solid")
	text_fild = Text (f_text, bg=bg_color, fg=label_color, font=font_style, padx=10, pady=10, width=30, height=14, wrap=WORD)
	button_exit = Button(root_txt, text = 'Вернуться  в меню', command=lambda: exit(), font=font_style, bg=button_color)
	button_open = Button(root_txt, text='Открыть', command=lambda: [text_fild.config(state=NORMAL), open_file()], font=font_style, bg=button_color)
	button_save = Button(root_txt, text='Сохранить', command=save_file, font=font_style, bg=button_color)



	
	frame.pack(pady=10)
	text_log.pack()
	f_text.pack(fill=BOTH, expand = 1)
	text_fild.pack(expand=1, fill = BOTH, side = LEFT)
	button_open.pack(pady=5)

	f = open('login_main.txt', 'rb')
	a = pickle.load(f)
	print(a)
	lenght = len(a)
	f.close()

	if login_main in a:
		if a[login_main]['role'] != 'user':
			button_save.pack(pady=5)
			if a[login_main]['role'] == 'admin':
				button_chan = Button(root_txt, text = 'Изменение прав', command = lambda: tk_chan(), font=font_style, bg=button_color)
				button_chan.pack(pady=5)

	
	button_exit.pack(pady=5)





	          

	root_txt.mainloop()