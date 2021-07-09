
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from bs4 import BeautifulSoup
import requests
import numpy as np
from datetime import datetime
import sqlite3


def get_address(data):
    part = data.split(",")
    partAmount = len(part)
    if(partAmount == 3):
        return {'address' : part[0],'city' : part[1], 'region' : part[2]}
    elif(partAmount > 3):
        return {'address' : " ".join(part[:len(part)-3]), 'city' : part[partAmount-2], 'region' : part[partAmount-1]}
    elif(partAmount < 3):
        for i in range(0,1):
            print("error:")
            print(data)
        return {'address' : 'FAIL','city' : 'FAIL', 'region' : data}

def li_html_to_obj(house_li_html): #obtenemos los objetos python

    #obtenemos url de imagen
    try:
        img_url = house_li_html.find("img")['data-src']
    except:
        img_url = house_li_html.find("img")['src']
    #sacamos el precio y le sacamos el punto
    price = house_li_html.find(class_="price-tag-fraction").text.replace(".","")

    #titulo de la publicacion
    title = house_li_html.find(class_="ui-search-item__title").text

    #obtiene dirreccion 
    address = house_li_html.find(class_="ui-search-item__location").text
    address = get_address(address)

    #obtiene tamaño y/o cantidad de habitaciones
    all_attribute = house_li_html.find_all(class_= "ui-search-card-attributes__attribute")

    size = ""
    rooms = ""
    if(len(all_attribute) > 0):
        if("útiles" in all_attribute[0].text):
            size = all_attribute[0].text
        else:
            rooms = all_attribute[0].text
    if(len(all_attribute) > 1):
        rooms = all_attribute[1].text
    #obtiene la url de la publicacion 
    url = house_li_html.find("a")["href"]
    #   Devuelce el objeto con esta data
    return{"img_url": img_url, "price": price, "title": title, 'address': address['address'],
            'city': address['city'], 'region': address['region'], "size": size, 
            "rooms": rooms, "url": url }


URL_use = "https://listado.mercadolibre.cl/inmuebles/casas/#deal_print_id=a3b5c420-dfc2-11eb-8057-19e52126f5fb&c_id=carousel&c_element_order=2&c_campaign=CASAS&c_uid=a3b5c420-dfc2-11eb-8057-19e52126f5fb"
driver = webdriver.Firefox(executable_path= 'geckodriver') #maneja el navegador en este caso firefox
driver.get(URL_use)
html_code = driver.page_source # tomo el html de la pagina  
soup = BeautifulSoup(html_code, 'lxml')#objetohtml y el parse 

    
all_house_li = soup.find_all("li", class_="ui-search-layout__item")

for house_li_html in all_house_li:
    house_obj = li_html_to_obj(house_li_html)
    print(house_obj)


# connect function opens a connection to the SQLite database file, 
conn = sqlite3.connect('Mercadolibre.db')
#Sprint(conn)
conn.execute('''
         CREATE TABLE casaMercadoLibre
         ( img_url  TEXT PRIMARY KEY,
         price INTEGER NOT NULL,
         title        TEXT    NOT NULL,
         address        TEXT    NOT NULL,
         city         TEXT NOT NULL,
         region TEXT    NOT NULL,
         size       TEXT   NOT NULL,
         rooms     TEXT   NOT NULL,
         url      TEXT   NOT NULL);''')
conn.close()
li_html_to_obj
cursorObj = conn.cursor()
cursorObj.execute('''INSERT INTO casaMercadoLibre (img_url,price,title,address,city,region,rooms,Región,url) VALUES (?,?,?,?,?,?,?,?,?)''', house_obj)
conn.commit()
