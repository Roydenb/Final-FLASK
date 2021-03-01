from flask import Flask, request,jsonify,redirect,url_for
import sqlite3 as sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def dbase_tables():
    conn = sql.connect('database.db')
    print ("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS Users (name TEXT, surname TEXT, email TEXT, contact TEXT)')
    print ("Table created successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS Admin (adm_name TEXT, adm_surname TEXT, adm_email TEXT, adm_pass TEXT)')
    print ("Table created successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS Items (full_kit TEXT, machines TEXT, needles TEXT, generators TEXT)')
    print ("Table created successfully")

    conn.close()

# FOR USER
# Route for handling the login page logic for user
@app.route('/userlogin' , methods=['POST','GET'])
def adminlogin():
    rqst_email = request.form[''] != ''
    rqst_mobile=request.form[''] != ''

    # success = None
    if request.method == 'GET':
            try:
                with sql.connect('database.db') as connect:
                    connect.row_factory = dict_factory
                    cursor = connect.cursor()
                    cursor.execute("SELECT FROM User WHERE adm_mail = '' AND adm_pass = '' "),()

            except Exception as e:
                    connect.rollback()
                    print("There was a problem login in ")

            else:
                return redirect(url_for('file:///home/user/Desktop/FLASK_APP_front/user_login.html'))
                # return jsonify(success)

@app.route('/adduser/' , methods=['POST','GET'])
def adduser():
    if request.method == 'POST':
        try:
            nm = request.form['name']
            surname = request.form['surname']
            mail = request.form['email']
            num = request.form['contact']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Users (name,surname,email,contact) VALUES (?,?,?,?)", (nm, surname, mail, num))
                con.commit()
                msg = "Record successfully added"
                return jsonify(msg)

        except:
                con.rollback()
                msg = "error in insert operation"
                return jsonify(msg)

        finally:
                con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("Select * from Users")

    list= []
    try:
        with sql.connect('database.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM Users")
            list = cursor.fetchall()
    except Exception as e:
            connect.rollback()
            print("There was an error fetching results from the database: " + str(e))
    finally:
        connect.close()
        return jsonify(list)

# ************************************************************************************************************************************************************
# THIS WILL BE THE ADMIN SECTION

# ADMIN
@app.route('/addadmin/' , methods=['POST','GET'])
def addadmin():
    if request.method == 'POST':
        try:
            # post_data = request.get_json()
            ad_nm = request.form['adm_name']
            ad_surname = request.form['adm_surname']
            ad_mail = request.form['adm_email']
            ad_pass = request.form['adm_pass']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Admin (adm_name,adm_surname,adm_email,adm_pass) VALUES (?,?,?,?)", (ad_nm, ad_surname, ad_mail, ad_pass))
                con.commit()
                msg = "Record successfully added"
                return jsonify(msg)

        except:
                con.rollback()
                msg = "error in insert operation"
                return jsonify(msg)

        finally:
                con.close()

@app.route('/adminlist')
def adminlist():
    con = sql.connect("database.db")

    cur = con.cursor()
    cur.execute("Select * from Admin")

    ad_list= []

    try:
        with sql.connect('database.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM Admin")
            ad_list = cursor.fetchall()
    except Exception as e:
            connect.rollback()
            print("There was an error fetching results from the database: " + str(e))
    finally:
        connect.close()
        return jsonify(ad_list)

if __name__ == '__main__':
    app.run(debug=True)
