import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    conn.execute('CREATE TABLE students (name TEXT, surname TEXT, email TEXT, contact TEXT)')
    print("Table created successfully")
    conn.close()

    init_sqlite_db()

@app.route('/')
@app.route('/index/')
def enter_new_student():
    return render_template('index.html')

@app.route('/add-new-user/', methods=['POST'])
def add_new_record():
    if request.method == "POST":

        try:
            name = request.form['name']
            sur = request.form['surname']
            mail = request.form['email']
            cont = request.form['contact']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Users (name, surname, email, contact) VALUES (?, ?, ?, ?)", (name, sur, mail, cont))
                con.commit()
                msg = "Record successfully added."

        except Exception as e:
            con.rollback()
            msg = "Error occurred in insert operation: " + e
        finally:
            con.close()
            return render_template('success.html', msg=msg)


