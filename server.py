from flask import Flask, render_template, json, request, session, redirect, url_for
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
from __init__ import mysql_password

PEOPLE_FOLDER = os.path.join('static','styles')

app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'your_secret_key'
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = mysql_password
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('home.html')

@app.route("/verify")
def Verify_View():
    return render_template('login.html')

@app.route("/details")
def Details_View():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(port=9001)
  
"""
STORED PROCEDURE FOR USER DETAILS

DELIMITER $$
CREATE PROCEDURE `sp_userCreate`(
        IN p_username VARCHAR(20),
        IN p_email TEXT,
        IN p_age BIGINT,
        IN p_password TEXT
    )
BEGIN
        if ( select exists (select 1 from users where username = p_username) ) THEN
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
