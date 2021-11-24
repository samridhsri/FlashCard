import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from flask import Flask
from flask.app import Flask
from flask.templating import render_template
from flask import request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def homepage():
    if request.method=='POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()
        username = request.form['username']
        password = request.form['password']

        print(username, password)
    return render_template("homepage.html")

@app.route("/register.html",methods=["GET","POST"])
def register():
    if request.method=='POST':
        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()
        username = request.form['new_user']
        password = request.form['new_pass']
        newUserCommand = "insert into users values("+"'"+username+"'"+", '"+password+"'"+")"
        cursor.execute(newUserCommand)
        connection.commit()

# Insert into users values('Samridh', '1234')

    return render_template("register.html")
if __name__ == '__main__':
    app.debug= True
    app.run()




#functions that might come handy
