#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
fio = form.getfirst("fio", "не задано")
pol = form.getfirst("pol", "не задано")
edu = form.getfirst("edu", "не задано")
avto = form.getfirst("avto", "не задано")
fio = html.escape(fio)
pol = html.escape(pol)
edu = html.escape(edu)
avto = html.escape(avto)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("{}, cпасибо за заполнение анкеты.<br>".format(fio))
print("Вы указали следующие данные: <br>")
print("Образование {}, пол: {}.<br>".format(edu.lower(),pol.lower()))

if avto=="ON":
    print("Имеется автомобиль. <br>")

print("""</body>
        </html>""")

