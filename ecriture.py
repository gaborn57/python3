#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
##from PIL import Image
from glob import iglob
from random import choice
import os

# select a random file:
liste = iglob('pictures/*.png')
liste = list(liste)

# pick a random item from the list
fichier = choice(liste)
image = os.path.basename(fichier).split('.')[0]
print(image)

# create the image window
image = Tk()
image.title('Image')
image.resizable(width=False, height=False)

cv = Canvas()
pic = PhotoImage(file = fichier)
width = pic.width()
height = pic.height() + 200

c = Canvas(image, width = width, height = height)
item = c.create_image(width, height, image = pic, anchor = 'se')
c.pack(side='bottom')

## create the control window
#command = Tk()
#command.title('Contrôles')
#command.resizable(width = False, height = False)
#command.geometry('{}x{}'.format(1024, 400))

mainloop()
