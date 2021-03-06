from flask import Flask, render_template, request,jsonify
import sqlite3 as sql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    return jsonify("records.html", rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
