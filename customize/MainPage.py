from tkinter import *
from tkinter import ttk
from tkinter import colorchooser 
from customize_functions import add_navbar_tofile
class MainPage:
	
	def __init__(self, projectpath):
		self.root  = Tk()
		self.projectpath = projectpath
		self.components = ["Navbar", "Image"]
		self.component_choice  = StringVar()
		self.component_choice.set("Navbar")
		
		self.initialize_components()
		self.pack_components()
			

	def initialize_components(self):
		
		self.workplace = ttk.Notebook(self.root)
		self.workplace.pack(pady = 15)

		self.home_page = Frame(self.workplace, width = 800, height = 500, bg = "white")
		self.new_frame = Frame(self.workplace, width = 800, height = 500)

		self.add_component_button = OptionMenu(self.home_page,  self.component_choice , *self.components, command = self.add_component)
		self.add_component_button.config(bg = "white",  relief = "flat")

	def pack_components(self):
		self.home_page.pack(fill = 'both', expand = 1)
		self.new_frame.pack(fill = 'both', expand = 1)

		self.workplace.add(self.home_page, text = "Home")
		self.workplace.add(self.new_frame, text = "New")
		
		self.add_component_button.pack(anchor = NW)

		self.root.geometry('800x500')
		self.root.mainloop()

	def add_component(self, selected):
		if(selected=='Navbar'):
			self.add_navbar()

	def add_navbar(self):
		self.navbar_frame = Frame(self.home_page, bg = "skyblue")
		self.navbar_text = Entry(self.navbar_frame, width = 50)
		self.navbar_text.insert(0, "Enter comma separated Navigation bar button")
		self.set_color_navbar = Button(self.navbar_frame, text = "Background-Color", command = self.pick_color_navbar)
		self.render_navbar = Button(self.navbar_frame, text = "Render", command = self.update_navbar)
		
		self.navbar_text.pack(pady = 10, side = LEFT, padx = 10)
		self.set_color_navbar.pack(side = LEFT, padx = 10)
		self.render_navbar.pack(side = LEFT, padx = 10)
		self.navbar_frame.pack(fill = 'both')
		
		

	def pick_color_navbar(self):
		self.p_c_chooser = colorchooser.askcolor(title = "select a color")
		self.navbar_frame.config(bg = self.p_c_chooser[1])

	def update_navbar(self):
		navtext =  self.navbar_text.get()
		navtext = navtext.split(',')
		add_navbar_tofile(self.projectpath, navtext, self.p_c_chooser[1])		
		

myclass = MainPage("E:\\Projects\\dummyproject")







