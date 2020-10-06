
import MySQLdb


def test_pymysql():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='your_username',
        passwd=your_password’,
        db='mysql'
    )

    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE price (
                timestamp TIMESTAMP NOT NULL,
                BTCUSD FLOAT(8,2),
                PRIMARY KEY (timestamp)
            );
        ''')
    cur.execute('''
            INSERT INTO price VALUES(
                "2019-07-14 14:12:17",
                11234.56
            );
        ''')

    conn.commit()
    conn.close()


test_pymy




import peewee
from peewee import *

db = MySQLDatabase('mysql', user='your_username', passwd=your_password’)


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    Price.create_table()
    price = Price(timestamp='2019-06-07 13:17:18', BTCUSD='12345.67')
    price.save()


test_p