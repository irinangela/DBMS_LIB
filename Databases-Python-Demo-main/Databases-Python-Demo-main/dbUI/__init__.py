## This file is ran automatically the first time a Python program imports the package dbdemo
from flask import Flask
from flask_mysqldb import MySQL
from dbUI.login import login
from dbUI.signup import signup
from dbUI.student import student
from dbUI.teacher import teacher
from dbUI.operator import operator
from dbUI.book import book
from dbUI.bookinfo import bookinfo
from dbUI.reviews import review

## __name__ is the name of the module. When running directly from python, it will be 'dbdemo'
## Outside of this module, as in run.py, it is '__main__' by default
## Create an instance of the Flask class to be used for request routing
app = Flask(__name__)

## configuration of database

app.config["MYSQL_USER"] = 'root'
##app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'library'
app.config["MYSQL_HOST"] = 'localhost'
app.config["SECRET_KEY"] = 'key' ## secret key for sessions (signed cookies). Flask uses it to protect the contents of the user session against tampering.
app.config["WTF_CSRF_SECRET_KEY"] = 'key' ## token for csrf protection of forms.
## secret keys can be generated by secrets.token_hex()

## initialize database connection object
db = MySQL(app)

## routes must be imported after the app object has been initialized
from dbUI import routes
from dbUI.login import routes
from dbUI.signup import routes
from dbUI.student import routes
from dbUI.teacher import routes
from dbUI.operator import routes
from dbUI.book import routes
from dbUI.bookinfo import routes
##from dbUI.reviews import routes
app.register_blueprint(login)
app.register_blueprint(signup)
app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(book)
app.register_blueprint(bookinfo)
app.register_blueprint(review)
app.register_blueprint(operator)
