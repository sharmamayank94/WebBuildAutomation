import os
import subprocess
import time

def makebackend(projectpath):

	staticpath = projectpath.replace('/', '\\') + '\\static'
	viewspath =  projectpath.replace('/', '\\') +'\\views'
	#subprocess.run(["mkdir", projectpath], shell = True)
	subprocess.run(['npm', 'init', '-y'], shell = True)
	subprocess.run(['move', 'package.json', projectpath], shell = True)


	subprocess.run([ 'npm', 'install', 'express'], shell = True)
	subprocess.run([ 'npm', 'install', 'ejs'], shell = True)
	
	subprocess.run(['move', 'node_modules', projectpath], shell = True)
	subprocess.run(['mkdir', staticpath], shell = True)
	subprocess.run(['mkdir', viewspath ], shell = True)
	subprocess.run(['mkdir', viewspath+"\\partials" ], shell = True)
	subprocess.run(['copy', 'home.ejs', viewspath], shell = True)
	print(staticpath)
	print(viewspath)
	basefile = ""
	with open("backendreference.js") as f:
	    basefile = f.read()

	with open(os.path.join(projectpath, 'app.js'), 'w+') as f:
	    f.write(basefile)



	#subprocess.run(['node', os.path.join(projectpath, 'app.js')])