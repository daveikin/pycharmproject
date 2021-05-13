#!/usr/bin/env python3

import cgi
import html

def is_digit(string):
  if string.isdigit():
    return True
  else:
    try:
      float(string)
      return True
    except ValueError:
      return False
def istochka(a):
  a = a.split(".")
  a = ','.join(str(i) for i in a)
  return a
form = cgi.FieldStorage()
a = form.getfirst("a", "не задано")
b = form.getfirst("b", "не задано")
task = form.getfirst("task", "не задано")
a = html.escape(istochka(a))
b = html.escape(istochka(b))
mass=[]
task = int(html.escape(task))
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>Обработка данных форм</title>
          </head>
          <body>""")
if is_digit(a)==True and is_digit(b)==True and int(a)==float(a)and int(b)==float(b):
    a=int(a)
    b=int(b)
    if a>b:
        print("Конечное значение отрезка должно быть больше или равно начальному. Повторите ввод.")
    else:
        print("Спасибо за заполнение данных<br>")
        j=0
        if task==1:
            for i in range(a,b+1):
                mass.append(i**2)
            for i in range(0, len(mass)):
                print(i,"элемент массива=",mass[i],"<br>")
        elif task==2:
            for i in range(a, b + 1):
                mass.append(2*i)
            for i in range(0, len(mass)):
                print(i, "элемент массива=", mass[i], "<br>")
else:
    print("Ошибка. Повторите ввод")



