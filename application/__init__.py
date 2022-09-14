from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import application.data.credentials as credentials
import sqlalchemy
import MySQLdb
################################

from sqlalchemy import create_engine

import sqlalchemy
import mysql.connector
import pymysql


hostname= credentials.host
dbname= credentials.dbname
uname= credentials.username
pwd= credentials.password
tableNameIE = credentials.tableNameIE

app = Flask(__name__)

app.config['SECRET_KEY'] = "JLKJJJO3IURYoiouolnojojouuoo=5y9y9youjuy952oohhbafdnoglhoho"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenseDB.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+uname+':'+pwd+'@'+hostname+'/'+dbname
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+uname+':'+pwd+'@'+hostname+'/'+dbname
#mysql://username:password@server/db


db = SQLAlchemy(app)


from application import routes