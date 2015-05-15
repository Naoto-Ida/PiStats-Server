from application import app
from flask import render_template, jsonify
import os
import sys
import psutil
import json

@app.route('/cpu')
def cpu():
	cpus = get_cpus()
	return jsonify(results = cpus)

def get_cpus():
	list = []
	list.append({"percent": psutil.cpu_percent()})
	return list
