#! /usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import re
from sys import stdout

main=Tk()

w=Canvas(main, width=500, height=800)
w.pack()

part=0
gagne=False
secret='helicoptere' # my favorite hangman word :)
decouvert=[]

def dessine_prochaine_partie(nb):
  a=[(20,780,480,780),
     (175,780,175,20),
     (50,20,450,20),
     (175,95,250,20),
     (380,20,380,100),
     (),
     ()]

  if nb==5:
    w.create_oval(340,100, 420,180,width=10)
  elif nb==6:
    w.create_line(380,180,380,430, width=10) # neck

    w.create_line(380,240,440,400, width=10) # arm on right side
    w.create_line(380,240,320,400, width=10) # arm on left  side

    w.create_line(380,430,440,550, width=10) # leg on right side
    w.create_line(380,430,320,550, width=10) # leg on left  side
  else:
    w.create_line(a[nb],width=10)

def affiche_texte():
  for i in range(len(secret)):
    if secret[i] in decouvert:
      stdout.write(secret[i])
    else:
      stdout.write('-')
  stdout.write('\n')

while part!=7 and gagne==False:
  lettre=input("Quelle lettre voulez-vous demander ?")
  m=re.match('^[a-zA-Z]$',lettre)
  if not m:
    print('Veuillez svp n\'entrer qu\'un seul caractère alphabétique (a-zA-Z)!')
    continue
  if lettre not in secret:
    dessine_prochaine_partie(part)
    part+=1
  else:
    decouvert.append(lettre)
    # il manque encore le cas où on gagne, à mettre ici :)
  affiche_texte()

if part==7:
  print('Vous avez perdu')
  main.destroy()



mainloop()
