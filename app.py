#i imported flask and jsonify along with mariadb and the dbcreds
from flask import Flask
import json
import dbhelpers
#i set app
app = Flask(__name__)
#so first i set up the /aniamls by calling the procedure and turing it into json then returning that json
@app.get('/animals')
def get_books():
    results = dbhelpers.run_procedures("CALL get_animals" , [])
    results_json = json.dumps(results, defualt=str)
    return results_json
#i set up the /dogs by calling the procedure and turing it into json then returning that json
@app.get('/dogs')
def get_books():
    results = dbhelpers.run_procedures("CALL get_cats" , [])
    results_json = json.dumps(results, defualt=str)
    return results_json
#and lastly i set up the /cats by calling the procedure and turing it into json then returning that json
@app.get('/cats')
def get_books():
    results = dbhelpers.run_procedures("CALL get_dogs" , [])
    results_json = json.dumps(results, defualt=str)
    return results_json
if __name__ == '__main__':
    app.run()
