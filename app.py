from flask import Flask, request,jsonify,redirect,url_for
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
                    cursor.execute("SELECT FROM User WHERE adm_mail = '?' AND adm_pass = '?' "),()

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
                msg = "New user successfully added"
                return jsonify(msg)

        except:
                con.rollback()
                msg = "No new User added"
                return jsonify(msg)

        finally:
                con.close()

# ADMINS ABILITY TO VIEW THE USERS THAT REGISTERED
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
            print("There was an error fetching User results from the database: " + str(e))
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
                msg = "Admin successfully added"
                return jsonify(msg)

        except:
                con.rollback()
                msg = "New Admin not added."
                return jsonify(msg)

        finally:
                con.close()

# ADMINS ABILITY TO VIEW THE ADMINS THAT THEY REGISTERED.
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
@app.route('/itemvalues')
def itemvalues():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('INSERT INTO Product (id,name, code, image, price) VALUES(1, Full Tattoo Kit, KITSET1, product-images/bag.jpg, R12000.00),
                2, Tattoo Needles, NEEDLE2, product-images/bag.jpg, R12000.00),
                3, Generators, GEN3, product-images/bag.jpg, R12000.00),
                4, Ink , INKZ4, product-images/bag.jpg, R12000.00),



@app.route('/add', methods=['POST'])
def add_product_to_cart():
    cursor = None
	try:
		_quantity = int(request.form['quantity'])
		_code = request.form['code']

		# validate the received values
		if _quantity and _code and request.method == 'POST':
			conn = sql.connect()
			cursor = conn.cursor(sql.cursor.DictCursor)
			cursor.execute("SELECT * FROM Product WHERE code=%s", _code)
			row = cursor.fetchone()

			itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity' : _quantity, 'price' : row['price'], 'image' : row['image'], 'total_price': _quantity * row['price']}}

			all_total_price = 0
			all_total_quantity = 0

			session.modified = True

            if 'cart_item' in session:
				if row['code'] in session['cart_item']:
					for key, value in session['cart_item'].items():
						if row['code'] == key:
							#session.modified = True
							#if session['cart_item'][key]['quantity'] is not None:
							#	session['cart_item'][key]['quantity'] = 0
							old_quantity = session['cart_item'][key]['quantity']
							total_quantity = old_quantity + _quantity
							session['cart_item'][key]['quantity'] = total_quantity
							session['cart_item'][key]['total_price'] = total_quantity * row['price']

                        else:
                            session['cart_item'] = array_merge(session['cart_item'], itemArray)
                            for key, value in session['cart_item'].items():
                                individual_quantity = int(session['cart_item'][key]['quantity'])
                                individual_price = float(session['cart_item'][key]['total_price'])
                                all_total_quantity = all_total_quantity + individual_quantity
                                all_total_price = all_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                all_total_price = all_total_price + _quantity * row['price']

                session['all_total_quantity'] = all_total_quantity
                session['all_total_price'] = all_total_price
                return redirect(url_for('.products'))
            else:
                return 'Error while adding item to cart'
            except Exception as e:
                        print(e)
            finally:
                    cursor.close()
		            conn.close()

@app.route('/')
def products():
	try:
		conn = sql.connect()
		cursor = conn.cursor(sql.cursor.DictCursor)
		cursor.execute("SELECT * FROM product")
		rows = cursor.fetchall()
		return render_template('products.html', products=rows)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/empty')
def empty_cart():
	try:
		session.clear()
		return redirect(url_for('.products'))
	except Exception as e:
		print(e)

@app.route('/delete/<string:code>')
def delete_product(code):
	try:
		all_total_price = 0
		all_total_quantity = 0
		session.modified = True

		for item in session['cart_item'].items():
			if item[0] == code:
				session['cart_item'].pop(item[0], None)
				if 'cart_item' in session:
					for key, value in session['cart_item'].items():
						individual_quantity = int(session['cart_item'][key]['quantity'])
						individual_price = float(session['cart_item'][key]['total_price'])
						all_total_quantity = all_total_quantity + individual_quantity
						all_total_price = all_total_price + individual_price
				break

		if all_total_quantity == 0:
			session.clear()
		else:
			session['all_total_quantity'] = all_total_quantity
			session['all_total_price'] = all_total_price

		#return redirect('/')
		return redirect(url_for('.products'))
	except Exception as e:
		print(e)

def array_merge( first_array , second_array ):
	if isinstance( first_array , list ) and isinstance( second_array , list ):
		return first_array + second_array
	elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
		return dict( list( first_array.items() ) + list( second_array.items() ) )
	elif isinstance( first_array , set ) and isinstance( second_array , set ):
		return first_array.union( second_array )
	return False
if __name__ == '__main__':
    app.run(debug=True)
