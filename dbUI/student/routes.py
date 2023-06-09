from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_mysqldb import MySQL
from dbUI import db ## initially created by __init__.py, need to be used here
from dbUI.student import student
from dbUI.student.forms import StudentForm
from dbUI import routes
from dbUI.book import book

@student.route("/student/<string:username>")
def getStudent(username):
    try:
        cur = db.connection.cursor()
        query = "SELECT b.ISBN, b.title, bo.b_date FROM borrows bo INNER JOIN book b ON b.ISBN = bo.ISBN WHERE bo.username = '{}' AND bo.ret_date IS NULL;".format(username)
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        borrows = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        query = "SELECT b.ISBN, b.title, r.r_date FROM reserves r INNER JOIN book b ON b.ISBN = r.ISBN WHERE r.username = '{}';".format(username)
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        reserves = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        query = ("SELECT Library_card FROM approves_user WHERE username = '{}';".format(username))
        cur.execute(query)
        result = cur.fetchone()
        query = "SELECT b.ISBN, b.title, bo.b_date, bo.ret_date FROM borrows bo INNER JOIN book b ON b.isbn = bo.isbn WHERE bo.ret_date IS NOT NULL and bo.username = '{}';".format(username)
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        old_borrows = [dict(zip(column_names, entry)) for entry in cur.fetchall()] 

        if result is not None:
            library_card = result[0]
            has = 1 if library_card == 1 else 0
        else:
            has = 0
        cur.close()

        return render_template("student.html",old_borrows = old_borrows, borrows = borrows, username = username, reserves = reserves, has=has, pageTitle = "Student Page")
    except Exception as e:
        flash(str(e),"danger")
        abort(500)    

@student.route("/student/profile/<string:username>", methods=['GET', 'POST'])
def getStudentProfile(username):
    form = StudentForm()

    if(request.method == "POST" and form.validate_on_submit()):
        studentinfo = form.__dict__
        if studentinfo["first_name"].data:
            try:
                query = "UPDATE student_user SET student_first_name = '{}' WHERE Username = '{}';".format(
                    studentinfo["first_name"].data,
                    username
                    )
                cur = db.connection.cursor()
                cur.execute(query)
                db.connection.commit()
                cur.close()
            except Exception as e:
                abort(500)  

        if studentinfo["last_name"].data:
            try:
                query = "UPDATE student_user SET student_last_name = '{}' WHERE Username = '{}';".format(
                    studentinfo["last_name"].data,
                    username
                    )
                cur = db.connection.cursor()
                cur.execute(query)
                db.connection.commit()
                cur.close()
            except Exception as e:
                abort(500)  

        if studentinfo["password"].data:
            try:
                query = "UPDATE users SET U_password = '{}' WHERE Username = '{}';".format(
                    studentinfo["password"].data,
                    username
                    )
                cur = db.connection.cursor()
                cur.execute(query)
                db.connection.commit()
                cur.close()
            except Exception as e:
                abort(500)                  

    try:
        cur = db.connection.cursor()
        query = "SELECT * FROM usernameview u INNER JOIN users us ON u.username = us.username WHERE u.username = '{}';".format(username)
        cur.execute(query)
        column_names = [i[0] for i in cur.description]
        information = [dict(zip(column_names, entry)) for entry in cur.fetchall()]
        cur.close()

    except Exception as e:
        abort(500)      

    return render_template("student_profile.html", information=information[0], pageTitle="Student Profile", form = form)
    
@student.route("/student/delete/<string:username>", methods=['GET', 'POST'])
def deleteStudent(username):
    if(request.method == "POST"):
        try:
            query = "CALL delete_user('{}');".format(username)
            cur = db.connection.cursor()
            cur.execute(query)
            db.connection.commit()
            cur.close()
            return redirect(url_for("index"))
        except Exception as e:
            abort(500)  
           
        
   


