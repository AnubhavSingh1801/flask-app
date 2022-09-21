from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_DATABASE_USER'] = 'db_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'db_password'
app.config['MYSQL_DATABASE_DB'] = 'employee_test_db'
app.config['MYSQL_DATABASE_HOST'] = '172.31.12.187'
mysql.init_app(app)


@app.route('/test')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM employee_table''')
    rv = cur.fetchall()
    return str(rv)

@app.route('/')
def main_func():
    return "Hello there!!!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)