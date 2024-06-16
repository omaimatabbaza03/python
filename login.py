import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the username and password are valid
    if username == "admin" and password == "1234":
       
        #screen=tk.Toplevel(root)
        #screen.title('app')
        #root.config(bg="#ddd")
        #root.geometry('925x500+300+200')
        #tk.Label(screen,text='Hello Everyone!',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        #screen.mainloop()
        import home
    elif password!="1234" and username!="admin":
        messagebox.showerror("Invalid","Invalid username or password")
   
    elif password!="1234":
                messagebox.showerror("Invalid","Invalid   password")

    elif username!="admin":
                messagebox.showerror("Invalid","Invalid username")
# Create the GUI
root = tk.Tk()
root.title('Login')
root.configure(bg="#eee")
root.geometry('925x500+300+200')
root.resizable(False,False)
#create title;
heading=tk.Label(root, text="Sign in" ,fg= '#86A8E7' ,font=('Microsoft YaHei UI Light',23, 'bold'))
heading.place(x=550,y=55)
# Create the username label and entry
username_label = tk.Label(root, text="Username", font='Helvetica 12 bold') #tester la form de label
username_label.pack()
username_label.place(x=500,y=120)
username_entry = tk.Entry(root,bg='white',border=3,width=30, font='Helvetica 12') #tester form de input
username_entry.pack()
username_entry.place(x=500,y=150)
# Create the password label and entry
password_label = tk.Label(root, text="Password", font='Helvetica 12 bold')
password_label.pack()
password_label.place(x=500,y=200)
password_entry = tk.Entry(root, show="*",width=30,bg='white',border=3, font='Helvetica 12')
password_entry.pack()
password_entry.place(x=500,y=230)
# Create the login button
login_button = tk.Button(root, text="Login", width=28,cursor='hand2', command=login,fg="white",bg='#86A8E7' ,font='Helvetica 12 bold')
login_button.pack()
login_button.place(x=500,y=280)
# Create the message label to display login status
message_label = tk.Label(root, text="")
message_label.pack()
# Create a canvas for the background image
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()
canvas.place(x=10,y=100)
# Load the background image
image = Image.open("login.jpg")
background_image = ImageTk.PhotoImage(image)
# Add the background image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
# Run the GUI
root.mainloop()
