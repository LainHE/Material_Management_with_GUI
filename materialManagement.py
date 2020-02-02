# coding=utf-8

#LainHE

from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox

# import heartrate; heartrate.trace(browser=True)

db = Database('list.db')


def fillList():
    lb.delete(0, END)
    for row in db.fetch():
        lb.insert(END, row)


def comboboxSelect(event):
    tText.get()


def insertMaterial():
    if nText.get() == '' or aText.get() == '' or pText.get() == '' or dpText.get() == '':
        messagebox.showerror("Error!", "Please fill all boxes!")
        return

    db.insert(nText.get(), aText.get(), pText.get(), dpText.get(), tText.get())
#    lb.delete(0, END)
#    lb.insert(END, (nText.get(), aText.get(), pText.get(), dpText.get(), tText.get()))
    clearInput()
    fillList()


def selectMaterial(event):
    global selectedMaterial
    index = lb.curselection()[0]
    selectedMaterial = lb.get(index)

    nEntry.delete(0, END)
    nEntry.insert(END, selectedMaterial[1])
    aEntry.delete(0, END)
    aEntry.insert(END, selectedMaterial[2])
    pEntry.delete(0, END)
    pEntry.insert(END, selectedMaterial[3])
    dpEntry.delete(0, END)
    dpEntry.insert(END, selectedMaterial[4])
    tText.delete(0, END)
    tText.insert(END, selectedMaterial[5])


def removeMaterial():
    db.remove(selectedMaterial[0])
    clearInput()
    fillList()


def updateMaterial():
    db.update(selectedMaterial[0], nText.get(), aText.get(), pText.get(), dpText.get(), tText.get())
    fillList()


def clearInput():
    nEntry.delete(0, END)
    aEntry.delete(0, END)
    pEntry.delete(0, END)
    dpEntry.delete(0, END)


def searchMaterial():
    if nText.get() == '' and aText.get() == '' and pText.get() == '' and dpText.get() == '':
        fillList()
        clearInput()
    elif nText.get() == '' and pText.get() == '' and dpText.get() == '' and aText != '':
        lb.delete(0, END)
        for row in db.selectAuthor(aText.get()):
            lb.insert(END, row)
            continue
        clearInput()
    elif nText.get() == '' and aText.get() == '' and dpText.get() == '' and pText != '':
        lb.delete(0, END)
        for row in db.selectPublisher(pText.get()):
            lb.insert(END, row)
            continue
        clearInput()
    elif nText.get() == '' and aText.get() == '' and pText.get() == '' and dpText != '':
        lb.delete(0, END)
        for row in db.selectDateOfPublish(dpText.get()):
            lb.insert(END, row)
            continue
        clearInput()
    elif aText.get() == '' and pText.get() == '' and dpText.get() == '' and nText.get != '':
        lb.delete(0, END)
        for row in db.selectName(nText.get()):
            lb.insert(END, row)
            continue
        clearInput()
    else:
        messagebox.showerror("Error!", "Please fill only one box!")


def helpCommand():
    messagebox.showinfo("Help Tips", "INSERT MATERIAL:\nUser should fill all boxes of Material Name, Author, Publisher, "
                                     "and Date of Publish.\nPlease keep the format of date as DD/MM/YYYY as possible.\n"
                                     "I understand that some material may not give clear date.\nSuch as, c1988 etc. so I did not set limit.\n"
                                     "The Type of Material is defaulted as Book.\nIf the material is not book, "
                                     "user could change it\n\nREMOVE & UPDATE MATERIAL:\nSelect a material in listbox first.\n\n"
                                     "CLEAR INPUT:\nThis function is only use to clear the text what user inputted in the boxes.\n"
                                     "This button will not clear any data it stored.\n\nSEARCH MATERIAL:\n"
                                     "Due to the technical issues, it only allow user to search the material in one element.\n"
                                     "Which means only input one of material Name, Author, Publisher, or Date of Publish to search.\n"
                                     "The type element will not works in this function.\nClick again without input, to return full list")


# create a window and named Material Management
mm = Tk()
mm.title("Material Management")
mm.geometry('1024x720')

# create a top menubar
menuBar = Menu(mm)
fileMenu = Menu(menuBar, tearoff=False)
fileMenu.add_command(label="Help", command=helpCommand)
fileMenu.add_command(label="Made by:", state=DISABLED)
fileMenu.add_command(label="LainHE", state=DISABLED)
menuBar.add_cascade(label="About", menu=fileMenu)
mm.config(menu=menuBar)

# Name
nText = StringVar()
nLabel = Label(mm, text="Material Name", font=('Helvetica', 14), pady=20, padx=20)
nLabel.grid(row=0, column=1)
nEntry = Entry(mm, textvariable=nText)
nEntry.grid(row=1, column=1)
# Author
aText = StringVar()
aLabel = Label(mm, text="Author", font=('Helvetica', 14))
aLabel.grid(row=0, column=2)
aEntry = Entry(mm, textvariable=aText)
aEntry.grid(row=1, column=2)
# Publisher
pText = StringVar()
pLabel = Label(mm, text="Publisher", font=('Helvetica', 14))
pLabel.grid(row=0, column=3)
pEntry = Entry(mm, textvariable=pText)
pEntry.grid(row=1, column=3)
# Date of Publish
dpText = StringVar()
dpLabel = Label(mm, text="Date of Publish", font=('Helvetica', 14))
dpLabel.grid(row=0, column=4)
dpEntry = Entry(mm, textvariable=dpText)
dpEntry.grid(row=1, column=4)
# Type
tlabel = Label(mm, text="Select a Type", font=('Helvetica', 14))
tlabel.grid(row=0, column=5)
tComboxlist = StringVar()
tText = ttk.Combobox(mm, values=["Book", "Magazine", "Newspaper", "CD/DVD"])
tText.current(0)
tText.grid(row=1, column=5)

# Listbox
lb = Listbox(mm, height=26, width=108)
lb.grid(row=4, column=1, rowspan=6, columnspan=7, padx=20)
lb.config(font=('Helvetica', 12))
# Scrollbar
sb = Scrollbar(mm)
sb.grid(row=4, column=7, rowspan=6, sticky=S + N)
lb.configure(yscrollcommand=sb.set)  # Bind the scrollbar with listbox
sb.configure(command=lb.yview)

# show the order of data
order = Label(mm, text="ORDER OF DISPLAY\nID -> Material Name -> Author -> Publisher -> Date of Publish -> Type "
                       "(See more helps in Help under About menubar)", anchor=W, width=112)
order.grid(row=3, column=1, columnspan=6)
# fill the data into list
fillList()
# bind the comboxlist
tText.bind("<<ComboboxSelected>>", comboboxSelect)
# bind the select function
lb.bind('<<ListboxSelect>>', selectMaterial)

# Buttons
addBtn = Button(mm, text="Insert Material", width=15, command=insertMaterial)
addBtn.grid(row=2, column=1, pady=20)

removeBtn = Button(mm, text="Remove Material", width=15, command=removeMaterial)
removeBtn.grid(row=2, column=2)

updateBtn = Button(mm, text="Update Material", width=15, command=updateMaterial)
updateBtn.grid(row=2, column=3)

clearBtn = Button(mm, text="Clear Input", width=15, command=clearInput)
clearBtn.grid(row=2, column=4)

searchBtn = Button(mm, text="Search Material", width=15, command=searchMaterial)
searchBtn.grid(row=2, column=5)

createrName = Label(mm, text="LainHE", width=8, anchor=E)
createrName.grid(row=0, column=6, sticky=NE)

# Enter the loop
mm.mainloop()