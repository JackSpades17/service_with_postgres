#import time
#from bs4 import BeautifulSoup
#import requests
import psycopg2
from flask import Flask

con = psycopg2.connect (
    database = "postgres",
    user = "",
    password = "",
    host = "89.169.142.196",
    port = "5432"
)

@app.route('/get')
def get_price():
    
    cur.execute('''select * from check_market_price order by id desc;''')
    sets = cur.fetchone()
    print(sets)
    return f'<h1>{sets[1]} стоит {sets[2]}</h1>'

@app.route('/update')
def update_price():
    product = 'cat/123/p/ajco-kurinoe-roskar-ekstra-so-10st-44323'
    r = requests.get(f'https://www.perekrestok.ru/{product}')
    soup = BeautifulSoup(r.text,'html.parser')
    a = soup.find('div', class_='price-card-unit-value')
    new_price = a.get_text().split()[0]
    cur.execute(f'''insert into check_market_price(product, price) values('syr', '{new_price}');''')
    con.commit()
    cur.execute('''select * from check_market_price order by id desc;''')
    sets = cur.fetchone()
    return f'<h1>Обновлено! Теперь {sets[1]} стоит {sets[2]}!</h1>'