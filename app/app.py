import os
import psycopg2
from flask import Flask, request

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )
    return conn


@app.route('/')
def index():
    """Главная страница, отображающая счетчик посещений."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, count INTEGER);')

        cur.execute('SELECT count FROM visits;')
        if cur.fetchone() is None:
            cur.execute('INSERT INTO visits (count) VALUES (0);')

        cur.execute('UPDATE visits SET count = count + 1 RETURNING count;')
        count = cur.fetchone()[0]

        conn.commit()
        cur.close()
        conn.close()

        return f"""
        <h1>Привет из Kubernetes!</h1>
        <p>Количество посещений: {count}</p>
        """
    except Exception as e:
        return f"<h1>Ошибка подключения к базе данных</h1><p>{e}</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)