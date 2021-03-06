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
    # conn.execute('CREATE TABLE IF NOT EXISTS Items (prod_name TEXT, prod_description TEXT, prod_price TEXT)')
    # print ("Table created successfully")

    conn = sql.connect('CREATE TABLE Product (id int unsigned COLLATE utf8mb4_unicode_ci NOT NULL AUTO_INCREMENT,'
	'name varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,'
	'code varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,'
	'image text COLLATE utf8mb4_unicode_ci NOT NULL,'
	'price double COLLATE utf8mb4_unicode_ci NOT NULL,'
	'PRIMARY KEY (id)')
    'ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;'
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
@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("Select * from Users")

    users_list = []
    try:
        with sql.connect('database.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM Users")
            users_list = cursor.fetchall()
    except Exception as e:
            connect.rollback()
            print("There was an error fetching User results from the database: " + str(e))
    finally:
        connect.close()
        return jsonify(users_list)

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
@app.route('/adminlist/')
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
            print("There was an error fetching Admin results from the database: " + str(e))
    finally:
        connect.close()
        return jsonify(ad_list)
# **********************************************************************************************************************************************************
# TABLES FOR THE PRODUCT
# THIS WILL ALLOW A ADMIN TO UPDATE ITEMS AND VIEW WHAT THEY UPDATED
# @app.route('/additems/' , methods=['POST','GET'])
# def additem():
#     if request.method == 'POST':
#         try:
            # post_data = request.get_json()
        #     prod_nm = request.form['prod_name']
        #     prod_descrip = request.form['prod_description']
        #     prod_price = request.form['prod_price']
        #
        #     with sql.connect("database.db") as con:
        #         cur = con.cursor()
        #         cur.execute("INSERT INTO Items (prod_name,prod_description,prod_price) VALUES (?,?,?,?)", (prod_nm, prod_descrip, prod_price))
        #         con.commit()
        #         msg = "Item successfully added"
        #         return jsonify(msg)
        #
        # except:
        #         con.rollback()
        #         msg = "error trying to update the product"
        #         return jsonify(msg)
        #
        # finally:
        #         con.close()

# ADMINS ABILITY TO VIEW THE ITEMS WAS ADDED.
# @app.route('/itemlist')
# def itemlist():
#     con = sql.connect("database.db")
#
#     cur = con.cursor()
#     cur.execute("Select * from Item")
#
#     prod_list= []
#
#     try:
#         with sql.connect('database.db') as connect:
#             connect.row_factory = dict_factory
#             cursor = connect.cursor()
#             cursor.execute("SELECT * FROM Items")
#             prod_list = cursor.fetchall()
#     except Exception as e:
#             connect.rollback()
#             print("There was an error fetching Item information from the database: " + str(e))
#     finally:
#         connect.close()
#         return jsonify(prod_list)

##########################################################################################################################################################
# NEW ITEM FUNCTION
# @app.route('/itemvalues/')
# def itemvalues():
#     con = sql.connect("database.db")
#     con.row_factory = sql.Row
#
#     cur = con.cursor()
#     cur.execute("INSERT INTO Product (id,name, code, image, price) "
#                 "VALUES(1, 'test', 'test', 'test', 'test')")
#
#
# @app.route('/add/', methods=['POST'])
# def add_product_to_cart():
#     cursor = None
#     try:
#         _quantity = int(request.form['quantity'])
#         _code = request.form['code']

        # validate the received values
        # if _quantity and _code and request.method == 'POST':
        #     with sql.connect('database.db') as conn:
        #         cursor = conn.cursor()
        #         cursor.execute("SELECT * FROM Product WHERE code=%s", _code)
        #         row = cursor.fetchone()
        #
        #         itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity' : _quantity, 'price' : row['price'], 'image' : row['image'], 'total_price': _quantity * row['price']}}
        #
        #         all_total_price = 0
        #         all_total_quantity = 0
        #
        #         session.modified = True
        #
        #     if 'cart_item' in session:
        #         if row['code'] in session['cart_item']:
        #             for key, value in session['cart_item'].items():
        #                 if row['code'] == key:
                            #session.modified = True
							#if session['cart_item'][key]['quantity'] is not None:
							#	session['cart_item'][key]['quantity'] = 0
# 							old_quantity = session['cart_item'][key]['quantity']
#                             total_quantity = old_quantity + _quantity
#                             session['cart_item'][key]['quantity'] = total_quantity
#                             session['cart_item'][key]['total_price'] = total_quantity * row['price']
#
#                         else:
#                             session['cart_item'] = array_merge(session['cart_item'], itemArray)
#                             for key, value in session['cart_item'].items():
#                                 individual_quantity = int(session['cart_item'][key]['quantity'])
#                                 individual_price = float(session['cart_item'][key]['total_price'])
#                                 all_total_quantity = all_total_quantity + individual_quantity
#                                 all_total_price = all_total_price + individual_price
#             else:
#                 session['cart_item'] = itemArray
#                 all_total_quantity = all_total_quantity + _quantity
#                 all_total_price = all_total_price + _quantity * row['price']
#
#                 session['all_total_quantity'] = all_total_quantity
#                 session['all_total_price'] = all_total_price
#                 return redirect(url_for('.products'))
#             else:
#                 return 'Error while adding item to cart'
#             except Exception as e:
#                         print(e)
#             finally:
#                     cursor.close()
# 		            conn.close()
#
# @app.route('/')
# def products():
# 	try:
# 		conn = sql.connect()
# 		cursor = conn.cursor(sql.cursor.DictCursor)
# 		cursor.execute("SELECT * FROM product")
# 		rows = cursor.fetchall()
# 		return render_template('products.html', products=rows)
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close()
# 		conn.close()
#
# @app.route('/empty')
# def empty_cart():
# 	try:
# 		session.clear()
# 		return redirect(url_for('.products'))
# 	except Exception as e:
# 		print(e)
#
# @app.route('/delete/<string:code>')
# def delete_product(code):
# 	try:
# 		all_total_price = 0
# 		all_total_quantity = 0
# 		session.modified = True
#
# 		for item in session['cart_item'].items():
# 			if item[0] == code:
# 				session['cart_item'].pop(item[0], None)
# 				if 'cart_item' in session:
# 					for key, value in session['cart_item'].items():
# 						individual_quantity = int(session['cart_item'][key]['quantity'])
# 						individual_price = float(session['cart_item'][key]['total_price'])
# 						all_total_quantity = all_total_quantity + individual_quantity
# 						all_total_price = all_total_price + individual_price
# 				break
#
# 		if all_total_quantity == 0:
# 			session.clear()
# 		else:
# 			session['all_total_quantity'] = all_total_quantity
# 			session['all_total_price'] = all_total_price

		#return redirect('/')
# 		return redirect(url_for('.products'))
# 	except Exception as e:
# 		print(e)
#
# def array_merge( first_array , second_array ):
# 	if isinstance( first_array , list ) and isinstance( second_array , list ):
# 		return first_array + second_array
# 	elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
# 		return dict( list( first_array.items() ) + list( second_array.items() ) )
# 	elif isinstance( first_array , set ) and isinstance( second_array , set ):
# 		return first_array.union( second_array )
# 	return False

if __name__ == '__main__':
    app.run(debug=True)
