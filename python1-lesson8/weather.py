# coding: utf-8

import os
import csv
import json
import sqlite3
import requests

api_app_id = '1390230d256a568a0bdf22e7dbce8c87'
api_get_url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'
db_filename = 'weather.db'
csv.register_dialect('ru-excel', delimiter=';', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)

with open('city.list.json', 'r', encoding='UTF-8') as f:
    cities = json.load(f)

if not os.path.exists(db_filename):
    with sqlite3.connect(db_filename) as conn:
        conn.execute("""
            create table city (
                id          integer primary key,
                name        varchar(255),
                weather     varchar(255),
                temp        real,
                up_date     date
            );
            """)

operation = ''
while operation != 'q':
    print('\nДоступные действия:')
    print('1. Узнать погоду в городе')
    print('2. Экспортировать историю')
    operation = input("Что делаем? (номер / q) - ")

    if operation == '1':
        country_city = input("Название города [RU:Moscow] - ")
        if not country_city:
            country_city = 'RU:Moscow'
        country = country_city.split(':')[0]
        city_name = country_city.split(':')[1]

        for city in cities:
            if city["country"] == country and city["name"] == city_name:
                s = requests.get(api_get_url.format(str(city["id"]), api_app_id))
                city_info = eval(s.text)
                print('Температура: {}; Погода: {}.'.format(city_info["main"]["temp"], city_info["weather"][0]["main"]))

                with sqlite3.connect(db_filename) as conn:
                    conn.execute("""update city 
                                    set weather = ?, temp = ?, up_date = datetime(?, 'unixepoch', 'localtime')
                                    where id = ?;""", (
                        city_info["weather"][0]["main"],
                        city_info["main"]["temp"],
                        city_info["dt"],
                        city_info["id"]))
                    conn.execute("""insert or ignore into city (id, name, weather, temp, up_date) 
                                    VALUES (?,?,?,?,datetime(?, 'unixepoch', 'localtime'));""", (
                        city_info["id"],
                        city_info["name"],
                        city_info["weather"][0]["main"],
                        city_info["main"]["temp"],
                        city_info["dt"]))

                    cur = conn.cursor()
                    cur.execute("select * from city")
                    for row in cur.fetchall():
                        print(row)

    elif operation == '2':
        encoding = 'windows-1251'
        with open('history.csv', 'w', encoding=encoding) as csvfile:
            writer = csv.writer(csvfile, dialect='ru-excel')
            writer.writerow(('ID Города', 'Город', 'Погода', 'Температура', 'Последнее обновление'))
            with sqlite3.connect(db_filename) as conn:
                cur = conn.cursor()
                cur.execute("select * from city")
                for row in cur.fetchall():
                    print(row)
                    writer.writerow(row)

    else:
        print('Неизвестное действие')
