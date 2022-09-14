from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import application.data.credentials as credentials
import sqlalchemy
import MySQLdb
################################

from sqlalchemy import create_engine

import sqlalchemy
import mysql.connector


hostname= credentials.host
dbname= credentials.dbname
uname= credentials.username
pwd= credentials.password
tableNameIE = credentials.tableNameIE

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+uname+':'+pwd+'@'+hostname+'/'+dbname



db = SQLAlchemy(app)


from application import routes