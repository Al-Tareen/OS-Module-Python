import os

	#------Shows all the attributes and methods in the 'os' module------
#print(dir(os))

	#------Shows current working directory------
#print(os.getcwd())

	#------Navigate current working directory------
#os.chdir('C:/Users/user/Desktop/Python/')
#print(os.getcwd())

	#------Listing your Directory------
#print(os.listdir()) #By Default, will list the folders/files in your cwd. You can however, pass a directory you want to see

	#------Creating a folder------
#os.makedir('OS-Demo-2') #Creating a folder
#os.makedirs('OS-Demo-2') #Creating folders layers deep (Tree structure)

	#------Deleting folders------
#os.rmdir('OS-Demo-2/Sub-Dir-1') #Will not remove intermediate directories
#os.removedirs('OS-Demo-2/Sub-Dir-1') #Will remove intermediate directories

	#------Renaming File/Folders------
#os.rename('filename.txt', 'newfilename.txt')

	#------Reading Meta Data from a file------
#print(os.stat('filename.txt')) #Shows file size, timestamp (last modified)
#print(os.stat('filename.txt')).st_mtime #Shows modified time of this file

	#How to make Last Modified human readable?
#from datetime import datetime

#modified_time=os.stat('os-tut.py').st_mtime  #Assign the modified time of your file to modified_time variable
#print(datetime.fromtimestamp(modified_time)) #print the modified_time variable usitilizing the datetime module / .fromtimestamp method

	#------List entire directory Tree------
#os.walk() #A generator that yields a tuple of 3 values as it walks the directory tree

#os.chdir('C:/Users/user/Desktop/')
"""
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()
"""

	#------Access home directory location------
#print(os.environ) #Shows all your environment variables
#print(os.environ.get('HOMEDRIVE')) #Shows pathh of directory

	#------Creating a directory location using your environment variables paths and respective filename------
#filepath = os.path.join(os.environ.get('HOMEDRIVE'), 'test.txt') #Joins an environment path with your desired file name & stores full path in variable (for file creation purposes preventing errors of slashes/ in path)

	#------Find basename of a path------
#print(os.path.basename('/tmp/test.txt')) #Shows basename of your path (basename.extension) e.g. test.txt

	#------Find Directory name of path------
#print(os.path.dirname('/tmp/test.txt')) #shows directory name of your path. e.g. /tmp

	#------Show basename and directory name of your path------
#print(os.path.split('/tmp/test.txt')) #e.g. output: ('/tmp', 'test.txt')

	#------Check if a path exists------
#print(os.path.exists('yourpath')) #Output is either 'True' or 'False'

	#------Check if your path is a directory------
#print(os.path.isdir('yourpath')) #Output is either "True" or "False"

	#------Check if your path is a File------
#print(os.path.isfile('yourpath')) #Output is either "True" or "False"

	#------Splits the file and its extension (easier than parsing out the extension------
#print(os.path.splittext('/tmp/test.txt')) #Output is something like ('/tmp/test', '.txt')

	#------Shows all available methods of the os module------	
#print(dir(os.path))