from flask import Flask, request,jsonify
import sqlite3 as sql
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "secret key"
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def dbase_tables():
    con = sql.connect('database.db')
    print ("Opened database successfully")
    con.execute('CREATE TABLE IF NOT EXISTS Users (name TEXT, surname TEXT, email TEXT, contact TEXT)')
    print ("Table created successfully")
    con.execute('CREATE TABLE IF NOT EXISTS Admin (adm_name TEXT, adm_surname TEXT, adm_email TEXT, adm_pass TEXT)')
    print ("Table created successfully")
    con.execute('CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, prod_type TEXT, title TEXT, description TEXT, price TEXT, availability TEXT, image TEXT)')
    print ("Table created successfully")

    con.close()
dbase_tables()
#########################################################################################################################################################
def create():
    with sql.connect('database.db') as con:
        con.row_factory = dict_factory
        cur = con.cursor()
        # FIRST ROW OF ITEMS
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Machine','Tattoo Machine', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R1000.00', 'Out of Stock','https://i.postimg.cc/mkcLSxcW/machine.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Machine','Tattoo Machine', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R1150.00', 'Out of Stock','https://i.postimg.cc/X7C1yVjc/machine-power.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Needles','Tattoo Needles', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R500.00', 'Out of Stock','https://i.postimg.cc/Zq7XxV1r/needles1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Needles','Tattoo Needles', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R700.00', 'Available','https://i.postimg.cc/6qRSwwT0/needles3.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Full Kit','Tattoo Kit', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R2500.00', 'Out of Stock','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))

        # SECOND ROW OF ITEMS
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Ink','Tattoo Ink', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R150.00', 'Out of Stock','https://i.postimg.cc/D0jWvVDS/tat-equip2.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R2200.00', 'Out of Stock','https://i.postimg.cc/qRmBnsGY/tattoo-kit2.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Ink','Tattoo Ink', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R500.00', 'Out of Stock','https://i.postimg.cc/D0jWvVDS/tat-equip2.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R900.00', 'Out of Stock','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Needles','Tattoo Needles', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R100.00', 'Available','https://i.postimg.cc/6qRSwwT0/needles3.jpg'))

        # THE LAST ROW OF ITEMS
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Needles','Tattoo Needles', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R300.00', 'Out of Stock','https://i.postimg.cc/6qRSwwT0/needles3.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R4000.00', 'Available','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Needles','Tattoo Needles', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R150.00', 'Available','https://i.postimg.cc/6qRSwwT0/needles3.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R300.00', 'Available','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Ink','Tattoo Ink', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R200.00', 'Out of Stock','https://i.postimg.cc/D0jWvVDS/tat-equip2.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply .', 'R5000.00', 'Available','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R300.00', 'Available','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply .', 'R5000.00', 'Available','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Needles','Tattoo Needles', 'Lorem Ipsum is simply dummy text.', 'R550.00', 'Out of Stock','https://i.postimg.cc/Zq7XxV1r/needles1.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Machine','Tattoo Machine', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'R1150.00', 'Out of Stock','https://i.postimg.cc/X7C1yVjc/machine-power.jpg'))
        cur.execute("INSERT INTO Products (id, prod_type, title, description, price, availability, image) VALUES (?, ?, ?, ?,?,?)", ('Kit','Tattoo Kit', 'Lorem Ipsum is simply .', 'R5000.00', 'Available','https://i.postimg.cc/8C0n6s64/tat-equip1.jpg'))

        con.commit()

        items = cur.fetchall()
        print(items)

        create()
##############################################################################################################################################################################################################
# FOR USER
#check if user in database just by diplaying the data from database and checking if in\
@app.route('/userdata/', methods=['GET'])
def check_users():
    with sql.connect("database.db") as con:
        con.row_factory= dict_factory
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Users")
        data = cursor.fetchall()
        print(data)
        return jsonify(data)

@app.route('/adduser/', methods=['POST'])
def add_new_record():
    if request.method == "POST":
        msg = None
        try:
            post_data = request.get_json()
            name = post_data['name']
            sur = post_data['surname']
            email = post_data['email']
            cont = post_data['contact']
            data = name, sur, email, cont
            print(data)

            with sql.connect('database.db') as con:
                con.row_factory = dict_factory
                cur = con.cursor()
                cur.execute("INSERT INTO Users (name, surname, email, contact) VALUES (?, ?, ?, ?)", (name, sur, email, cont))
                con.commit()
                msg = "User "+name+" successfully added."
                print(msg)

        except Exception as e:
                con.rollback()
                msg = "Error occurred in insert operation: " + str(e)
        finally:
            con.close()
            return jsonify(msg = msg)

# ************************************************************************************************************************************************************
# THIS WILL BE THE ADMIN SECTION
# ADMIN
# CHECKING FOR THE ADMIN DATA
@app.route('/admindata/', methods=['GET'])
def check_admin():
    with sql.connect("database.db") as con:
        con.row_factory= dict_factory
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Admin")
        data = cursor.fetchall()
        print(data)
        return jsonify(data)

@app.route('/addadmin/', methods=['POST'])
def add_new_admin():
    if request.method == "POST":
        msg = None
        try:
            post_data = request.get_json()
            nm = post_data['adm_name']
            sur = post_data['adm_surname']
            ad_mail = post_data['adm_email']
            passw = post_data['adm_pass']
            data = nm, sur, ad_mail, passw
            print(data)

            with sql.connect('database.db') as con:
                con.row_factory = dict_factory
                cur = con.cursor()
                cur.execute("INSERT INTO Admin (adm_name, adm_surname, adm_email, adm_pass) VALUES (?, ?, ?, ?)", (nm, sur, ad_mail, passw))
                con.commit()
                msg = "Admin "+nm+" successfully added."
                print(msg)

        except Exception as e:
                con.rollback()
                msg = "Error occurred in insert operation: " + str(e)
        finally:
            con.close()
            return jsonify(msg = msg)
# **********************************************************************************************************************************************************
# TABLES FOR THE PRODUCT
# @app.route('/prods/', methods=['POST'])
# create products table


@app.route('/viewprods/', methods=['GET'])
def view_prod():
    with sql.connect("database.db") as con:
        con.row_factory= dict_factory
        cur = con.cursor()
        cur.execute("SELECT * FROM Products")
        items = cur.fetchall()
        print(items)
        return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
