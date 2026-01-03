import os
from sys import int_info
import tkinter
import customtkinter as custtk
import calendar
import datetime
from calendar import *
from datetime import date
import calendar
from datetime import datetime
from datetime import timedelta
import tkinter.font as tkFont
from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkComboBox

# Define a folder to store files
storage_dir = os.path.join(os.getcwd(), "data")

# Ensure the folder exists
if not os.path.exists(storage_dir):
    os.makedirs(storage_dir)


## def the time variables fun for copying and pasting
def TimeVariables():
    date1 = date.today()
    x = monthrange(date1.year, date1.month)
    input_dt = datetime.today()
    res = input_dt.replace(day=1)
    date2 = res.date()
    List1 = [
        'Sunday', 'Monday', 'Tuesday', "Wedsnesday", "Thursday", 'Friday',
        'Saturday'
    ]
    o = calendar.day_name[date2.weekday()]
    y = x[1]


## Defines all the variables although some of these seem unimportant they all are
global date1, x, input_dt, res, date2, list1, o, y, finalnote, noteslist, list1bil, title
date1 = date.today()
x = monthrange(date1.year, date1.month)
input_dt = datetime.today()
res = input_dt.replace(day=1)
date2 = res.date()
List1 = [
    'Sunday', 'Monday', 'Tuesday', "Wedsnesday", "Thursday", 'Friday',
    'Saturday'
]
o = calendar.day_name[date2.weekday()]
y = x[1]
title = ''
finalnote = ''
noteslist = {}
list1bil = []

storage_dir = os.path.join(os.getcwd(), "data")

# Ensure the folder exists
if not os.path.exists(storage_dir):
    os.makedirs(storage_dir)

## you need to define all these
##j1 = 0j2 = 0j3 = 0j4 = 0j5 = 0j6 = 0j7 = 0j8 = 0j9 = 0j10 = 0j11 = 0j12 = 0j13 = 0j14 = 0j15 = 0j16 = 0j17 = 0j18 = 0j19 = 0j20 = 0j21 = 0j22 = 0j23 = 0j24 = 0j25 = 0j26 = 0j27 = 0j28 = 0j29 = 0j30 = 0j31 = 0j32 = 0
for i in range(33):
    i2 = ((i) + 1)
    j0 = (f'j{i}')
    exec(j0 + " = 0 ")

## end
##  sets the color mode of the system and creates root which is what the entire program is inside
choice = 'Dark'
custtk.set_appearance_mode(choice)
ColorsBase = ['-Select-', "Dark", "Light", 'System']
custtk.set_default_color_theme('green')
root = custtk.CTk()
## sets the size of the application
root.geometry('821x700')
root.title('Calendar')
root.resizable(False, False)

## defining of all the functions for the calendarpiece buttons
def fj1():
    notes(1)
def fj2():
    notes(2)
def fj3():
    notes(3)
def fj4():
    notes(4)

def fj5():
    notes(5)

def fj6():
    notes(6)

def fj7():
    notes(7)

def fj8():
    notes(8)

def fj9():
    notes(9)

def fj10():
    notes(10)

def fj11():
    notes(11)

def fj12():
    notes(12)

def fj13():
    notes(13)

def fj14():
    notes(14)

def fj15():
    notes(15)

def fj16():
    notes(16)

def fj17():
    notes(17)

def fj18():
    notes(18)

def fj19():
    notes(19)

def fj20():
    notes(20)

def fj21():
    notes(21)

def fj22():
    notes(22)

def fj23():
    notes(23)

def fj24():
    notes(24)

def fj25():
    notes(25)

def fj26():
    notes(26)

def fj27():
    notes(27)

def fj28():
    notes(28)

def fj29():
    notes(29)

def fj30():
    notes(30)

def fj31():
    notes(31)

def fj32():
    notes(32)

def clearframe():
    for Item in frame.winfo_children():
        Item.destroy()
        ## Is a for loop for the amount of items in frame and destroys them


