#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from glob import iglob
from random import choice
import os

# select a random file:
liste = iglob('pictures/*.png')
liste = list(liste)

def PickRandom(liste):
  fichier = choice(liste)
  return (fichier, os.path.basename(fichier).split('.')[0])

def AfficheRandomImage(window, liste):
  (fichier, image) = PickRandom(liste) 
  print(image)
  window.withdraw()
  
  window.deiconify()

# pick a random item from the list
(fichier, image) = PickRandom(liste)
print(fichier, image)

# create the image window
ecriture = Tk()
ecriture.title('Ecriture')
ecriture.resizable(width=False, height=False)

ecriture.withdraw()
ecriture.update_idletasks()
x = (ecriture.winfo_screenwidth() - ecriture.winfo_reqwidth())/2
y = (ecriture.winfo_screenheight() - ecriture.winfo_reqheight())/2

##ecriture.geometry("+{}+{}".format(int(x), int(y)))
ecriture.geometry("+10+100")
ecriture.deiconify()

cv = Canvas()

BoutonAutre = Button(ecriture, text = 'Une autre', command = AfficheRandomImage(ecriture, liste))
BoutonAutre.pack(padx = 5, pady = 5)

pic = PhotoImage(file = fichier)
width = pic.width()
height = pic.height()

c = Canvas(ecriture, width = width, height = height)
item = c.create_image(width, height, image = pic, anchor = 'se')
c.pack(side='bottom')

mainloop()
