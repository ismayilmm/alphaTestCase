from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = request.remote_addr

    conn = psycopg2.connect(
        host='postgres-postgresql',
        port=5432,
        user='postgres',
        password='password',
        database='mydatabase'
    )

    cursor = conn.cursor()

    cursor.execute("INSERT INTO mytable (ip_address) VALUES (%s)", (ip_address,))
    conn.commit()

    cursor.close()
    conn.close()

    return 'IP address recorded: {}'.format(ip_address)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

