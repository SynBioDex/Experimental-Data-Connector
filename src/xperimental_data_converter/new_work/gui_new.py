#This file will use Peter's work for dictionary stuff

from openpyxl import load_workbook
from openpyxl import Workbook

from itertools import product

from tkinter import *
from tkinter.ttk import *
from tkinter import Entry, Button, messagebox
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

import ctypes

import os
import string
uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

#dictionary has strain, media, chemical, supplement
input_metadata_test = {
                'media':['lb', 'm9'],
                'strain':['top10', 'dh5a'],
                'supplement':['atc', 'iptg'],
                'vector':['repressilator','toggleswitch'],
                }

#gui work below
root = tk.Tk()

root.iconbitmap('icon.ico')

#setting the taskbar icon NOT FUNCTIONAL YET
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#sets the window icon to 'icon.io' image
p1 = ImageTk.PhotoImage(Image.open('icon.ico'))
root.iconphoto(False, p1)

#labels the GUI
root.title("Welcome to LabGen")
root.geometry("500x500")

hseperator1 = ttk.Separator(root, orient='horizontal')
hseperator1.grid(column=0, row=3, columnspan=5, sticky='ew', pady=10)

hseperator2 = ttk.Separator(root, orient='horizontal')
hseperator2.grid(column=0, row=7, columnspan=5, sticky='ew', pady=10)

vseperator1 = ttk.Separator(root, orient='vertical')
vseperator1.grid(column=2, row=0, rowspan=8, sticky='ns', padx=10)

def show(): 
    label.config(text = media.get())

#List of options for each variable

media_options = input_metadata_test['media']

strain_options = input_metadata_test['strain']

supp_options = input_metadata_test['supplement']

vector_options = input_metadata_test['vector']

#adding an open list to add to later
gui_output = []









#MEDIA SELECTION DROP DOWN
label = Label(root, text = "Select Media(s) from Menu")
label.grid(column =0, row =0, sticky=tk.N+tk.S+tk.W+tk.E)   

media = tk.StringVar(root)

media.set("-Media-")

media_option = tk.OptionMenu(root, media, *media_options) #ENTER a command to reduce the selection process
media_option.grid(column =0, row =1, sticky=tk.N+tk.S+tk.W+tk.E)

#adding selections to a media list to reference later
media_list = set()
max_mediaitems = len(media_options)

def media_dropdown(*args):
    global dropdown
    dropdown = str(media.get())
    print(dropdown)

    if media.get() == media_options[0]:
        media_select = media_options[0]

    if media.get() == media_options[1]:
        media_select = media_options[1]

    if len(media_list) < max_mediaitems:
        media_list.add(media_select)
    else:
        print("Max items reached")

    result_label.config(text=f"{media_list}", fg = "blue")
    result_label.grid(column =0, row=2, sticky=tk.N+tk.S+tk.W+tk.E)

def delete_mediaitems():
    media_select = media.get()
    if media_select in media_list:
        media_list.remove(media_select)
        print(f"Removed {media_select}")
    else:
        print(f"{media_select} not in list")
    
    result_label.config(text=f"{media_list}", fg="blue")
    result_label.grid(column=0, row=2, sticky=tk.N+tk.S+tk.W+tk.E)

#adding the selected media to the open list above
gui_output.append(media_list)

# link function to change dropdown
media_button = Button(root, text = "add", bg='#85e472', fg='black', command = media_dropdown)
media_button.grid(column = 1, row =1, sticky=tk.N+tk.S+tk.W+tk.E )

media_delete = Button(root, text = "delete", bg='#e47272', fg='black', command = delete_mediaitems)
media_delete.grid(column = 1, row =2, sticky=tk.N+tk.S+tk.W+tk.E )








#STRAIN SELECTION DROP DOWN MENU
label = Label(root, text = "Select Strain(s) from Menu")
label.grid(column =3, row =0, sticky=tk.N+tk.S+tk.W+tk.E)

strain = tk.StringVar(root)

strain.set("-Strain-")

strain_option = tk.OptionMenu(root, strain, *strain_options)
strain_option.grid(column =3, row =1, sticky=tk.N+tk.S+tk.W+tk.E)

