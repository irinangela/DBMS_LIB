from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from dbUI import app, db ## initially created by __init__.py, need to be used here

@app.route("/")
def index():
        query = "CALL check_reserves();"
        try:
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
        except Exception as e: ## OperationalError
            flash("Something wrong with reserves", "danger")   
             
        return render_template("landing.html", pageTitle = "Landing Page")
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("errors/404.html", pageTitle = "Not Found"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html", pageTitle = "Internal Server Error"), 500
