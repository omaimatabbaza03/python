import tkinter as tk
import pymongo
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient

# Create the GUI
root = tk.Tk()
root.title('the student')
root.configure(bg="#eee")
root.geometry('1100x600+300+200')
root.resizable(False,False)

# Connexion à la base de données MongoDB
conn_str = "mongodb://localhost:27017/"
def ajoute():
    idd= id_entry.get()
    date= date_entry.get()
    duree= duree_entry.get()
    name = Nom_entry.get()
    num = int(Numero_entry.get())
    group = Group_entry.get()
    
    client = MongoClient(conn_str)
       # Accéder à la base de données "test"
    db = client["test"]
# create a new collection
    my_collection = db["student"]
# Création d'un document à insérer dans la collection
    document= {"_id":idd,"DATE":date,"Name":name,"NUM":num,"GROUP":group,"DUREE":duree}
# Insertion du document dans la collection
    result = my_collection.insert_one(document)
# Affichage de l'identifiant du document inséré
    if(result.inserted_id):

        messagebox.showinfo("ajoute","student ajouter")
        
        y=my_collection.find({})
        for row in y:
            #insert les donnee
            tree.insert('', 0,  text=row['_id'],values=(row['DATE'],row['Name'],row['NUM'],row['GROUP'], row['DUREE']))
    client.close()
#modifier
def modifier():
    idd= id_entry.get()
    date= date_entry.get()
    duree= duree_entry.get()
    name = Nom_entry.get()
    num = int(Numero_entry.get())
    group = Group_entry.get()

    client = MongoClient(conn_str)
    db = client["test"]
    my_collection = db["student"]
    result = my_collection.update_one({'_id':idd},{'$set':{"DATE":date,"Name":name,"NUM":num,"GROUP":group,"DUREE":duree}})
    if(result):
        messagebox.showinfo("modifeir","student modifier")
        y=my_collection.find({})
        for row in y:
            #insert les donnee
            tree.insert('', 0,  text=row['_id'],values=(row['DATE'],row['Name'],row['NUM'],row['GROUP'], row['DUREE']))
    client.close()

#supprimer
def supprimer():
     idd= id_entry.get()
     client = MongoClient(conn_str)
     db = client["test"]
     my_collection = db["student"]
     result = my_collection.delete_one({'_id':idd})
     if(result):
       messagebox.showinfo("supprimer","student supprimer")
        y=my_collection.find({})
        for row in y:
            #insert les donnee
            tree.insert('', 0,  text=row['_id'],values=(row['DATE'],row['Name'],row['NUM'],row['GROUP'], row['DUREE']))
     client.close()
#Ajoute titre
titre = tk.Label(root,bd=20,text="GESTION DES ABSENCES",font=("Arial",30),bg="#86A8E7",fg="white") #tester la form de label
titre.place(x=0,y=0,width=1100,height=60)
#LISTE DE ABSENCES
liste = tk.Label(root,text="LISTES DES ABSENCES",font=("Arial",30),bg="#86A8E7",fg="white") #tester la form de label
liste.place(x=400,y=120,width=600)
#créee formulaire
#Id
idd= tk.Label(root, text="Id :",font=("Arial",16)) #tester la form de label
idd.pack()
idd.place(x=10,y=70)
id_entry = tk.Entry(root,bg='white',width=30, font='Helvetica 12') #tester form de input
id_entry.pack()
id_entry.place(x=10,y=100, width=250,height=30)
#date abse
date = tk.Label(root, text="Date Absence :",font=("Arial",16)) #tester la form de label
date.pack()
date.place(x=10,y=130)
date_entry = tk.Entry(root,bg='white', font='Helvetica 12') #tester form de input
date_entry.pack()
date_entry.place(x=10,y=160, width=250,height=30)
#Duree d'absences
Duree = tk.Label(root, text="Duree Absences :",font=("Arial",16)) #tester la form de label
Duree.pack()
Duree.place(x=10,y=200)

duree_entry= tk.Entry(root,bg='white',width=30, font='Helvetica 12') #tester form de input
duree_entry.pack()
duree_entry.place(x=10,y=230, width=250,height=30)
#Nom de stagiare
Nom = tk.Label(root, text="Nom Stagiare :",font=("Arial",16)) #tester la form de label
Nom.pack()
Nom.place(x=10,y=260)
Nom_entry = tk.Entry(root,bg='white',width=30, font='Helvetica 12') #tester form de input
Nom_entry.pack()
Nom_entry.place(x=10,y=290, width=250,height=30)
#Num de stagiare
Numero = tk.Label(root, text="Numero Stagiare :",font=("Arial",16)) #tester la form de label
Numero.pack()
Numero.place(x=10,y=320)
Numero_entry = tk.Entry(root,bg='white',width=30, font='Helvetica 12') #tester form de input
Numero_entry.pack()
Numero_entry.place(x=10,y=350, width=250,height=30)
#Group
Group = tk.Label(root, text="Group :",font=("Arial",16)) #tester la form de label
Group.pack()
Group.place(x=10,y=380)
Group_entry = tk.Entry(root,bg='white',width=30, font='Helvetica 12') #tester form de input
Group_entry.pack()
Group_entry.place(x=10,y=410, width=250,height=30)
#button enregistrer
btnEnr= tk.Button(root, text="Enregistrer", width=15,cursor='hand2', command=ajoute,fg="white",bg='#86A8E7' ,font='Helvetica 12 bold')
btnEnr.pack()
btnEnr.place(x=20,y=450)
#button Modifier
btnMod= tk.Button(root, text="Modifier", width=15,cursor='hand2', command=modifier,fg="white",bg='#86A8E7' ,font='Helvetica 12 bold')
btnMod.pack()
btnMod.place(x=200,y=450)
#button Supprimer
btnMod= tk.Button(root, text="Supprimer", width=15,cursor='hand2',command=supprimer,fg="white",bg='#86A8E7' ,font='Helvetica 12 bold')
btnMod.pack()
btnMod.place(x=100,y=490)
#table
# create a ttk.Treeview widget
tree = ttk.Treeview(root)
# add some columns to the treeview
tree["columns"] = (1,2,3,4,5)
tree.heading("#0",text="ID")
tree.heading(1, text="DATE")
tree.heading(2, text="Name")
tree.heading(3, text="NUM")
tree.heading(4, text="GROUP")
tree.heading(5, text="DUREE")
tree.column(0,width=50)
tree.column(1,width=100)
tree.column(2,width=100)
tree.column(3,width=100)
tree.column(4,width=100)
tree.column(5,width=100)
tree.pack()
tree.place(x=350,y=200)
# Run the GUI
root.mainloop()
