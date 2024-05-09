from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


mysql_host = '172.17.0.2'
mysql_user = 'davi'
mysql_password = 'davi'
mysql_database = 'newsletter'


conn = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fotos')
def fotos():
    return render_template('fotos.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/novidade')
def novidade():
    return render_template('novidade.html')


@app.route('/inscrever', methods=['POST'])
def inscrever():
    email = request.form['email']

    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO newsletter (email) VALUES (%s)", (email,))
    conn.commit()
    cursor.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
