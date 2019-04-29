#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-

from tkinter import *
import glob
import random
from PIL import Image, ImageTk
import sys

# quelques initialisations
images = []
gImage = ''

# charge la liste d'images disponibles
for file in glob.glob('pictures/*.jpeg'):
  images.append(file.split('/')[1].split('.')[0])

# enregistre le nombre d'images trouvées, pour afficher le taux de réussite à la fin du jeu
nbpic = len(images)

# fonction pour en choisir une au hasard
def auhasard(tableau):
  if len(tableau) != 0:
    tmp = random.choice(tableau)
    tableau.remove(tmp)
    return tmp
  else:
    return None

def Quitter(window):
  sys.exit(0)

def check_content(event, window):
  if event.get() == gImage:
    print("Bravo!")
    # go to next picture
    window.destroy()
  else:
    print("Failed!")

def Affiche():
  fenetre = Tk()
  fenetre.title('Ecriture')
  fenetre.resizable(0,0) # prevent <<maximize>> window
  im  = Image.open('pictures/{}.jpeg'.format(gImage))
  img = ImageTk.PhotoImage(im)
  cv = Canvas(fenetre, width=im.width+10, height=im.height+10)
  cv.pack(padx = 10, pady = 10)
  cv.create_image(0, 0, image = img, anchor = 'nw')
  t = Label(fenetre, text = 'Que représente cette image ?')
  t.pack()
  e = Entry(fenetre)
  e.pack()
  e.bind('<Return>', (lambda _: check_content(e, fenetre)))
  e.focus_set()
  b = Button(fenetre, text="Quitter", command = lambda: Quitter(fenetre))
  b.pack()
  fenetre.mainloop()

while (len(images) > 0):
  gImage = auhasard(images)
  Affiche()