#adding strain selections to a list to reference later
strain_list = set()
max_strainitems = len(strain_options)

def strain_dropdown(*args):
    global dropdown
    dropdown = str(strain.get())
    print(dropdown)

    if strain.get() == strain_options[0]:
        strain_select = strain_options[0]

    if strain.get() == strain_options[1]:
        strain_select = strain_options[1]

    if len(strain_list) < max_strainitems:
        strain_list.add(strain_select)
    else:
        print("Max items reached")

    sresult_label.config(text=f"{strain_list}", fg = "blue")
    sresult_label.grid(column =3, row=2, sticky=tk.N+tk.S+tk.W+tk.E)

def delete_strainitems():
    strain_select = strain.get()
    if strain_select in strain_list:
        strain_list.remove(strain_select)
        print(f"Removed {strain_select}")
    else:
        print(f"{strain_select} not in list")
    
    sresult_label.config(text=f"{strain_list}", fg = "blue")
    sresult_label.grid(column =3, row=2, sticky=tk.N+tk.S+tk.W+tk.E)
    
gui_output.append(strain_list)

strain_button = Button(root, text = "add", bg='#85e472', fg='black', command = strain_dropdown)
strain_button.grid(column = 4, row =1, sticky=tk.N+tk.S+tk.W+tk.E )

strain_delete = Button(root, text = "delete", bg='#e47272', fg='black', command = delete_strainitems)
strain_delete.grid(column = 4, row =2, sticky=tk.N+tk.S+tk.W+tk.E )








#SUPPLEMENT SELECTION DROP DOWN MENU
label = Label(root, text = "Select Supplement(s) from Menu")
label.grid(column =0, row =4, sticky=tk.N+tk.S+tk.W+tk.E)

supp = tk.StringVar(root)

supp.set("-Supplement-")

supp_option = tk.OptionMenu(root, supp, *supp_options)
supp_option.grid(column =0, row =5, sticky=tk.N+tk.S+tk.W+tk.E)

#Dropdown selection loop to add the selected values to the overall temp list
supp_list = set()
max_suppitems = len(supp_options)

def supp_dropdown(*args):
    global dropdown
    dropdown = str(supp.get())
    print(dropdown)

    if supp.get() == supp_options[0]:
        supp_select = supp_options[0]

    if supp.get() == supp_options[1]:
        supp_select = supp_options[1]

    if len(supp_list) < max_suppitems:
        supp_list.add(supp_select)
    else:
        print("Max items reached")

    suresult_label.config(text=f"{supp_list}", fg = "blue")
    suresult_label.grid(column =0, row=6, sticky=tk.N+tk.S+tk.W+tk.E)

def delete_suppitems():
    supp_select = supp.get()
    if supp_select in supp_list:
        supp_list.remove(supp_select)
        print(f"Removed {supp_select}")
    else:
        print(f"{supp_select} not in list")
    
    suresult_label.config(text=f"{supp_list}", fg = "blue")
    suresult_label.grid(column =0, row=6, sticky=tk.N+tk.S+tk.W+tk.E)

gui_output.append(supp_list)

supp_button = Button(root, text = "add", bg='#85e472', fg='black', command = supp_dropdown)
supp_button.grid(column = 1, row =5, sticky=tk.N+tk.S+tk.W+tk.E )

supp_delete = Button(root, text = "delete", bg='#e47272', fg='black', command = delete_suppitems)
supp_delete.grid(column = 1, row =6, sticky=tk.N+tk.S+tk.W+tk.E )








#VECTOR SELECTION DROP DOWN MENU
#vector list
label = Label(root, text = "Select Vector(s) from Menu")
label.grid(column =3, row =4, sticky=tk.N+tk.S+tk.W+tk.E)

vector = tk.StringVar(root)

vector.set("-Vector-")

vector_option = tk.OptionMenu(root, vector, *vector_options) #ENTER a command to reduce the selection process
vector_option.grid(column =3, row =5, sticky=tk.N+tk.S+tk.W+tk.E)

#adding selections to a media list to reference later
vector_list = set()
max_vectoritems = len(vector_options)