def deletea():
    Text1.delete(0.0, 'end')
    ## Deletes all the text in Text1 this needs to be a function because buttons must have a function in there command area and not a line of code


def copytea():
    global thing
    thing = Text1.get(0.0, 'end')
    ## Makes thing the variable everything in Text1 with the .get function


def copytea2():
    global finalnote
    finalnote = Text1.get(0.0, 'end')
    ## same thing but used on a different button to save the text so it has to use a different variable


def pastetea():
    Text1.insert(0.0, thing)
    ## Pastes everything in the variable thing into Text1

def notes(xxx):
    clearframe()
    global Text1, title

    title = f'{date1.year}, {date1.month}, {xxx}'
    file_path = os.path.join(storage_dir, f"{title}.txt")
    try:
        with open(file_path, 'x') as file:
                file.write("")
    except FileExistsError:
        pass

    with open(file_path, 'r') as file:
            s = file.read()
    file.close()

    Text1 = custtk.CTkTextbox(master=frame, height=500, width=600)
    Text1.insert(0.0, s)
    Text1.pack(pady=20, padx=20)

    frame8989 = CTkFrame(master=frame)
    frame8989.pack(pady=20)
    delbutton = CTkButton(master=frame8989,
                              text='Delete All',
                              command=deletea)
    delbutton.grid(row=0, column=0)
    copbutton = CTkButton(master=frame8989,
                              text='Copy All',
                              command=copytea)
    copbutton.grid(row=0, column=1)
    pasbutton = CTkButton(master=frame8989, text='Paste', command=pastetea)
    pasbutton.grid(row=0, column=2)
    Backbuttonnotes = CTkButton(master=frame8989,
                                    text='Save&Back',
                                    command=savenote)
    Backbuttonnotes.grid(row=1, column=1)


## all the functions for the top buttons back1 and back2 go back an amount of months and Forward1 and Forward2 are the same thing but forward
def Back1Fun():
    clearframe()
    global date1, input_dt
    ## this sets date1 to be date1 - the amount of days in day one which is y
    date1 = date1 - timedelta(days=y)
    input_dt = input_dt - timedelta(days=y)
    ## same thing for input_dt but its used elsware for the
    CalnderPart()


def Back2Fun():
    clearframe()
    global date1, input_dt, y
    date1 = date1 - timedelta(days=y)
    input_dt = input_dt - timedelta(days=y)
    res = input_dt.replace(day=1)
    o = calendar.day_name[date2.weekday()]
    y = x[1]
    date1 = date1 - timedelta(days=y)
    input_dt = input_dt - timedelta(days=y)
    CalnderPart()


def Forward1Fun():
    clearframe()
    global date1, input_dt
    date1 = date1 + timedelta(days=y)
    input_dt = input_dt + timedelta(days=y)
    CalnderPart()


def Forward2Fun():
    clearframe()
    global date1, input_dt, y
    date1 = date1 + timedelta(days=y)
    input_dt = input_dt + timedelta(days=y)
    res = input_dt.replace(day=1)
    o = calendar.day_name[date2.weekday()]
    y = x[1]
    date1 = date1 + timedelta(days=y)
    input_dt = input_dt + timedelta(days=y)
    CalnderPart()


def savenote():
    finalnote = Text1.get(0.0, 'end')
    file_path = os.path.join(storage_dir, f"{title}.txt")
    with open(file_path, 'w') as file:
        file.write(finalnote)
    CalnderPart()


