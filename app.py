from flask import Flask, jsonify
import mariadb
import dbcreds

app = Flask(__name__)

@app.route('/animals', methods=['GET'])
def get_all_animals():
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()

        cursor.execute("SELECT name, species FROM animal")
        animals = cursor.fetchall()

        animals_list = []
        for animal in animals:
            animal_dict = {
                'name': animal[0],
                'species': animal[1]
            }
            animals_list.append(animal_dict)

        return jsonify(animals_list)

    except mariadb.Error as e:
        print("Error connecting to MariaDB: ", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/dogs', methods=['GET'])
def get_dogs():
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()

        cursor.execute("SELECT name, species FROM animal WHERE species = 'dog'")
        dogs = cursor.fetchall()

        dogs_list = []
        for dog in dogs:
            dog_dict = {
                'name': dog[0],
                'species': dog[1]
            }
            dogs_list.append(dog_dict)

        return jsonify(dogs_list)

    except mariadb.Error as e:
        print("Error connecting to MariaDB: ", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/cats', methods=['GET'])
def get_cats():
    try:
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()

        cursor.execute("SELECT name, species FROM animal WHERE species = 'cat'")
        cats = cursor.fetchall()

        cats_list = []
        for cat in cats:
            cat_dict = {
                'name': cat[0],
                'species': cat[1]
            }
            cats_list.append(cat_dict)

        return jsonify(cats_list)

    except mariadb.Error as e:
        print("Error connecting to MariaDB: ", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run()