def vector_dropdown(*args):
    global dropdown
    dropdown = str(vector.get())
    print(dropdown)

    if vector.get() == vector_options[0]:
        vector_select = vector_options[0]

    if vector.get() == vector_options[1]:
        vector_select = vector_options[1]

    if len(vector_list) < max_vectoritems:
        vector_list.add(vector_select)
    else:
        print("Max items reached")

    vresult_label.config(text=f"{vector_list}", fg = "blue")
    vresult_label.grid(column =3, row=6, sticky=tk.N+tk.S+tk.W+tk.E)

def delete_vectoritems():
    vector_select = vector.get()
    if vector_select in vector_list:
        vector_list.remove(vector_select)
        print(f"Removed {vector_select}")
    else:
        print(f"{vector_select} not in list")

    vresult_label.config(text=f"{vector_list}", fg = "blue")
    vresult_label.grid(column =3, row=6, sticky=tk.N+tk.S+tk.W+tk.E)


gui_output.append(vector_list)

vector_button = Button(root, text = "add", bg='#85e472', fg='black', command = vector_dropdown)
vector_button.grid(column =4, row =5, sticky=tk.N+tk.S+tk.W+tk.E )

vector_delete = Button(root, text = "delete", bg='#e47272', fg='black', command = delete_vectoritems)
vector_delete.grid(column =4, row =6, sticky=tk.N+tk.S+tk.W+tk.E )




#Temp list button to check if the variables were added correctly
def temp_list1():
    print(gui_output)


temp_listbutton = Button(root, text = "temp list", command = temp_list1)
temp_listbutton.grid(column=0, row=15, sticky=tk.N+tk.S+tk.W+tk.E)
#End

#REPLICATES SLIDER MENU
repliresult_label = tk.Label(root, text = "", fg = "black")
repliresult_label.grid(column =1, row = 15)

label = Label(root, text = "Select Number of Replicates")
label.grid(column =0, row =11, sticky=tk.N+tk.S+tk.W+tk.E)

num_copies = 0
def save_value():
    global num_copies
    slider_value = scale.get()  # Get the slider value
    print(f"Slider value as integer: {slider_value}")
    num_copies += slider_value
    generate(gui_output, num_copies)


scale = tk.Scale(root, from_=1, to=10,tickinterval=1, orient='horizontal')
scale.grid(column =0, row =12, sticky=tk.N+tk.S+tk.W+tk.E)


#Button(root, text='Show', command=show_values).grid(column =0, row =13, sticky=tk.N+tk.S+tk.W+tk.E)
save_button = tk.Button(root, text="Save Value", command=save_value)
save_button.grid(column=0, row=13, sticky=tk.N+tk.S+tk.W+tk.E)

#Below are label placeholders for the visual printing of the list values above
result_label = tk.Label(root, text = "", fg = "black")
result_label.grid(column =1, row =12)

sresult_label = tk.Label(root, text = "", fg = "black")
sresult_label.grid(column =1, row = 13)

suresult_label = tk.Label(root, text = "", fg = "black")
suresult_label.grid(column =1, row = 14)

vresult_label = tk.Label(root, text = "", fg = "black")
suresult_label.grid(column =1, row = 14)

label = tk.Label(root, text = " ")
label.grid()
#End label placeholder code


#Excel sheet opening work
def generate(gui_output, num_copies):
    wb = Workbook()
    sheet = wb.active

    #I don't think this is needed, there is a better way to seperate gui_output into sep lists
    combinations = list(product(*gui_output))

    #Generally below is fine, I'm just struggling with creating a dictionary to reference the values
    for index, combination in enumerate(combinations):
        sheet[uppercase_alphabet[index]+'1'] = (f'{combination}')
        for i in range(num_copies):
            # Modify the row index as needed (e.g., 'A2', 'A3', etc.)
            sheet[uppercase_alphabet[index] + str(i + 2)] = (f'{combination}')
    #PROBLEM CHILD CODE ENDS

    filename = "excel_test_sheet.xlsx"
    try:
        os.remove('./'+ filename)
    except:
        pass

    wb.save(filename = filename)
button = Button(root, text = "Generate", command = lambda: generate(gui_output)).grid()

root.mainloop()