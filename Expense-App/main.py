from flask import Flask, render_template, request, redirect, session
import mysql.connector  # to connect with mysql database
import os  # for session

app = Flask(__name__)  # creating the Flask class object
app.secret_key = os.urandom(24)

# conn = mysql.connector.connect(host="localhost", user="root", password="root", database="bank")
# cursor = conn.cursor()
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': 8889,
    'database': 'flaskloginDB',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(dictionary=True)


@app.route('/')  # decorator defines the
def login():
    # return "Hello world"
    # return "<h1 style = 'color:red'> hello, this is our first flask website </h1>"
    return render_template('login.html')


@app.route('/register')
def about():
    #  return "About Page"
    return render_template('register.html')


@app.route('/home')  # decorator defines the
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')


# to validate the login details entered wrt database
# install xamp/mamp for mysql database
# launch mamp/xamp -> start apache web server and mysql database
# go to the browser -> type "http://localhost/phpmyadmin/" ---> this is database server for xamp
# http://localhost:8888/MAMP/?language=English ---> http://localhost:8888/phpMyAdmin5/ for mamp
# create database "flaskloginDB" --> crate table "users" ---> 5 columns ---> make 3 entries
# source for guide https://www.youtube.com/watch?v=nopIGY1zJE0&list=PLKnIA16_RmvYun1_5r9Fb4eQigioPB7yn&index=2
# you can check for syntax for mysql connection on http://localhost:8888/MAMP/?language=English for python

# install mysql connector by typing in terminal "pip install mysql.connector"
# import mysql.connector

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute(
        """SELECT `user_id`, `name` FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,
                                                                                                            password))
    # cursor.execute('SELECT `user_id`, `name` FROM `users`') ---> this works
    # cursor.execute("""SELECT user_id,
    # name FROM users where email like '{}' and password like '{}'""".format(email,password)) --> works
    results = cursor.fetchall()
    # return "The email is {} and the password is {}".format(email, password)
    # return results
    if len(results) > 0:
        session['user_id'] = results[0]  # you can session id stored in browser -> inspect -> Application -> cookies ->
        # session
        # return render_template('home.html')
        return redirect('/home')
    else:
        # return render_template('login.html')
        return redirect('/')


@app.route('/add_user', methods=['POST'])
def add_user():  # could be anything other than add_user()
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    cursor.execute(
        """INSERT into users (user_id,name,email,password) values (NULL,'{}','{}','{}')""".format(name, email,
                                                                                                  password))
    cnx.commit()

    cursor.execute("""select * from users where email like '{}'""".format(email))
    myuser = cursor.fetchall()
    session['user_id'] = myuser[0]

    # return "User Registered Successfully!!"
    return redirect('/home')


# cnx.close()


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
