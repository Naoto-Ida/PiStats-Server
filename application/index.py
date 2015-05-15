from application import app
from flask import render_template
from flask.ext.basicauth import BasicAuth

app_name = "PiStats"
app.config['BASIC_AUTH_USERNAME'] = 'rpi'
app.config['BASIC_AUTH_PASSWORD'] = 'rpi'
basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def index():
	return render_template("index.html", app_name = app_name)
