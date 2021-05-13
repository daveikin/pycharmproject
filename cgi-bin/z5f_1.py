#!/usr/bin/env python3

import cgi
import html
import pymysql
from sqlalchemy import create_engine
import pandas as pd

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
b1=html.escape(form.getfirst("b1", "не задано"))
if b1=="не задано":
  vendorpc=html.escape(istochka(form.getfirst("vendorpc", "не задано")))
  model_namepc=html.escape(istochka(form.getfirst("model_namepc", "не задано")))
  cpu_corepc=html.escape(istochka(form.getfirst("cpu_corepc", "не задано")))
  cpu_speedpc=html.escape(istochka(form.getfirst("cpu_speedpc", "не задано")))
  rampc=html.escape(istochka(form.getfirst("rampc", "не задано")))
  hdd_sizepc=html.escape(istochka(form.getfirst("hdd_sizepc", "не задано")))
  prizepc=html.escape(istochka(form.getfirst("prizepc", "не задано")))

  vendorsm=html.escape(istochka(form.getfirst("vendorsm", "не задано")))
  model_namesm=html.escape(istochka(form.getfirst("model_namesm", "не задано")))
  cpu_coresm=html.escape(istochka(form.getfirst("cpu_coresm", "не задано")))
  cpu_speedsm=html.escape(istochka(form.getfirst("cpu_speedsm", "не задано")))
  flash_sizesm=html.escape(istochka(form.getfirst("flash_sizesm", "не задано")))
  ossm=html.escape(istochka(form.getfirst("ossm", "не задано")))
  ltesm=html.escape(istochka(form.getfirst("ltesm", "не задано")))
  screen_sizesm=html.escape(istochka(form.getfirst("screen_sizesm", "не задано")))
  prizesm=html.escape(istochka(form.getfirst("prizesm", "не задано")))

  vendorn=html.escape(istochka(form.getfirst("vendorn", "не задано")))
  model_namen=html.escape(istochka(form.getfirst("model_namen", "не задано")))
  cpu_coren=html.escape(istochka(form.getfirst("cpu_coren", "не задано")))
  cpu_speedn=html.escape(istochka(form.getfirst("cpu_speedn", "не задано")))
  hdd_type=html.escape(istochka(form.getfirst("hdd_type", "не задано")))
  hdd_sizen=html.escape(istochka(form.getfirst("hdd_sizen", "не задано")))
  screen_sizen=html.escape(istochka(form.getfirst("screen_sizen", "не задано")))
  prizen=html.escape(istochka(form.getfirst("prizen", "не задано")))

  print("Content-type: text/html\n")
  print("""<!DOCTYPE HTML>
           <html>
           <head>
               <meta charset="utf-8">
               <title>Обработка данных форм</title>
           </head>
           <body>""")
  if ltesm!="не задано":
    if vendorsm!="не задано" and model_namesm!="не задано"and cpu_coresm!="не задано"and cpu_speedsm!="не задано"and \
    flash_sizesm!="не задано"and ossm!="не задано"and screen_sizesm!="не задано"and prizesm!="не задано"and \
    is_digit(cpu_coresm) == True and float(cpu_coresm) > 0 and is_digit(cpu_speedsm) == True and float(cpu_speedsm) > 0 and \
    is_digit(flash_sizesm) == True and float(flash_sizesm) > 0 and is_digit(screen_sizesm) == True and float(screen_sizesm) > 0 and \
    is_digit(prizesm) == True and float(prizesm) > 0:
      print("Данные записаны")
      basess = pymysql.connect('localhost', 'user1', 'password', 'it')

      cur = basess.cursor()
      t="smartphone"
      if ltesm=="ON":
        lte=1
      else:
        lte=0
      cur.execute(f"insert into product values('{vendorsm}', '{model_namesm}','{t}')")
      cur.execute(f"insert into smartphone values('{model_namesm}', '{int(cpu_coresm)}','{int(cpu_speedsm)}','{int(flash_sizesm)}','{ossm}','{lte}','{float(screen_sizesm)}','{int(prizesm)}')")
      cur.close()
      basess.commit()
    else:
      print("Ошибка в данных")
  elif hdd_type!="не задано":
    if vendorn!="не задано" and model_namen!="не задано"and cpu_coren!="не задано"and cpu_speedn!="не задано"and \
    hdd_sizen!="не задано"and screen_sizen!="не задано"and prizen!="не задано"and \
    is_digit(cpu_coren) == True and float(cpu_coren) > 0 and is_digit(cpu_speedn) == True and float(cpu_speedn) > 0 and \
    is_digit(hdd_sizen) == True and float(hdd_sizen) > 0 and is_digit(screen_sizen) == True and float(screen_sizen) > 0 and \
    is_digit(prizen) == True and float(prizen) > 0:
      print("Данные записаны")
      basess = pymysql.connect('localhost', 'user1', 'password', 'it')
      cur = basess.cursor()
      t = "notebook"
      cur.execute(f"insert into product values('{vendorn}', '{model_namen}','{t}')")
      cur.execute(
        f"insert into notebook values('{model_namen}', '{int(cpu_coren)}','{int(cpu_speedn)}','{hdd_type}','{int(hdd_sizen)}','{float(screen_sizen)}','{int(prizen)}')")
      cur.close()
      basess.commit()
    else:
      print("Ошибка в данных")
  else:
    if vendorpc!="не задано" and model_namepc!="не задано"and cpu_corepc!="не задано"and cpu_speedpc!="не задано"and \
    rampc!="не задано"and hdd_sizepc!="не задано"and prizepc!="не задано"and \
    is_digit(cpu_corepc) == True and float(cpu_corepc) > 0 and is_digit(cpu_speedpc) == True and float(cpu_speedpc) > 0 and \
    is_digit(rampc) == True and float(rampc) > 0 and is_digit(hdd_sizepc) == True and float(hdd_sizepc) > 0 and \
    is_digit(prizepc) == True and float(prizepc) > 0:
      print("Данные записаны")
      basess = pymysql.connect('localhost', 'user1', 'password', 'it')
      cur = basess.cursor()
      t = "pc"
      cur.execute(f"insert into product values('{vendorpc}', '{model_namepc}','{t}')")
      cpu_corepc=int(cpu_corepc)
      cpu_speedpc=int(cpu_speedpc)
      rampc=int(rampc)
      hdd_sizepc=float(hdd_sizepc)
      prizepc=int(prizepc)
      cur.execute(f"insert into pc values('{model_namepc}', '{cpu_corepc}','{cpu_speedpc}','{rampc}','{hdd_sizepc}','{prizepc}')")
      cur.close()
      basess.commit()
    else:
      print("Ошибка в данных")
