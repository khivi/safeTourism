import flask
from flask import request, jsonify
import main

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/testapi', methods=['GET'])
def api_test():
    return "Success"

@app.route('/api/v1/getNews', methods=['GET'])
def api_id():
    if 'location' in request.args:
        location = str(request.args['location'])
    else:
        return "Location Parameter missing."
    result = []
    print(location)
    news = main.main(location)
    result.append(news)
    return jsonify(result)

@app.errorhandler(404)
def page_not_found(e):
    return str(e) + "Requested Resource not found"

app.run(host='0.0.0.0')
