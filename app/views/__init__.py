from app import flask_app as app
import json
from datetime import datetime
import numpy as np


@app.route("/heartbeat")
def heartbeat():
    return json.dumps(
        {
            "status": True,
            "service": "Homework_Template",
            "datetime": f"{datetime.now()}"
        }
    )

@app.route("/sum", methods = ['POST'])
def sum():
    data =  request.json
    x = int(data['x'])
    y = int(data['y'])
    
    result = {x + y}
    return json.dumps({'Sum': result})

@app.route("/minimum", methods = ['POST'])
def minimum():
    data =  request.json
    values = data['values']
    result = min(values)
    return json.dumps({'Minimum': result})

@app.route("/product", methods = ['POST'])
def product():
    data =  request.json
    values = data['values']
    if len(values):
        result = int(np.prod(values))
    else :
        result = 0
    return json.dumps({'Product': result})

@app.before_first_request
def load_app():
    print("Loading App Before First Request")
