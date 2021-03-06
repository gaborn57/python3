#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-

import re

series='Miss Fisher:Phrany Fisher;GOT:Daenerys Targaryen;X-Files:Dana Scully;Miss Fisher:Jack Robinson;Miss Fisher:Dorothy Williams;GOT:Jon Snow;GOT:Tyrion Lannister;X-Files:Fox Mulder'

# on donne au findall le pattern et la source. Il génère un tableau
pattern=r':([a-zA-Z ]+)[;$]'
match=re.findall(r'GOT'+pattern, series)

# ou alors on applique un findall, mais cette fois sur un objet compilé
pattern2=re.compile(r'GOT:([A-Za-z ]+)[;$]')
match2=pattern2.findall(series)

# et les résultats sont identiques
print(match)
print(match2)
