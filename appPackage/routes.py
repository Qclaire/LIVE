from flask import render_template, request
from . import app
from .models import *
import json



@app.route('/', methods=["GET"])
def home():
	data = Data.query.order_by('-id').first()
	# context = {"temperature":query.temperature, "moisture":query.moisture, "humidity":query.humidity, "status":query.status}
	# temp = query.temperature
	# moist = query.moisture
	# hum = query.humidity
	# stat = query.status
	# //data = json.dumps(context)
	return render_template('home.html', data=data)
	# query the db for the last item
	# send and object to be taken apart on the front end

@app.route('/info', methods=['GET'])
def info():
	return render_template('blank.html')


@app.route("/update", methods = ['POST'])
def updateDB():
	if request.method=="POST":
		data = request.data
		data = data.decode("utf-8")
		data = data.split()
		temperature = data[0]
		humidity = data[1]
		moisture = data[2]
		status = data[3]
		print(data)
	return "True"


@app.route('/login')
def login():
	return render_template('login.html')