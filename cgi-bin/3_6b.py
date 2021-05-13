#!/usr/bin/env python3

import cgi
import html
#from cv2 import imread,imshow,waitKey

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
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
form = cgi.FieldStorage()
k = form.getfirst("k", "не задано")
k=istochka(k)
k = html.escape(istochka(k))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>""")

if is_digit(k)==True and float(k)>0 and float(k)==int(k):
    k=int(k)
    sum = 0
    for i in range(1, k + 1):
        sum+= (-1)**(3*i-1)/fac(4*i+4)
    print("Сумма {} членов последовательности: {} ".format(k, sum))
    #img = imread('1.png', 0)
    #imshow('', img)
    #waitKey(0)


else:
    print("Ошибка. Повторите ввод")