else:
  if int(b1)==4:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
              <html>
              <head>
                  <meta charset="utf-8">
                  <title>Обработка данных форм</title>
                  <style>
              H1 {
              font-size: 120%;
              font-family: Verdana, Arial, Helvetica, sans-serif;
              color: #338366;
              }
              </style>
              </head>
              <body>""")

    db_connection = 'mysql+pymysql://user1:password@localhost/it'
    conn = create_engine(db_connection)
    '''
    df = pd.read_sql("SELECT * FROM product", conn)
    #print(df)
  
    df1 = pd.DataFrame.from_dict(df)
    print("<h1>Продукты:</h1>")
    print(df1.to_html())
  
    df = pd.read_sql("SELECT * FROM pc", conn)
    # print(df)
  
    df1 = pd.DataFrame.from_dict(df)
    print("<h1>Компьютеры:</h1>")
    print(df1.to_html())
    df = pd.read_sql("SELECT * FROM smartphone", conn)
    # print(df)
  
    df1 = pd.DataFrame.from_dict(df)
    print("<h1>Смартфоны:</h1>")
    print(df1.to_html())
    df = pd.read_sql("SELECT * FROM notebook", conn)
    # print(df)
  
    df1 = pd.DataFrame.from_dict(df)
    print("<h1>Ноутбуки:</h1>")
    print(df1.to_html())
    '''
    a = pd.read_sql("SHOW TABLES", conn)
    print(f"<h1>Имеющееся таблицы в базе данных:</h1>")
    for i in range(0, a.shape[0]):
      #print(a.iloc[i, 0])

      df = pd.read_sql(f"SELECT * FROM {a.iloc[i, 0]}", conn)

      # print(df)

      df1 = pd.DataFrame.from_dict(df)
      print(f"<h1>{i+1}) {a.iloc[i, 0]}</h1>")
      print(df1.to_html())
  elif int(b1)==2:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                  <html>
                  <head>
                      <meta charset="utf-8">
                      <title>Обработка данных форм</title>
                      <style>
                  H1 {
                  font-size: 120%;
                  font-family: Verdana, Arial, Helvetica, sans-serif;
                  color: #338366;
                  }
                  </style>
                  </head>
                  <body>""")

    db_connection = 'mysql+pymysql://user1:password@localhost/it'
    conn = create_engine(db_connection)

    df = pd.read_sql("SELECT * FROM pc", conn)
    # print(df)

    df1 = pd.DataFrame.from_dict(df)
    df2=df1.sort_values('price',ascending=True)
    print("<h1>Компьютеры:</h1>")
    print(df2.to_html())
    df = pd.read_sql("SELECT * FROM smartphone", conn)
    # print(df)

    df1 = pd.DataFrame.from_dict(df)
    df2 = df1.sort_values('price', ascending=True)
    print("<h1>Смартфоны:</h1>")
    print(df2.to_html())
    df = pd.read_sql("SELECT * FROM notebook", conn)
    # print(df)

    df1 = pd.DataFrame.from_dict(df)
    df2 = df1.sort_values('price', ascending=True)
    print("<h1>Ноутбуки:</h1>")
    print(df2.to_html())
