#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
z1 = form.getfirst("z1", "не задано")
z2 = form.getfirst("z2", "не задано")
z3 = form.getfirst("z3", "не задано")
z4 = form.getfirst("z4", "не задано")
mass=[]
mass.append(html.escape(z1))
mass.append(html.escape(z2))
mass.append(html.escape(z3))

z4 = html.escape(z4)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>Обработка данных форм</title>
          </head>
          <body>""")
if mass[0]==z4 or mass[1]==z4 or mass[2]==z4 :
    print("Элемент с указанным значением найден! его номер:",mass.index(z4)+1,"<br>")
else:
    print("Элемент с указанным значением не найден!<br>")
