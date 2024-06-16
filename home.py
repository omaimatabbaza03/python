import tkinter as tk
import webbrowser #deplacer entre les pages
import time
def clock(): #function de date et time
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f' Date:   {date}\nTime:  {currenttime}')
    datetimeLabel.after(1000, clock)## pour changer time
def saisie():
    import saisie
    #webbrowser.open_new()

def Recherche():
    import Recherche
def quitter():
    import login.py
# Créer la fenêtre principale
root = tk.Tk()
root.title("gestion des absences")
root.configure(bg="#eee")
root.geometry('925x500+300+200')
root.resizable(False,False)
# Créer le menu
menu_bar = tk.Menu(root)
# Ajouter les éléments de menu
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Saisie absence", command=saisie)
menu_file.add_command(label="Recherche absence", command=Recherche)
menu_file.add_command(label="quitter", command=quitter)
menu_bar.add_cascade(label="Menu", menu=menu_file)
# Configurer la fenêtre principale pour utiliser le menu
root.config(menu=menu_bar)
#create title;
heading=tk.Label(root, text="Gestion des absences" ,bg= '#86A8E7' ,fg= 'white',font=('Microsoft YaHei UI Light',23, 'bold'))
heading.place(x=0,y=0,width=1000,height=40)
#saisie la date
datetimeLabel = tk.Label(root, font='Helvetica 12 bold') #tester la form de label
datetimeLabel.pack()
datetimeLabel.place(x=30,y=60)
clock()
# Lancer la boucle principale
root.mainloop()
