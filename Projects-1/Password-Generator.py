
from tkinter import * 
from tkinter.ttk import Progressbar
import tkinter
import tkinter.messagebox
import pyperclip
import random,string

no_of_options = 0
length_value = 0

def get_slider_value(value):
    global length_value
    length_value = int(value)
    progress_status()

def progress_status():
    global no_of_options,length_value
    no_of_options = upper_case.get()*5 + small_case.get()*5 + special_Chars.get()*5 + num.get()*5 + length_value*5
    length_progress['value'] = no_of_options
    
def generate_pass():
    global no_of_options,length_value
    password =""
    
    if upper_case.get()==1 and small_case.get()==1 and special_Chars.get()==0 and num.get()==0:
        password = generate1()
        
    if upper_case.get()==1 and small_case.get()==1 and special_Chars.get()==0 and num.get()==1:
        password = generate2()
        
    if upper_case.get()==0 and small_case.get()==0 and special_Chars.get()==0 and num.get()==1:
        password = generate3()
        
    if upper_case.get()==1 and small_case.get()==1 and special_Chars.get()==1 and num.get()==1:
        password = generate4()
        
    if upper_case.get()==0 and small_case.get()==1 and special_Chars.get()==0 and num.get()==0:
        password = generate5()
        
    if upper_case.get()==1 and small_case.get()==0 and special_Chars.get()==0 and num.get()==0:
        password = generate6()
        
    if upper_case.get()==0 and small_case.get()==0 and special_Chars.get()==1 and num.get()==0:
        password = generate7()
        
    if upper_case.get()==1 and small_case.get()==0 and special_Chars.get()==0 and num.get()==1:
        password = generate8()
        
    if upper_case.get()==0 and small_case.get()==1 and special_Chars.get()==0 and num.get()==1:
        password = generate9()
        
    if upper_case.get()==1 and small_case.get()==0 and special_Chars.get()==1 and num.get()==0:
        password = generate10()
        
    if upper_case.get()==0 and small_case.get()==1 and special_Chars.get()==1 and num.get()==0:
        password = generate11()
        
    if upper_case.get()==1 and small_case.get()==1 and special_Chars.get()==1 and num.get()==0:
        password = generate12()
        
    if upper_case.get()==0 and small_case.get()==0 and special_Chars.get()==1 and num.get()==1:
        password = generate13()
        
    if upper_case.get()==0 and small_case.get()==1 and special_Chars.get()==1 and num.get()==1:
        password = generate14()
        
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    

def generate1():  
    "Upper Smaller"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate2():
    "Upper smaller number"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','0','1','2','3','4', '5', '6', '7', '8', '9']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate3():
    "Number"
    try:
        n=int(length_value)
        password=""
        listpass=['0','1','2','3','4', '5', '6', '7', '8', '9']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate4():
    "Upper smaller number special"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','0','1','2','3','4', '5', '6', '7', '8', '9','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate5():
    "Smaller"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate6():
    "Upper"
    try:
        n=int(length_value)
        password=""
        listpass=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate7():
    "Special"
    try:
        n=int(length_value)
        password=""
        listpass=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate8():
    "Upper number"
    try:
        n=int(length_value)
        password=""
        listpass=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','0','1','2','3','4', '5', '6', '7', '8', '9']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate9():
    "Smaller Number"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4', '5', '6', '7', '8', '9']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate10():
    "Upper Special"
    try:
        n=int(length_value)
        password=""
        listpass=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','0','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate11():
    "Smaller Special"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate12():
    "Smaller Upper Special"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate13():
    "Number Spceial"
    try:
        n=int(length_value)
        password=""
        listpass=['0','1','2','3','4', '5', '6', '7', '8', '9','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
def generate14():
    "Smaller Number Special"
    try:
        n=int(length_value)
        password=""
        listpass=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4', '5', '6', '7', '8', '9','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
        for i in range(0,n):
            password+=random.choice(listpass)
        return password
    except:
        return  "Invalid length_value"
    
def copyclip():
    passwordcopy=password_entry["text"]
    pyperclip.copy(passwordcopy)

root = Tk()
root.title("TryCatch Password Generator")
root.geometry("700x300")

title = Label(root, text="TryCatch-Password Generator",
               fg="Blue", font=("Arial", 15, 'bold')).place(x=200, y=10)

num = IntVar()
small_case = IntVar()
upper_case = IntVar()
special_Chars = IntVar()
length = IntVar()
password_str =StringVar()

#Checkboxes
C1 = Checkbutton(root,text = "A-Z",variable = upper_case,onvalue=1,offvalue=0,command=progress_status)
C1.place(x=100,y=40)
C2 = Checkbutton(root,text = "a-z",variable = small_case,onvalue=1,offvalue=0,command=progress_status)
C2.place(x=180,y=40)
C3 = Checkbutton(root,text = "0-9",variable = num,onvalue=1,offvalue=0,command=progress_status)
C3.place(x=250,y=40)
C4 = Checkbutton(root,text = "special characters",variable = special_Chars,onvalue=1,offvalue=0,command=progress_status)
C4.place(x=320,y=40)

#Length scale
s1 = Scale( root, variable = length,  
           from_ = 1, to = 16,  
           orient = HORIZONTAL,command=get_slider_value
           ) 
s1.place(x=550,y=40)
scale_lable = Label(root, text="Length",
                    font=("Arial", 11)).place(x=500, y=40)

strength_lable = Label(root, text="Password Strength",
                    font=("Arial", 12,"bold")).place(x=280, y=80)

# Progressbar to show strength
length_progress = Progressbar(root, orient = HORIZONTAL, 
              length = 400, mode = 'determinate' )
length_progress.place(x=150,y=120)

btn = Button(master=root, text="calculate",fg="green",
                font=("Arial", 10, 'bold') ,command=generate_pass).place(x=300,y=150)


password_entry = Entry(root,width=30)
password_entry.place(x=220, y=200)

copy_btn = Button(master=root, text="Copy",fg="green",
                font=("Arial", 10, 'bold') ,command=copyclip).place(x=320,y=230)


root.mainloop()
print(length_value)