from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

import application.index
import application.cpu
import application.disk
import application.memory
