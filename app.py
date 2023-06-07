#i imported flask and jsonify along with mariadb and the dbcreds
from flask import Flask
import json
import dbhelpers
import mariadb
#i set app
app = Flask(__name__)
#so first i set up the /aniamls by calling the procedure and turing it into json then returning that json
@app.get('/animals')
def get_aniamls():
    try:
        results = dbhelpers.run_procedures("CALL get_animals", [])
        results_json = json.dumps(results, default=str)
        return results_json

    except mariadb.IntegrityError:
        print("Sorry, what you entered doesn't exist")

    except mariadb.OperationalError:
        print('There is an error in the database')

    except mariadb.ProgrammingError:
        print('Error in the SQL syntax or query execution')

    except Exception as error:
        print('Error:', error)
    return results_json
#i set up the /dogs by calling the procedure and turing it into json then returning that json
@app.get('/dogs')
def get_dogs():
    try:
        results = dbhelpers.run_procedures("CALL get_animals", [])
        results_json = json.dumps(results, default=str)
        return results_json

    except mariadb.IntegrityError:
        print("Sorry, what you entered doesn't exist")

    except mariadb.OperationalError:
        print('There is an error in the database')

    except mariadb.ProgrammingError:
        print('Error in the SQL syntax or query execution')

    except Exception as error:
        print('Error:', error)
    return results_json
#and lastly i set up the /cats by calling the procedure and turing it into json then returning that json
@app.get('/cats')
def get_cats():
    try:
        results = dbhelpers.run_procedures("CALL get_animals", [])
        results_json = json.dumps(results, default=str)
        return results_json

    except mariadb.IntegrityError:
        print("Sorry, what you entered doesn't exist")

    except mariadb.OperationalError:
        print('There is an error in the database')

    except mariadb.ProgrammingError:
        print('Error in the SQL syntax or query execution')

    except Exception as error:
        print('Error:', error)
    return results_json
if __name__ == '__main__':
    app.run()
