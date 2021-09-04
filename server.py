from flask import Flask, render_template, json, request
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

PEOPLE_FOLDER = os.path.join('static','styles')

app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '*********'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('home.html')

@app.route("/login")
def Login_View():
    return render_template('login.html')

@app.route("/signup")
def Signup_View():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(port=9001)