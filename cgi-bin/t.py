#!/usr/bin/env python3

import cgi
import html


def sun(z, x, c, v):
    return z + x + c + v


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def sr(z, x, c, v):
    return (z + x + c + v) / 4


form = cgi.FieldStorage()

fio = []
k = []
F = []
M = []
A = []
Mx = []
i = 0
r = True
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>Обработка данных форм</title>
          </head>
          <body>""")
# print(form)
while r:
    st = str("name[" + str(i) + "]")
    fio.append(html.escape(str(form.getfirst(st, "не задано"))))
    if fio[i] != "не задано":
        i += 1
    else:
        r = False
        fio.pop()
i = 0
r = True
while r:
    st = str("k[" + str(i) + "]")
    k.append(html.escape(str(form.getfirst(st, "не задано"))))

    if k[i] != "не задано":
        i += 1
    else:
        r = False
        if i > 0:
            k.pop()
i = 0
r = True
while r:
    st = str("F[" + str(i) + "]")
    F.append(html.escape(str(form.getfirst(st, "не задано"))))
    if F[i] != "не задано":
        i += 1
    else:
        r = False
        if i > 0:
            F.pop()
i = 0
r = True
while r:
    st = str("M[" + str(i) + "]")
    M.append(html.escape(str(form.getfirst(st, "не задано"))))
    if M[i] != "не задано":
        i += 1
    else:
        r = False
        if i > 0:
            M.pop()
i = 0
r = True
while r:
    st = str("A[" + str(i) + "]")
    A.append(html.escape(str(form.getfirst(st, "не задано"))))
    if A[i] != "не задано":
        i += 1
    else:
        r = False
        if i > 0:
            A.pop()
i = 0
r = True
while r:
    st = str("Mx[" + str(i) + "]")
    Mx.append(html.escape(str(form.getfirst(st, "не задано"))))
    if Mx[i] != "не задано":
        i += 1
    else:
        r = False
        if i > 0:
            Mx.pop()
flag = 0
och = 0
maxx = 0
i = 0
for j in range(0, len(F)):
    F[j] = int(F[j])
    M[j] = int(M[j])
    A[j] = int(A[j])
    Mx[j] = int(Mx[j])
    if len(k)!=len(fio):
        och = 1
    else:
        if is_digit(k[j]) == False or int(k[j]) != float(k[j]):
            och = 1
    if len(F)!=len(fio):
        och = 1
    else:
        if len(fio[j])==0 :
            och = 1
            print(fio)
        else:
            a = fio[j].split(" ")
            a = ''.join(str(i) for i in a)
                #print(a)
            if a.isalpha() == False:
                och = 1
            #print(fio)

for i in range(0, len(F)):
    if maxx < (sun(F[i], M[i], A[i], Mx[i])):
        maxx = (sun(F[i], M[i], A[i], Mx[i]))
        flag = i
        # print(flag)
# print (fio[flag])
if och == 1:
    print("ошибка в данных")
else:
    # print(fio[flag])
    print("{} - лучший студент {} курса.<br>".format(fio[flag], k[flag]))
    print("Он имеет следующие оценки: <br>")
    print("Физика: {};<br> Мат. анализ: {};<br> Алгебра: {};<br> Механика: {},<br>"
          .format(F[flag], M[flag], A[flag], Mx[flag]))
    print("Средний бал: ", sr(F[flag], M[flag], A[flag], Mx[flag]))
# fio = html.escape(fio)
# k = html.escape(k)
# data = html.escape(data)


# print(fio,k,F,M,A,Mx)
