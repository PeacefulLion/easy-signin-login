from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import errorcode


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', (username,))
    values = cursor.fetchall()
    try:
        if password==values[0][1]:
        	return render_template('signin-ok.html', username=username) 
    except:
        return render_template('form.html', message='Bad username or password', username=username)
    else:
    	return render_template('form.html', message='Bad username or password', username=username)
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('formfl.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    cursor.execute('insert into user (id, name) values (%s, %s)', [username, password])
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('form.html')
    #if username=='admin' and password=='password':
        #return render_template('signin-ok.html', username=username)

    #return render_template('form.html', message='Bad username or password', username=username)
if __name__ == '__main__':
    app.run()