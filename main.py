import tkinter as tk
from tkinter import *


body = Tk()
body.geometry("500x500")
body.title("Calculator de calorii")
titlu = Label(text = "Calculator de calorii", fg ="blue", width="500",height="3")
titlu.pack()




def calculator():
#Background

    top = Toplevel()
    top.geometry("500x500")
    top.title("Calculator")

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

        offset = IntVar()
        if(sex_info == "M"):
            RMB = int(10*greutate_info+6.25*inaltime_info-5*varsta_info+5)
        if(sex_info == "F"):
            RMB = int(10*greutate_info+6.25*inaltime_info-5*varsta_info-161)
        if(sedentar_info == "1"):
            offset = 1.2
        if(activitateRedusa_info == "1"):
            offset = 1.375
        if(activ_info == "1"):
            offset = 1.55
        if(factiv_info == "1"):
            offset = 1.9
        caloriiBaza = RMB * offset
        if(slabire_info == "1"):
            caloriiBaza = caloriiBaza-500
        if(mentinere_info == "1"):
            caloriiBaza = caloriiBaza
        if(ingrasare_info == "1"):
            caloriiBaza = caloriiBaza + 500

        T = Label(top,height=2, width=4,text=int(caloriiBaza))
        T.place(x=240,y=400)
        rez = Label(top,height=2,width=9,text="Rezultat:")
        rez.place(x=170,y=400)
        print(RMB,sedentar_info,offset,caloriiBaza)

    #Intrari_text

    varsta_text = Label(top,text = "Varsta:", fg ="blue")
    varsta_text.place(x=10,y=50)

    sex_text = Label(top,text = "Sex(M/F):", fg ="blue")
    sex_text.place(x=10,y=100)

    greutate_text = Label(top,text = "Greutate(kg):", fg ="blue")
    greutate_text.place(x=10,y=150)

    inaltime_text = Label(top,text = "Inaltime(cm):", fg ="blue")
    inaltime_text.place(x=10,y=200)

    activitate_text = Label(top,text = "Tipul activitatii fizice:", fg ="blue")
    activitate_text.place(x=10,y=250)

    scop_text = Label(top,text = "Scopul:", fg ="blue")
    scop_text.place(x=10,y=300)

    #Variabile
    varsta=IntVar()
    sex=StringVar()
    greutate=IntVar()
    inaltime=IntVar()


    #Intrari_casete
    varsta_entry = Entry(top,text = varsta)
    sex_entry = Entry(top,text = sex)
    greutate_entry = Entry(top,text = greutate)
    inaltime_entry = Entry(top,text = inaltime)

    #VariabileActivitate
    sedentarVar=StringVar()
    activitateRedusaVar=StringVar()
    activVar=StringVar()
    fActivVar=StringVar()

    inputActivitate = Menubutton(top,text="Activitate",width = 12)
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

    inputScop = Menubutton(top,text="Scop",width = 12)
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
    calculeazaButon = Button(top,text = "Calculeaza",width = "30", height = "2" ,command=save_info)
    calculeazaButon.place(x=130,y=350)

def evidenta():
    top2 = Toplevel()
    top2.geometry("500x500")
    top2.title("Evidenta")
    mancare=StringVar()
    cantitate=IntVar()
    mesaj1_text = Label(top2,text = "Introduceti numele mancarii:", fg ="blue").pack()
    mesaj2_text = Label(top2,text = "Nume:", fg ="blue").pack()
    mancare_entry = Entry(top2,text = mancare).pack()
    mesaj3_text = Label(top2,text = "Cantitate:", fg ="blue").pack()
    cantitate_entry = Entry(top2,text = cantitate).pack()
    btn3 = Button(top2,text="Inregistreaza").pack()
    mesaj4_text = Label(top2,text = "Valorile nutrititonale sunt:", fg ="blue").pack()


btn = Button(body,text="Calculator",command=calculator).pack()
btn2 = Button(body,text="Test",command=evidenta).pack()
mainloop() #initializare GUI