def CalnderPart():
    ## set z , p and Editbutton to global variables
    global z, p, Editbutton
    ## Defines  all the neccessary variables
    x = monthrange(date1.year, date1.month)
    res = input_dt.replace(day=1)
    date2 = res.date()
    List1 = [
        'Sunday', 'Monday', 'Tuesday', "Wedsnesday", "Thursday", 'Friday',
        'Saturday'
    ]
    o = calendar.day_name[date2.weekday()]
    y = x[1]
    list1bil = []
    q = 1
    listfin = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
    ]
    ## end
    z = 0
    p = 2
    clearframe()
    ## creates the seven days of the weak as text labels above the calendar
    for loop4 in range(7):
        Frame4321 = CTkFrame(master=frame, width=100, height=20)
        Frame4321.grid(row=1, column=loop4)
        yapsesh = CTkLabel(master=Frame4321, text=List1[loop4])
        yapsesh.grid(row=1, column=loop4)
    ## more setting of time variables
    date43 = date1 - timedelta(days=y)
    B11 = date43.month
    B12 = calendar.month_name[B11]
    B13 = date43.year
    ## makes a button thats text is B12 and B13 which is one month before the current month the calendars on
    Back1 = CTkButton(master=frame,
                      command=Back1Fun,
                      width=100,
                      height=20,
                      text=f'{B12}{B13}',font= ("Arial",10))
    Back1.grid(row=0, column=2)

    y2 = monthrange(date43.year, date43.month)
    date44 = date43 - timedelta(days=y2[1])
    B24 = date44.month
    B21 = calendar.month_name[B24]
    y2 = monthrange(date44.year, date44.month)
    B22 = date44.year
    ## makes a button thats text is b21 and b22 which is 2 months before the current month
    Back2 = CTkButton(master=frame,
                      command=Back2Fun,
                      width=100,
                      height=20,
                      text=f'{B21}{B22}',font= ("Arial",10))
    Back2.grid(row=0, column=0)

    currentd = CTkLabel(master=frame,
                        width=100,
                        height=20,
                        text=f'{calendar.month_name[date2.month]}{date2.year}',
                        bg_color='#2b2b2b',
                        fg_color='#2b2b2b')
    currentd.grid(row=0, column=3)

    date46 = date1 + timedelta(days=y)
    f11 = date46.month
    f12 = calendar.month_name[f11]
    f13 = date46.year
    ## same things as the other but instead 1 month ahead
    Forward1 = CTkButton(master=frame,
                         command=Forward1Fun,
                         width=100,
                         height=20,
                         text=f'{f12}{f13}',font= ("Arial",10))
    Forward1.grid(row=0, column=4)
    y3 = monthrange(date46.year, date46.month)
    date45 = date46 + timedelta(days=y3[1])
    f24 = date45.month
    f21 = calendar.month_name[f24]
    f22 = date45.year
    ##same thing as the other but instead two months ahead
    Forward2 = CTkButton(master=frame,
                         command=Forward2Fun,
                         width=100,
                         height=20,
                         text=f'{f21}{f22}',font= ("Arial",10))
    Forward2.grid(row=0, column=6)
    ## these if statements dictate where the month starts so that it doesn't start on a sunday when it should really be Tuesday
    if o == 'Sunday':
        z = 0
        i = 0
    elif o == 'Monday':
        z = 1
        i = 1
    elif o == 'Tuesday':
        z = 2
        i = 2
    elif o == 'Wednesday':
        z = 3
        i = 3
    elif o == 'Thursday':
        z = 4
        i = 4
    elif o == 'Friday':
        z = 5
        i = 5
    elif o == 'Saturday':
        z = 6
        i = 6
    for loop1 in range(y):
        ## these if statements change which row the calandarpiece buttons are on so that it looks like a calendar
        if i == 7:
            p = 3
            z = 0
        elif i == 14:
            p = 4
            z = 0
        elif i == 21:
            p = 5
            z = 0
        elif i == 28:
            p = 6
            z = 0
        elif i == 35:
            p = 7
            z = 0
        if loop1 == 0:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj1)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 1:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj2)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')

        if loop1 == 2:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj3)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 3:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj4)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 4:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj5)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 5:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj6)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 6:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj7)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 7:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj8)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 8:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj9)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 9:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj10)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 10:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj11)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 11:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj12)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 12:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj13)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 13:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj14)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 14:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj15)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 15:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj16)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 16:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj17)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 17:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj18)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 18:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj19)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 19:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj20)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 20:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj21)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 21:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj22)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 22:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj23)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 23:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj24)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 24:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj25)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 25:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj26)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 26:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj27)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 27:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj28)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 28:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj29)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 29:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj30)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 30:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj31)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
        if loop1 == 31:
            Calendarpiece = CTkFrame(master=frame,
                                     width=100,
                                     height=100,
                                     bg_color='#2b2b2b',
                                     fg_color='#2b2b2b')
            Calendarpiece.grid(row=p, column=z)
            Editbutton = custtk.CTkButton(master=frame,
                                          width=98,
                                          height=98,
                                          text=loop1 + 1,
                                          bg_color='#2b2b2b',
                                          fg_color='#141414',
                                          command=fj32)
            Editbutton.grid(row=p, column=z)
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-0{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-0{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
            if f'{date.today()}' == f'{date1.year}-{date1.month}-{loop1 + 1}':
                Calendarpiece.configure(fg_color='#42ff75')
                ## this if statement sets the button to have green border if the buttons date is todays date
        z = z + 1
        i = i + 1
    ReturnMMBut = CTkButton(master=frame,
                            command=ReturnMMFS,
                            text="Back",
                            width=100)
    ReturnMMBut.grid(row=7, column=6)
    settingsbutton = CTkButton(master=frame,
                               command=Settings2,
                               text='Settings',
                               width=100)
    settingsbutton.grid(row=7, column=5)


## the def settings function it loads up the settings menu and clears the frame. within the settings menu is a mode color pick which sets the color to Light Dark or system
def Settings():
    clearframe()
    TfCmode = CTkLabel(master=frame, text="Choose System your color mode")
    TfCmode.pack(padx='20')
    Color = CTkComboBox(master=frame, values=ColorsBase, command=ColorPick)
    Color.pack(padx='20', pady='20')
    ReturnMMBut = CTkButton(master=frame, command=ReturnMMFS, text="Back")
    ReturnMMBut.pack()


## Same thing as settings however this time the funcion for the back button has to be set to a different function
def Settings2():
    clearframe()
    TfCmode = CTkLabel(master=frame, text="Choose System your color mode")
    TfCmode.pack(padx='20')
    Color = CTkComboBox(master=frame, values=ColorsBase, command=ColorPick)
    Color.pack(padx='20', pady='20')
    ReturnMMBut = CTkButton(master=frame, command=CalnderPart, text="Back")
    ReturnMMBut.pack()


## this just sets the system color theme to whatever choice they make with the drop down bar in settings.
def ColorPick(choice):
    custtk.set_appearance_mode(choice)


## login menu
def login():
    global setting
    ## entry1 is what you put in the username box and entry 2 is the password if they are wrong it goes to else if its correct it loads up the main menu
    if entry1.get() == '1' and entry2.get() == '2':
        clearframe()
        CalenderBut = CTkButton(master=frame,
                                command=CalnderPart,
                                text="Calender")
        CalenderBut.pack(padx=20, pady=40)
        setting = CTkButton(master=frame, command=Settings, text="Settings")
        setting.pack(padx=20, pady=40)
    else:
        ## if you use the wrong username and password this pops up a messagebox
        tkinter.messagebox.showerror(title="Failed Login",
                                     message="Invlad Username or Password")


def ReturnMMFS():
    clearframe()
    CalenderBut = CTkButton(master=frame, command=CalnderPart, text="Calender")
    CalenderBut.pack(padx=20, pady=40)
    setting = CTkButton(master=frame, command=Settings, text="Settings")
    setting.pack(padx=20, pady=40)


## return button for the settings and calendar menu ^^^^^^^^^^^^^^^^

## creates all the buttons and textboxes for the logiin menu
frame = custtk.CTkFrame(master=root)
frame.pack(pady='20', padx='60', fill='both', expand=True)
label = custtk.CTkLabel(master=frame, text="Login system")
label.pack(pady="12", padx="10")
entry1 = custtk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady="12", padx="10")
entry2 = custtk.CTkEntry(master=frame, placeholder_text="Password", show='*')
entry2.pack(pady="12", padx="10")
button = custtk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady='12', padx='10')
root.mainloop()
