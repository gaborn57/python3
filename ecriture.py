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

def AfficheRandomImage(liste):
  (fichier, image) = PickRandom(liste) 
  print(image)

# pick a random item from the list
(fichier, image) = PickRandom(liste)
print(fichier, image)

# create the image window
ecriture = Tk()
ecriture.title('Ecriture')
ecriture.resizable(width=False, height=False)

cv = Canvas()

BoutonAutre = Button(ecriture, text = 'Une autre', command = AfficheRandomImage(liste))
BoutonAutre.pack(padx = 5, pady = 5)

pic = PhotoImage(file = fichier)
width = pic.width()
height = pic.height()

c = Canvas(ecriture, width = width, height = height)
item = c.create_image(width, height, image = pic, anchor = 'se')
c.pack(side='bottom')

mainloop()
