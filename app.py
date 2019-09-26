from flask import Flask
import json
from datetime import datetime
from flask import request


app = Flask(__name__)

@app.route('/heartbeat')
def heartbeat():
    return json.dumps(
        {
            "status": True,
            "service": "Checking Heartbeat from System",
            "datetime": f"{datetime.now()}"
        }
    )

@app.route('/sum',  methods=['POST'])
def sum():
	form = request.form
	print(form)
	x = form.get("x")
	y = form.get("y")

	x = int(x)
	y = int(y)

	print(x)
	print(y)

	results = {
	"result": x + y
	}

	return json.dumps(results)

@app.route('/minimum', methods=['POST'])
def minimum():
	form = request.form
	print(form)
	x = form.get("values")

	min_x=min(x)


	results = {
	"result": min_x
	}

	return json.dumps(results)

@app.route('/product', methods=['POST'])
def product():
	form = request.form
	print(form)
	x = form.get("values")

	if len(x) == 0:
		res = 0

	else:
		res = np.prod(x)


	results = {
	"result": res
	}

	return json.dumps(results)

@app.before_first_request
def load_app():
	print("Loading App Before First Request")
	'''