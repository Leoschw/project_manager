from tkinter import *
from tkinter import scrolledtext
import re


'''
Defining variables
'''
global projects_txt_file
projects_txt_file = open(r'C:\Users\leosc\PycharmProjects\Project_Manager\Projects.txt', 'a+')
global proj_name
'''
Functions for adding projects

DELETE STILL DOESN'T WORK WITH THE LIST REGEX WITH ANCHOR PROBABLY DOESNT WORK?
'''
def delete_project():
    with open(r'C:\Users\leosc\PycharmProjects\Project_Manager\Projects.txt', 'a+') as foo:
        for project in foo:
            if not re.match(ANCHOR, project):
                foo.write(project)
    lb_prov.delete(ANCHOR)

def refresh(): # Function to refresh Listbox
    global projects_txt_file
    lb_prov.insert(END, proj_name.get())
    projects_txt_file.write(proj_name.get() + '\n')
    add_w.destroy()


def add_proj(): #Funtion to add project
    global proj_name
    global add_w
        # need to make it global otherwise the refresh function would not get the
        # given name for the new project
    add_w = Tk()
    add_w.geometry('300x70')
    add_w.title('Add Project')
    proj_name_label = Label(add_w, text = 'Project name and number: ')
    proj_name = Entry(add_w)
    proj_name_label.grid(column = 1, row = 2)
    proj_name.grid(column = 2, row = 2)
    b_accept = Button(add_w, text = 'Ok', command = refresh)
    b_cancel = Button(add_w, text = 'Cancel', command = add_w.destroy)
    b_accept.grid(column = 1, row = 3, columnspan = 2, pady = 8)
    b_cancel.grid(column = 1, row = 3, pady = 8)


'''
Window, button and frame creation
'''

# Creates main Window
main = Tk()                                 # Creates actual window
main.title('Project Manager')               # Gives window the title
main.geometry('1000x600')                   # To define initial size of window

lb_prov = Listbox(main)                     # Need to use the Label function instead of Frame one
lb_prov['width'] = 30                     #  because Frame doesn't work somehow!?
lb_prov['height'] = 35                    # Why is Width and height so different from geometry?
lb_prov['relief'] = 'groove'
with open(r'C:\Users\leosc\PycharmProjects\Project_Manager\Projects.txt', 'r') as \
        already_projects: # = projects_txt_file.read()
    for project in already_projects:
      lb_prov.insert(END, project)



l_tasks = Label(main)
l_tasks['width'] = 108                     #  because Frame doesn't work somehow!?
l_tasks['height'] = 27                    # Why is Width and height so different from geometry?
l_tasks['relief'] = 'groove'

l_info = scrolledtext.ScrolledText(main)
l_info['width'] = 93                     #  because Frame doesn't work somehow!?
l_info['height'] = 9                    # Why is Width and height so different from geometry?
l_info['relief'] = 'groove'

b_add_proj = Button(main, text = 'Add project', command = add_proj)          # Grid works with
# columns,
# yet it only makes
b_sub_proj = Button(main, text='Delete project', command = lambda: delete_project())
#
# decisions
                                                #  about possition in window, not size of e.g. Fram


'''
Gridding and geometrical organization
'''
lb_prov.grid(column = 1, row = 2, padx = 5, columnspan = 2)
b_add_proj.grid(column = 1, row = 1, pady = 5, padx = 5, sticky = W)    # Sticky here glues button
#  on left
                                                                # side of the window -
                                                                #  W, E, S, N are possible options
b_sub_proj.grid(column = 2, row = 1, sticky = E, pady = 5, padx = 5)
l_tasks.grid(column = 3, row = 2, padx = 5, sticky = N)
l_info.grid(column = 3, row = 2, padx = 5, sticky = S)



# Creates Menu Bar
mbar = Menu(main)                           #
mfile = Menu(mbar)                          #
mfile.add_command(label = 'Neu')            #
mfile.add_command(label = 'Laden')          #


# Adds menu bar to main window
main['menu'] = mbar

#Add Menu to Menuframe

mbar.add_cascade(label = 'Datei', menu = mfile)



#Infinityloop
main.mainloop()


