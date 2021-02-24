from flask import Flask, render_template, request,jsonify
import sqlite3 as sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# @app.route('/')
# def newuser():
#     return render_template('index.html')

def dbase_tables():
    conn = sql.connect('database.db')
    print ("Opened database successfully")

    conn.execute('CREATE TABLE Users (name TEXT, surname TEXT, email TEXT, contact TEXT)')
    print ("Table created successfully")
    conn.execute('CREATE TABLE Admin (admin_name TEXT, admin_surname TEXT, admin_email TEXT, admin_password TEXT)')
    print ("Table created successfully")
    conn.execute('CREATE TABLE items (full-kit TEXT, machines TEXT, needles TEXT, generators TEXT)')
    print ("Table created successfully")

    conn.close()

# FOR USER
# @app.route('/adduser/', methods=['POST', 'GET'])
# def adduser():
#     if request.method == 'POST':
#         try:
#             nm = request.form['name']
#             surname = request.form['surname']
#             mail = request.form['email']
#             num = request.form['contact']
#
#             with sql.connect("database.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO Users (name,surname,email,contact) VALUES (?,?,?,?)", (nm, surname, mail, num))
#                 con.commit()
#                 msg = "Record successfully added"
#         except:
#                 con.rollback()
#                 msg = "error in insert operation"
#
#         finally:
#                 return render_template("success.html", msg=msg)
#                 con.close()
#
# @app.route('/list')
# def list():
#     con = sql.connect("database.db")
#     con.row_factory = sql.Row
#
#     cur = con.cursor()
#     cur.execute("select * from Users")
#
#     list= []
#     try:
#         with sql.connect('database.db') as connect:
#             connect.row_factory = dict_factory
#             cursor = connect.cursor()
#             cursor.execute("SELECT * FROM Users")
#             list = cursor.fetchall()
#     except Exception as e:
#             connect.rollback()
#             print("There was an error fetching results from the database: " + str(e))
#     finally:
#         connect.close()
#         return jsonify(list)

# ************************************************************************************************************************************************************
# THIS WILL BE THE ADMIN SECTION
@app.route('/')
def newadmin():
    return render_template('admin.html')

# ADMIN
@app.route('/addadmin/', methods=['POST', 'GET'])
def addadmin():
    if request.method == 'POST':
        try:
            a_nm = request.form['admin-name']
            a_surname = request.form['admin-surname']
            a_mail = request.form['admin-email']
            admin_pass = request.form['admin-password']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Admin (admin-name,admin-surname,admin-email,admin-password) VALUES (?,?,?,?)", (a_nm, a_surname, a_mail, admin_pass))
                con.commit()
                msg = "Record successfully added"
        except:
                con.rollback()
                msg = "error in insert operation"

        finally:
                return render_template("admin-success.html", msg=msg)
                con.close()

@app.route('/admin-list')
def ad_list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Users")

    admin_list= []
    try:
        with sql.connect('database.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM Admin")
            admin_list = cursor.fetchall()
    except Exception as e:
            connect.rollback()
            print("There was an error fetching results from the database: " + str(e))
    finally:
        connect.close()
        return jsonify(admin_list)

if __name__ == '__main__':
    app.run(debug=True)
