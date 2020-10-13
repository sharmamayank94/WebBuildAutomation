import tkinter as tk
from tkinter import filedialog
from make import makebackend


def createproject():
	project_path = filedialog.askdirectory(title = "myproject")
	print(project_path)
	makebackend(project_path)

window = tk.Tk()

window['bg'] = 'white'

newproject_label = tk.Button(window, text =  "+", fg = 'gray', font="Verdana 50 bold", 
	relief = 'flat', command = createproject)

newproject_label.pack(padx = (10), pady = 20, anchor = tk.NW)
window.geometry("600x400")
window.mainloop()