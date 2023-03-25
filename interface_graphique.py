#!/usr/bin/python3

import module_arbre as ma
import main
import tkinter as tk

fenetre = tk.Tk()

canvas = tk.Canvas(fenetre,width =800,height =800,bg = "white")
#canvas.grid(row=3,columnspan=3)

text1 = tk.StringVar()
boite_texte1 = tk.Entry(fenetre, textvariable=text1)
boite_texte1.focus()
bouton_texte1 = tk.Button(fenetre, text="crypter", command=lambda : result1.config(text=main.crypter_text(text1.get())))
result1 = tk.Label(fenetre, text="")

boite_texte1.grid(row=1, column=0, columnspan=3, ipadx=100, ipady=10)
bouton_texte1.grid(row=1, column=3)
result1.grid(row=2,column=0)


text2 = tk.StringVar()
boite_texte2 = tk.Entry(fenetre, textvariable=text2)
boite_texte2.focus()
bouton_texte2 = tk.Button(fenetre, text="decrypter", command=lambda : result2.config(text=main.decrypter_text(text2.get())))
result2 = tk.Label(fenetre, text="")

boite_texte2.grid(row=3, column=0, columnspan=3, ipadx=100, ipady=10)
bouton_texte2.grid(row=3, column=3)
result2.grid(row=4)

    
    
    
    
def draw_arbre(fg,fd,racine):
    x1,y1,x2,y2 = 750,750,800,800
    canvas.create_oval(x1,y1,x2,y2,fill ="black")# fg
    canvas.create_text(x1+25,y1+25,text = fg,fill ="yellow")
    canvas.create_oval(x1-150,y1,x2-150,y2,fill ="black")# fd
    canvas.create_text(x1-150+25,y1+25,text = fd,fill ="yellow")
    canvas.create_oval(x1-75,y1-50,x2-75,y2-50,fill ="black")
    canvas.create_text(x1-75+25,y1-50+25,text = racine,fill ="yellow")

s1 = ma.Sommet("a", 2)
s2 = ma.Sommet("e", 3)
a1 = ma.ArbreB()
a1.insertion(s1)
a1.insertion(s2)        

#draw_arbre(a1.get_fils_gauche().get_lettre(),a1.get_fils_droit().get_lettre(),a1.get_racine().get_lettre())
fenetre.mainloop()
