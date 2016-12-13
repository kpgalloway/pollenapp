#/usr/bin/env python3

import xml.etree.ElementTree as et
import sqlite3
import requests
import datetime

xmldoc = requests.get('http://www.fmhdc.com/etc/pollendata/counts.xml').text


root = et.fromstring(xmldoc)

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
sql_statement_template = '''INSERT INTO pollen_counts_pollencounts (%s) VALUES(%s)'''

for child in root.findall('./pollendata'):
    record = {}
    for d in child.findall('./*'):
        try:
            record[d.tag] = float(d.text)
        except:
            record[d.tag] = d.text
    datetime_string = record['date'] + " " + record['time']
    print(datetime_string)
    print(datetime.datetime.strptime(datetime_string, r'%m/%d/%Y %I:%M %p').isoformat())
    record['datetime'] = datetime.datetime.strptime(datetime_string, r'%m/%d/%Y %I:%M %p').isoformat()
    del record['date']
    del record['time']
    
    columns = ', '.join(record.keys())
    placeholders = ':' + ', :'.join(record.keys())
    sql = sql_statement_template % (columns, placeholders)
    cur.execute(sql, record)
    conn.commit()
