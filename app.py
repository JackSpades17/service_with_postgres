#import time
#from bs4 import BeautifulSoup
#import requests
import psycopg2
from flask import Flask

con = psycopg2.connect (
    database = "postgres",
    user = "test_user",
    password = "1111",
    host = "89.169.151.196",
    port = "5432"
)

cur = con.cursor()
app = Flask(__name__)

@app.route('/get')
def get_price():
    
    cur.execute('''select * from count_update order by count desc;''')
    sets = cur.fetchone()
    print(sets)
    return f'<h1>BIG is {sets[0]}</h1>'

@app.route('/update')
def update_price():
    cur.execute('''select * from count_update order by count desc;''')
    sets = cur.fetchone()
    new_item = int(sets[0]) + 1
    cur.execute(f'''insert into count_update values('{new_item}');''')
    con.commit()
    cur.execute('''select * from count_update order by count desc;''')
    sets = cur.fetchone()
    return f'<h1>Congratulations!Обновлено! BIG is {sets[0]}!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1717)

con.close()