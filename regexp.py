#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-

import re

series='Miss Fisher:Phrany Fisher;GOT:Daenerys Targaryen;X-Files:Dana Scully;Miss Fisher:Jack Robinson;Miss Fisher:Dorothy Williams;GOT:Jon Snow;GOT:Tyrion Lannister;X-Files:Fox Mulder'

pattern=r':([a-zA-Z ]+)[;|$]'
match=re.findall(r'GOT'+pattern, series)
print(match)
