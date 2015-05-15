from application import app
from flask import render_template, jsonify
import os
import sys
import psutil

@app.route('/memory')
def memory():
	memories = get_memories()
	return jsonify(results = memories)

def get_memories():
	list = []
	info = psutil.virtual_memory()

	list.append({"total": info[0], "available": info[1], "percent": info[2], "used": info[3], "free": info[4], "active": info[5], "inactive": info[6], "buffers": info[7], "cached": info[7]})
	return list
