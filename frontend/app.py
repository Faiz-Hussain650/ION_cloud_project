from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_name():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        dbname=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )
    cur = conn.cursor()
    cur.execute("SELECT name FROM users LIMIT 1;")
    name = cur.fetchone()[0]
    cur.close()
    conn.close()
    return name

@app.route("/")
def hello():
    name = get_name()
    return f"hello world, {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
