import os
import subprocess

def add_navbar_tofile(projectpath, options, color):
	filecontent = []
	with open(os.path.join(projectpath, 'views', 'home.ejs')) as f:
		
		for line in f.readlines():
			filecontent.append(line)
			if line.strip() == '<body>':
				filecontent.append("\t\t"+ r"<%-include('partials/navbar.ejs')%>" + "\n")

	with open(os.path.join(projectpath, 'views', 'home.ejs'), 'w') as f:
		
		for line in filecontent:
			f.write(line)
			
				
			
			

	with open(os.path.join(projectpath,'views', 'partials', 'navbar.ejs'), 'w+') as f:
		f.write("<div>")
		for option in options:
			f.write("<a href = '#'>" + option + "</a>")

		f.write("</div>")