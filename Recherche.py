import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient

# Create the GUI
root = tk.Tk()
root.title('recherche des absences')
root.configure(bg="#eee")
root.geometry('1000x600+300+200')
root.resizable(False,False)

# Connexion à la base de données MongoDB
conn_str="mongodb://localhost:27017/"
#Methode Afficher
def affiche():
    name = Nom_entry.get()
    
    client = MongoClient(conn_str)
     db = client["test"]

    my_collection = db["student"]
    y=my_collection.find({"Name":name})
    for row in y:
        
        tree.insert('', 0,  text=row['_id'],values=(row['DATE'],row['Name'],row['NUM'],row['GROUP'], row['DUREE']))
        client.close()
        
#create title;
heading=tk.Label(root, text="Rechercher des absences" ,bg= '#86A8E7' ,fg= 'white',font=('Microsoft YaHei UI Light',23, 'bold'))
heading.place(x=0,y=0,width=1000,height=40)


#Nom de stagiare
Nom = tk.Label(root, text="Nom Stagiare :",font=("Arial",16)) #tester la form de label
Nom.pack()
Nom.place(x=100,y=70)

Nom_entry = tk.Entry(root,bg='white',width=30, font='Helvetica 12') #tester form de input
Nom_entry.pack()
Nom_entry.place(x=100,y=120, width=300,height=30)

#button Afficher
btnEnr= tk.Button(root, text="Afficher", width=20,cursor='hand2', command=affiche,fg="white",bg='#86A8E7' ,font='Helvetica 12 bold')
btnEnr.pack()
btnEnr.place(x=500,y=120)

#titre

titre = tk.Label(root,bd=20,text="Les nombre des absences par chaque stagiaire",font=("Arial",16),fg="black") #tester la form de label
titre.place(x=100,y=170)

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
tree.place(x=100,y=250)
# Run the GUI
root.mainloop()

