from flask import Flask, render_template, json, request
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL

PEOPLE_FOLDER = os.path.join('static','styles')

app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'your_secret_key'
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
  
"""
STORED PROCEDURE FOR USERS SIGNUP

DELIMITER $$
CREATE PROCEDURE `sp_userCreate`(
        IN p_username VARCHAR(20),
        IN p_email TEXT,
        IN p_age BIGINT,
        IN p_password TEXT
    )
BEGIN
        if ( select exists (select 1 from auths_table where username = p_username) ) THEN
            select 'Username Exists !!';
        ELSE
            insert into users (
                username,
                email,
                age,
                user_password
            )
            values (
                p_username,
                p_email,
                p_age,
                p_password
            );
        END IF;
END$$
"""
