#////////////////////////////////////////////////////////////
#//           Made by Gonçalo Mano                        //
#//        Random password Generator without Keyword     //
#//            18/02/2019                               //
#////////////////////////////////////////////////////////
import tkinter as tk
import string
import random
def password():
    l= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","w","z","0","1","2","3","4","5","6","7","8","9"]
    password1= l[random.randint(0,35)]
    password2= l[random.randint(0,35)]
    password3= l[random.randint(0,35)]
    password4= l[random.randint(0,35)]
    password5= l[random.randint(0,35)]
    password6= l[random.randint(0,35)]
    password7= l[random.randint(0,35)]
    password8= l[random.randint(0,35)]
    passwordfinal=password1+password2+password3+password4+password5+password6+password7+password8
    print(passwordfinal)
    resultLabel = tk.Label(root, text = passwordfinal)
    resultLabel.pack()
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Generate Password",
                   command=password)
slogan.pack(side=tk.LEFT)
root.title("Random Password Generator !")
root.mainloop()
