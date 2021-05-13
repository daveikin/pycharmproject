#!/usr/bin/env python3

import cgi
import html
from math import sqrt

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
  a = a.split(",")
  a = '.'.join(str(i) for i in a)
  return a

form = cgi.FieldStorage()
lent = form.getfirst("lent", "не задано")
a = form.getfirst("a", "не задано")
b = form.getfirst("b", "не задано")
c = form.getfirst("c", "не задано")
n = form.getfirst("n", "не задано")

lent = html.escape(istochka(lent))
a = html.escape(istochka(a))
b = html.escape(istochka(b))
c = html.escape(istochka(c))
n = html.escape(istochka(n))

if lent!="не задано" and is_digit(istochka(lent))==True and float(istochka(lent))>0:
  a=float(lent)
  print("Content-type: text/html\n")
  print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>Обработка данных форм</title>
          </head>
          <body>""")
  print("Площадь равностороннего треугольника: ")
  print(round(a * a * sqrt(3) / 4, 3),"<br>")
  print("Высота равностороннего треугольника: ")
  print(round(a * sqrt(3) / 2, 3),"<br>")
  print("Радиус вписанной окружности равностороннего треугольника: ")
  print(round(a / (2 * sqrt(3)), 3),"<br>")
  print("Радиус описанной окружности равностороннего треугольника: ")
  print(round(a / sqrt(3), 3),"<br>")
elif n!="не задано" and is_digit(istochka(n))==True and float(istochka(n))>0 and float(istochka(n))==int(float(istochka(n))) :
  n=int(float(istochka(n)))

  if n>=0:
    sum = 0
    for i in range(1, n + 1):
      sum += 5 / (25 * i * i - 5 * i - 6)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>""")
    print("Сумма {} членов последовательности: {} ".format(n,sum))

    print("""</body>
          </html>""")
elif a != "не задано"and b!="не задано"and c!="не задано" and is_digit(istochka(a))==True and is_digit(istochka(b))==True \
        and is_digit(istochka(c))==True and float(istochka(a))>0 and float(istochka(b))>0 and float(istochka(c))>0:
  a = float(istochka(a))
  b=float(istochka(b))
  c=float(istochka(c))
  print("Content-type: text/html\n")
  print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>Обработка данных форм</title>
          </head>
          <body>""")
  if a + b > c and a + c > b and b + c > a:
    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
      print("Да, прямоугольный")
    elif a ** 2 > b ** 2 + c ** 2 or b ** 2 > a ** 2 + c ** 2 or c ** 2 > b ** 2 + a ** 2:
      print("Да, тупоугольный")
    else:
      print("Да, остроугольный")
  else:
    print("Нет")
else:
  print("Content-type: text/html\n")
  print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>""")
  print("Ошибка. Повторите ввод")


