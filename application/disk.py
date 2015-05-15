from application import app
from flask import jsonify
import os
import sys
import psutil

@app.route('/disk')
def disk():
	disks = get_disks()
	return jsonify(results = disks)

def bytes_to_human(n):
	symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
	prefix = {}
	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10
	for s in reversed(symbols):
		if n >= prefix[s]:
			value = float(n) / prefix[s]
			return '%.1f%s' % (value, s)
	return "%sB" % n


def get_disks():
	list = []
	for part in psutil.disk_partitions(all=False):
		if os.name == 'nt':
			if 'cdrom' in part.opts or part.fstype == '':
				continue
		usage = psutil.disk_usage(part.mountpoint)
		device = part.device
		total = bytes_to_human(usage.total)
		used = bytes_to_human(usage.used)
		free = bytes_to_human(usage.free)
		percent = int(usage.percent)
		fstype = part.fstype
		mountpoint = part.mountpoint
		list.append({"device": device, "total": total, "used": used, "free": free, "percent": percent, "fstype": fstype, "mountpoint": mountpoint})
	return list
