from flask import Flask, render_template, request
import sqlite3 as sql


app = Flask(__name__)


@app.route('/')
def newuser():
    return render_template('index.html')

@app.route('/')
def newadmin():
    return render_template('admin.html')

# FOR USER
@app.route('/adduser/', methods=['POST', 'GET'])
def adduser():
    if request.method == 'POST':
        try:
            nm = request.form['name']
            surname = request.form['surname']
            mail = request.form['email']
            num = request.form['contact']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                con.execute('CREATE TABLE IF NOT EXISTS Users (name TEXT, surname TEXT, email TEXT, contact TEXT)')
                cur.execute("INSERT INTO Users (name,surname,email,contact) VALUES (?,?,?,?)", (nm, surname, mail, num))
                con.commit()
                msg = "Record successfully added"


        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Users")

    rows = cur.fetchall()
    return render_template("records.html", rows=rows)

# FOR ADMIN
# FOR A ADMIN TO VIEW THE LIST
# NEED TO CREATE A BUTTON THAT GOES TO THE ADMIN
# ADMIN NEED TO HAVE A LOGIN BEFORE THEY CAN VIEW THE INFORMATION
# @app.route('/adadmin/', methods=['POST', 'GET'])
# def adduser():
#     if request.method == 'POST':
#         try:
#             a_nm = request.form['admin-name']
#             a_surname = request.form['admin-surname']
#             a_mail = request.form['admin-email']
#             a_passw = request.form['admin-password']
#
#             with sql.connect("database.db") as con:
#                 cur = con.cursor()
#                 con.execute('CREATE TABLE IF NOT EXISTS Admin (name TEXT, surname TEXT, email TEXT, contact TEXT)')
#                 cur.execute("INSERT INTO Admin (admin-name,admin-surname,admin-email,admin-password) VALUES (?,?,?,?)", (a_nm, a_surname, a_mail, a_passw))
#                 con.commit()
#                 msg = "Record successfully added"
#
#
#         except:
#             con.rollback()
#             msg = "error in insert operation"
#
#         finally:
#             return render_template("success.html", msg=msg)
#             con.close()
#
# @app.route('/list')
# def list():
#     con = sql.connect("database.db")
#     con.row_factory = sql.Row
#
#     cur = con.cursor()
#     cur.execute("select * from Users")
#
#     rows = cur.fetchall()
#     return render_template("records.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
