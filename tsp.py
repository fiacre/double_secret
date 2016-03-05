from flask import Flask
from flask import jsonify, request
from lib import parse_cities, run_anneal

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"Context": "Hello World!"})

@app.route("/anneal", methods=['GET', 'POST'])
def anneal():
    if request.method == 'POST':
        json_data = request.get_json()
        cities = parse_cities(json_data)
        state = run_anneal(cities)
        return jsonify({"items" : state})
    elif request.method == 'GET':
        return jsonify({"Context": "POST json file of cities"})

if __name__ == "__main__":
    app.debug = True
    app.run()