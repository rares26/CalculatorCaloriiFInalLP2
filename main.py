import tkinter as tk
from tkinter import *
import json


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
        mancare_info=mancareVar.get()

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


    def rezultat():
        customerData ="""{
        "ceafa de porc": "20.9 proteine , 5.5 lipide , 0 glucide , 235 calorii",
        "muschi de porc": "23.9 proteine , 14.3 lipide , 0 glucide , 231 calorii",
        "sunca afumata": "17.2.9 proteine , 3.2 lipide , 0 glucide , 201 calorii",
        "mici de porc-vita": "20 proteine , 33 lipide , 0 glucide , 388 calorii",
        "pulpe de pui dezosate": "29 proteine , 5.2 lipide , 0 glucide , 190 calorii",
        "snitel de pui": "21.3 proteine , 5.9 lipide , 0 glucide , 198 calorii",
        "carnati la gratar": "22 proteine , 6.6 lipide , 0 glucide , 235 calorii",
        "coasta de porc": "32 proteine , 9 lipide , 0 glucide , 243 calorii",
        "ceafa de miel": "29 proteine , 6.5 lipide , 0 glucide , 190 calorii",
        "hering": "18 proteine , 10 lipide , 1 glucide , 186 calorii",
        "pastrav": "18.4 proteine , 12 lipide , 14 glucide , 90 calorii",
        "somn": "20.9 proteine , 5.5 lipide , 12 glucide , 82 calorii",
        "cartofi prajiti": "4 proteine , 12 lipide , 12 glucide , 319 calorii",
        "ceafa de porc": "10 proteine , 12 lipide , 14 glucide , 225 calorii",
        "cartofi piure": "10 proteine , 21 lipide , 13.2 glucide , 180 calorii",
        "cartofi nature": "19 proteine ,  18 lipide , 18 glucide , 70 calorii",
        "legume la gratar": "20 proteine , 12 lipide , 2 glucide , 87 calorii",
        "ciuperci la gratar": "14proteine , 19 lipide , 12 glucide , 40 calorii",
        "fasole verde": "24.9 proteine , 21 lipide , 3.2 glucide , 23 calorii",
        "supa de pui": "15 proteine , 3 lipide , 9 glucide , 123 calorii",
        "supa de legume": "12 proteine , 5 lipide , 8 glucide , 126 calorii",
        "ciorba de fasole": "20 proteine , 12 lipide , 6.2 glucide , 90 calorii",
        "ciorba taraneasca": "12 proteine , 11 lipide , 5.4 glucide , 67 calorii",
        "ciorba de perisoare": "11 proteine , 12 lipide , 8.3 glucide , 112 calorii",
        "supa crema de cartofi": "14 proteine , 14 lipide , 4.3 glucide , 101 calorii",
        "supa crema de legume": "14 proteine , 12.2 lipide , 6.5 glucide , 87 calorii",
        "baclava": "6.9 proteine , 5.5 lipide , 23 glucide , 234.3 calorii",
        "ecler": "5.9 proteine , 5.5 lipide , 34 glucide , 322 calorii",
        "prajitura Kinder": "9.9 proteine , 5.5 lipide , 67 glucide , 412.2 calorii",
        "savarina": "11.1 proteine , 9.3 lipide , 43 glucide , 213.3 calorii",
        "tiramisu": "8.7 proteine , 7.6 lipide , 32 glucide , 233.3 calorii",
        "cheesecake": "5.4 proteine , 12 lipide , 29.8 glucide , 223.2 calorii",
        "pandispan": "9.6 proteine , 12 lipide , 34 glucide , 235.3 calorii",
        "cozonac cu cacao si alune": "11.2 proteine , 14.6 lipide , 0 glucide , 192.2 calorii",
        "banane": "1.3 proteine , 0.3 lipide , 23 glucide , 94 calorii",
        "caise": "0.9 proteine , 0.4 lipide , 12.2 glucide , 51 calorii",
        "castane": "0.1 proteine , 0.5 lipide , 21 glucide , 123 calorii",
        "capsuni": "0.3 proteine , 0.2 lipide , 18.2 glucide , 93 calorii",
        "cirese": "1.3 proteine , 0.4 lipide , 19.3 glucide , 83 calorii",
        "mere": "1.2 proteine , 0.5 lipide , 9.3 glucide , 93 calorii",
        "pepene verde": "0.1 proteine , 0.4 lipide , 0.1 glucide , 23 calorii",
        "pepene galben": "0.2 proteine , 0.5 lipide , 0.2 glucide , 43 calorii",
        "pere": "0.3 proteine , 5.5 lipide , 0.4 glucide , 21 calorii",
        "piersici": "0.3 proteine , 0.2 lipide , 0.2 glucide , 76 calorii",
        "portocale": "0.4 proteine , 0.2 lipide , 0.2 glucide , 27 calorii",
        "prune": "0.4 proteine , 0.3 lipide , 0.4 glucide , 54 calorii",
        "struguri": "0.2 proteine , 0.4 lipide , 0.4 glucide , 102 calorii",
        "salata de varza": "2 proteine , 0.3 lipide , 1.1 glucide , 31 calorii",
        "salata de rosii": "2.3 proteine , 0.6 lipide , 11.1 glucide , 35 calorii",
        "salata de ton": "3 proteine , 1.1 lipide , 12 glucide , 45 calorii",
        "salata mexicana cu porumb ": "3.2 proteine , 2.2 lipide , 10 glucide , 23 calorii",
        "shaorma cu de toate": "8.2 proteine , 14.2 lipide , 19.0 glucide , 233 calorii",
        "kebap cu de toate": "7.5 proteine , 15.5 lipide , 17.2 glucide , 225 calorii",
        "shaorma la farfurie": "11.2 proteine , 16.5 lipide , 15.4 glucide , 292 calorii",
        "hamburger": "12.2 proteine , 8.7 lipide , 25.4 glucide , 190 calorii",
        "cheeseburger": "12.9 proteine , 15.5 lipide , 19.2 glucide , 196 calorii",
        "hot dog": "3.3 proteine , 14.5 lipide , 14.2 glucide , 154 calorii",
        "pizza diavola": "9.6 proteine , 5.5 lipide , 15.2 glucide , 202 calorii",
        "pizza capriciosa": "8.9 proteine , 5.5 lipide , 14.5 glucide , 219 calorii",
        "pizza quattro stagioni": "9.9 proteine , 12.2 lipide , 31.1 glucide , 192 calorii",
        "pizza salami": "7.9 proteine , 5.5 lipide , 13.4 glucide , 204 calorii",
        "piza margherita": "10.3 proteine , 5.5 lipide , 14 glucide , 212 calorii",
        "apa plata": "0 proteine , 0 lipide , 0 glucide , 0 calorii",
        "apa minerala": "0 proteine , 0 lipide , 0 glucide , 0 calorii",
        "cafea": "0 proteine , 0 lipide , 10 glucide , 32.2 calorii",
        "cafea cu lapte": "0 proteine , 0 lipide , 12 glucide , 43.1 calorii",
        "cappucino": "0 proteine , 0 lipide , 22 glucide , 89 calorii",
        "ceai de fructe de padure": "0 proteine , 0 lipide , 1.2 glucide , 2.1 calorii",
        "ceai nestea": "0 proteine , 0 lipide , 1.2 glucide , 4 calorii",
        "ceai verde": "0 proteine , 0 lipide , 1.3 glucide , 3 calorii",
        "ceai negru": "0 proteine , 0 lipide , 0.2 glucide , 2.2 calorii",
        "cola cola": "0 proteine , 0 lipide , 10.4 glucide , 52 calorii",
        "fanta": "0 proteine , 0 lipide , 10 glucide , 47 calorii",
        "sprite": "0 proteine , 0 lipide , 10.2 glucide , 32.9 calorii",
        "lipton": "0 proteine , 0 lipide , 8.7 glucide , 43.5 calorii",
        "frutti fresh": "0 proteine , 0 lipide , 9.8 glucide , 32.2 calorii",
        "smoothie cu capsuni": "0 proteine , 0 lipide , 13 glucide , 90 calorii",
        "smoothie cu cirese": "0 proteine , 0 lipide , 14 glucide , 92.2 calorii",
        "smoothie cu ananas si fructul pasiunii": "0 proteine , 0 lipide , 12.2 glucide , 87.7 calorii",
        "bere": "0 proteine , 0 lipide , 34 glucide , 45 calorii",
        "vin rosu": "0 proteine , 0 lipide , 20 glucide , 54 calorii",
        "vin alb": "0 proteine , 0 lipide , 21.1 glucide , 54.2 calorii"
        }"""
        
        
        
        
        
        
        
      






btn = Button(body,text="Calculator",command=calculator).pack()
btn2 = Button(body,text="Test",command=evidenta).pack()
mainloop() #initializare GUI
