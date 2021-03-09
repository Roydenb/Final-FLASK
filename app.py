from flask import Flask, request,jsonify,redirect,url_for, session
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
    conn = sql.connect('database.db')
    print ("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS Users (name TEXT, surname TEXT, email TEXT, contact TEXT)')
    print ("Table created successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS Admin (adm_name TEXT, adm_surname TEXT, adm_email TEXT, adm_pass TEXT)')
    print ("Table created successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS Products (prod_type, TEXT title TEXT, description TEXT, price TEXT, availability TEXT)')
    print ("Table created successfully")
    conn.close()
#########################################################################################################################################################
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


# ADMINS ABILITY TO VIEW THE USERS THAT REGISTERED
# @app.route('/list')
# def list():
#     con = sql.connect("database.db")
#     con.row_factory = sql.Row
#
#     cur = con.cursor()
#     cur.execute("Select * from Users")
#
#     users_list = []
#     try:
#         with sql.connect('database.db') as connect:
#             connect.row_factory = dict_factory
#             cursor = connect.cursor()
#             cursor.execute("SELECT * FROM Users")
#             users_list = cursor.fetchall()
#     except Exception as e:
#             connect.rollback()
#             print("There was an error fetching User results from the database: " + str(e))
#     finally:
#         connect.close()
#         return jsonify(users_list)

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


# ADMINS ABILITY TO VIEW THE ADMINS THAT THEY REGISTERED.
# @app.route('/adminlist/')
# def adminlist():
#     con = sql.connect("database.db")
#
#     cur = con.cursor()
#     cur.execute("Select * from Admin")
#
#     ad_list= []
#
#     try:
#         with sql.connect('database.db') as connect:
#             connect.row_factory = dict_factory
#             cursor = connect.cursor()
#             cursor.execute("SELECT * FROM Admin")
#             ad_list = cursor.fetchall()
#     except Exception as e:
#             connect.rollback()
#             print("There was an error fetching Admin results from the database: " + str(e))
#     finally:
#         connect.close()
#         return jsonify(ad_list)
# **********************************************************************************************************************************************************
# TABLES FOR THE PRODUCT
@app.route('/createprods/')
def create():
    con= sql.connect('database.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Needles','me', 'Best', 'R1050.00', 'Out of Stock'))

    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Machines','me', 'Best', 'R1050.00', 'Out of Stock'))


    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', ' Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type,title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Generators','me', 'Best', 'R1050.00', 'Available'))

    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Available'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Out of Stock'))
    cur.execute("INSERT INTO Products (product_type, title, description, price, availability) VALUES (?, ?, ?, ?,?)", ('Full kit','me', 'Best', 'R1050.00', 'Available'))

    con.commit()
create()

@app.route('/proddata', methods=['GET'])
def check_prod():
    with sql.connect("database.db") as con:
        con.row_factory= dict_factory
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Products")
        data = cursor.fetchall()
        print(data)
    return jsonify(data)

# @app.route('/adminAddProd/', methods=['POST'])
# def add_new_prod():
#     if request.method == "POST":
#         msg = None
#         try:
#             post_data = request.get_json()
#             prod_name = post_data['title']
#             prod_descrip = post_data['description']
#             price = post_data['price']
#             avail = post_data['availability']
#             data = prod_name, prod_descrip, price, avail
#             print(data)
#
#             with sql.connect('database.db') as con:
#                 con.row_factory = dict_factory
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO Products (title, description, price, availability) VALUES (?, ?, ?, ?)", (prod_name, prod_descrip, price, avail))
#                 con.commit()
#                 msg = " The "+prod_name+" product have successfully been added."
#                 print(msg)
#
#         except Exception as e:
#                 con.rollback()
#                 msg = "Problem updating the new product: " + str(e)
#         finally:
#             con.close()
#             return jsonify(msg = msg)


if __name__ == '__main__':
    app.run(debug=True)
