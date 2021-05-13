#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
fio = form.getfirst("fio", "не задано")
mail = form.getfirst("mail", "не задано")
pol = form.getfirst("pol", "не задано")
edu = form.getfirst("edu", "не задано")
dolgnost = form.getfirst("dolgnost", "не задано")
name = form.getfirst("name", "не задано")
doc = form.getfirst("doc", "не задано")
dis = form.getfirst("dis", "не задано")
ob = form.getfirst("ob", "не задано")
fio = html.escape(fio)
mail = html.escape(mail)
pol = html.escape(pol)
edu = html.escape(edu)
dolgnost = html.escape(dolgnost)
name = html.escape(name)
doc = html.escape(doc)
dis = html.escape(dis)
ob = html.escape(ob)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
if fio.isalpha()==False or "@"not in mail or "." not in mail:
    print("Ошибка. Повторите ввод. <br>")
else:
    print("{}, вы зарегистрировались на конференцию как {}.<br>".format(fio, dolgnost.lower()))
    print("Вы указали следующие данные: <br>")
    print("Эл.почта: {},<br> Образование {},<br> Пол: {},<br> Название доклада:{},<br> Сборник тезисов:{}"
      .format(mail,edu.lower(),pol.lower(),name,doc),end="")

    if dis == "ON":
        print(", <br>Дистанционное участие",end="")

    if ob == "ON":
        print(",<br>Требуется общежитие",end="")
    print(". <br>")

print("""</body>
        </html>""")
