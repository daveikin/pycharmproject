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
def openf():
    vf1 = open('D:/veikin1.txt', 'r', encoding='utf-8')
    vf2 = open('D:/veikin2.txt', 'r', encoding='utf-8')
    return vf1,vf2
def closef(vf1,vf2):
    vf1.close()
    vf2.close()
    return 1
def readf(vf1,vf2):
    vr1 = vf1.read()
    vr2 = vf2.read()
    print("Файл 1: {}<br>".format(vr1))
    print("Файл 2: {}<br>".format(vr2))
    return 1
def writef(s):
    vw1 = open('D:/veikin1.txt', 'w', encoding='utf-8')
    vw2 = open('D:/veikin2.txt', 'w', encoding='utf-8')
    vw1.write(s)
    vw1.close()
    vw2.write(s)
    vw2.close()
    return 1
def writet(v1,v2,vp):
    vw1 = open('D:/veikint.txt', 'w', encoding='utf-8')
    vw1.write(str(v1)+" "+str(v2)+" "+str(vp))
    vw1.close()
    return 1
def readt():
    vt = open('D:/veikint.txt', 'r', encoding='utf-8')
    vt1,vt2,vp = vt.read().split(" ")
    vt1=int(vt1)
    vt2 = int(vt2)
    vp = int(vp)
    return vt1,vt2,vp

form = cgi.FieldStorage()
v = html.escape(form.getfirst("b1", "не задано"))
s = html.escape(form.getfirst("stroka", ""))
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>Обработка данных форм</title>
          </head>
          <body>""")

v1, v2, vp = readt()
#print(v1, v2, vp)
# print("Выберите команду")
# print("1-открыть файл")
# print("2-закрыть файл")
# print("3-прочитать файл")
# print("4-записать в файл")
# print("5-выход")
#v = input()
if is_digit(v) == True:
    v = int(v)
    if v == 1 or v == 2 or v == 3 or v == 4 or v == 5:
        if v == 1:
            if v1 == 0 and v2 == 0:
                vf1, vf2 = openf()
                v1 = 1
                v2 = 1
                writet(v1, v2, vp)
                closef(vf1, vf2)
                print("файл открыт")
            else:
                print("файл уже открыт")
        if v == 2:
            if v1 != 0 and v2 != 0:
                vf1, vf2 = openf()
                closef(vf1, vf2)
                print("файл закрыт")
                v1 = 0
                v2 = 0
                vp = 0
                writet(v1, v2, vp)
            else:
                print("файл не открыт")
        if v == 3:
            if v1 != 0 and v2 != 0:
                if vp == 0:
                    vf1, vf2 = openf()
                    readf(vf1, vf2)
                    print("файл прочитан")
                    vp = 1
                    writet(v1, v2, vp)
                    closef(vf1, vf2)
                else:
                    print("файл уже прочитан")
            else:
                print("файл не открыт")
        if v == 4:
            writef(s)
            vp = 0
            writet(v1, v2, vp)
            print("файл записан")
            vf1, vf2 = openf()
            closef(vf1, vf2)
        if v == 5:
            print("Выход")
            a = False
    else:
        print("Неверная команда")
else:
    print("Неверная команда")
#print(v1, v2, vp)