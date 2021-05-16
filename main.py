import tkinter as tk
from tkinter import *

def save_info():
    varsta_info = varsta.get()
    sex_info = sex.get()
    greutate_info = greutate.get()
    inaltime_info = inaltime.get()
    sedentar_info = sedentarVar.get()
    activitateRedusa_info = activitateRedusaVar.get()
    activ_info = activVar.get()
    factiv_info = fActivVar.get()
    slabire_info=slabireVar.get()
    mentinere_info=mentinereVar.get()
    ingrasare_info=ingrasareVar.get()

#Background
body = Tk()
body.geometry("500x500")
body.title("Calculator de calorii")
titlu = Label(text = "Calculator de calorii", fg ="blue", width="500",height="3")
titlu.pack()


#Intrari_text

varsta_text = Label(text = "Varsta:", fg ="blue")
varsta_text.place(x=10,y=50)

sex_text = Label(text = "Sex(M/F):", fg ="blue")
sex_text.place(x=10,y=100)

greutate_text = Label(text = "Greutate(kg):", fg ="blue")
greutate_text.place(x=10,y=150)

inaltime_text = Label(text = "Inaltime(cm):", fg ="blue")
inaltime_text.place(x=10,y=200)

activitate_text = Label(text = "Tipul activitatii fizice:", fg ="blue")
activitate_text.place(x=10,y=250)

scop_text = Label(text = "Scopul:", fg ="blue")
scop_text.place(x=10,y=300)

#Variabile
varsta=IntVar()
sex=StringVar()
greutate=IntVar()
inaltime=IntVar()


#Intrari_casete
varsta_entry = Entry(text = varsta)
sex_entry = Entry(text = sex)
greutate_entry = Entry(text = greutate)
inaltime_entry = Entry(text = inaltime)

#VariabileActivitate
sedentarVar=StringVar()
activitateRedusaVar=StringVar()
activVar=StringVar()
fActivVar=StringVar()

inputActivitate = Menubutton(body,text="Activitate",width = 12)
inputActivitate.menu = Menu(inputActivitate,tearoff= 0)
inputActivitate["menu"] = inputActivitate.menu
inputActivitate.menu.add_checkbutton(label="Sedentar" ,variable=sedentarVar)
inputActivitate.menu.add_checkbutton(label="Activitate Redusa",variable=activitateRedusaVar)
inputActivitate.menu.add_checkbutton(label="Activ",variable=activVar)
inputActivitate.menu.add_checkbutton(label="Foarte Activ",variable=fActivVar)

#VariabileScop
slabireVar=StringVar()
mentinereVar=StringVar()
ingrasareVar=StringVar()

inputScop = Menubutton(body,text="Scop",width = 12)
inputScop.menu = Menu(inputScop,tearoff= 0)
inputScop["menu"] = inputScop.menu
inputScop.menu.add_checkbutton(label="Slabire" ,variable=slabireVar)
inputScop.menu.add_checkbutton(label="Mentinere",variable=mentinereVar)
inputScop.menu.add_checkbutton(label="Ingrasare",variable=ingrasareVar)

#Pozitionare casete
varsta_entry.place(x=50, y=50)
sex_entry.place(x=70, y=100)
greutate_entry.place(x=100, y=150)
inaltime_entry.place(x=100, y=200)
inputActivitate.place(x=130, y=250)
inputScop.place(x=60, y=300)

#Buton
calculeazaButon = Button(body,text = "Calculeaza",width = "30", height = "2" )
calculeazaButon.place(x=130,y=350)

body.mainloop() #initializare GUI
