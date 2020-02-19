#!/usr/bin/python
import psycopg2
from flask import Flask
import json

conn = psycopg2.connect("dbname=dockertest user=dockertest password=dockertest host=postgres")
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    results = cursor.execute("""
        SELECT *
        FROM users
    """)
    return json.dumps(results.fetchall())

if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0')