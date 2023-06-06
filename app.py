#i imported flask and jsonify along with mariadb and the dbcreds
from flask import Flask, jsonify
import mariadb
import dbcreds
#i set app
app = Flask(__name__)
#so first i set up the animals get all, i set the conn amd cursor
@app.route('/animals', methods=['GET'])
def get_all_animals():
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
#i then call the sql to run the get_animals procedure
        cursor.callproc('get_animals')
        animals = cursor.fetchall()
#i put the animals in an empty array to then be jsonified
        animals_list = []
        for animal in animals:
            animal_dict = {
                'name': animal[0],
                'species': animal[1]
            }
            animals_list.append(animal_dict)
#i return the list of the animal array
        return jsonify(animals_list)

    except mariadb.Error as e:
        print("Error connecting to MariaDB: ", e)
#i pu tthe close in the finally
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
#i then make the dogs function
@app.route('/dogs', methods=['GET'])
def get_dogs():
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
#i tell it to run the get_dogs procedure
        cursor.callproc('get_dogs')
        dogs = cursor.fetchall()
#i also store that in an empty array to be jsonified
        dogs_list = []
        for dog in dogs:
            dog_dict = {
                'name': dog[0],
                'species': dog[1]
            }
            dogs_list.append(dog_dict)
#i then return the the array
        return jsonify(dogs_list)

    except mariadb.Error as e:
        print("Error connecting to MariaDB: ", e)
#i put the close in the finally
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
#i then make the cats route
@app.route('/cats', methods=['GET'])
def get_cats():
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
#i get the get_cats procedure
        cursor.callproc('get_cats')
        cats = cursor.fetchall()
#i put the cats into an array and loop through them
        cats_list = []
        for cat in cats:
            cat_dict = {
                'name': cat[0],
                'species': cat[1]
            }
            cats_list.append(cat_dict)
#i then return the array as a json
        return jsonify(cats_list)

    except mariadb.Error as e:
        print("Error connecting to MariaDB: ", e)
#i then make sure the .close are in the finally
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run()
