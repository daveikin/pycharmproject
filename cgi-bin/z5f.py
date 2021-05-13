#!/usr/bin/env python3

import pymysql
import cgi
import html

form = cgi.FieldStorage()
v = html.escape(form.getfirst("vendor", "не задано"))
n = html.escape(form.getfirst("name", "не задано"))
t = html.escape(form.getfirst("type", "не задано"))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
          <html>
          <head>
              <meta charset="utf-8">
              <title>Обработка данных форм</title>
          </head>
          <body>""")

basess = pymysql.connect('localhost', 'user1', 'password', 'it')
cur = basess.cursor()
cur.execute(f"insert into product values('{v}', '{n}','{t}')")

#with basess:
cur = basess.cursor()
print("Структура:")
cur.execute("DESCRIBE product")
rows = cur.fetchall()
for j in range(0, len(rows)):
    print(rows[j])
    print("\nДанные:")
cur.execute("select* from product")
rows = cur.fetchall()
for j in range(0, len(rows)):
    print(rows[j])
basess.commit()
cur.close()