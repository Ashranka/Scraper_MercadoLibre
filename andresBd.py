import pymysql
import sqlite3
import pymysql.cursors

def get_bd_connection():
    conn = sqlite3.connect('Mercadolibre.db')
    return conn
#no use esta funcion
def create_bd():
    conn = get_bd_connection()
    conn.execute('''
            CREATE TABLE casaMercadoLibre
            ( img_url  TEXT PRIMARY KEY,
            price TEXT NOT NULL,
            title        TEXT    NOT NULL,
            address        TEXT    NOT NULL,
            city         TEXT NOT NULL,
            region TEXT    NOT NULL,
            size       TEXT   NOT NULL,
            rooms     TEXT   NOT NULL,
            url      TEXT   NOT NULL);''')

    conn.close()
#no use esta funcion
def sql_table(conn):

    cursorObj = conn.cursor()

    cursorObj.execute("CREATE TABLE casaMercadoLibre(img_url  TEXT PRIMARY KEY, price TEXT NOT NULL,title TEXT NOT NULL,address TEXT NOT NULL,city TEXT NOT NULL,region TEXT NOT NULL,size TEXT NOT NULL,roomsTEXT NOT NULL,url TEXT   NOT NULL)")
    conn.commit()

def query_execute(query, param = ""):
    bd_con = get_bd_connection()
    db_cursor = bd_con.cursor()
    if(param == ""):
        db_cursor.execute(query)
    else:
        db_cursor.execute(query,param)
    db_cursor.close()
    bd_con.commit()
    bd_con.close()

    return 1

def insert_house(house):
    query_for_insert_house = 'INSERT INTO casaMercadoLibre(img_url,price,title,address,city,region,size,rooms,url) VALUES (%s,%s,%s,%s,%s ,%s,%s,%s,%s)'
    param = (house['img_url'],house['price'],house['title'],house['address'],house['city'],house['region'],house['size'],house['rooms'],house['url'])
    query_execute(query_for_insert_house, param)
    return 1


