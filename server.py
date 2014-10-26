#!/usr/bin/env python
import socket
from flask import Flask, json, jsonify, render_template, request, url_for
from settings_manager import SettingsManager
from messenger import Messenger

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/get_settings")
def get_settings():
	settings_manager = SettingsManager()
	return jsonify(settings_manager.get_settings())

@app.route("/toggle_lights")
def toggle_lights():	
	Messenger().toggle_lights()

	return ""

@app.route("/update_alarms", methods=['POST'])
def update_alarms():
	settings_manager = SettingsManager()
	settings = settings_manager.get_settings()

# 	print request.form
	
	alarms = settings['settings']['alarms']

	if request.form['sunday_time']:
		alarms['0']['time'] = request.form['sunday_time']
	if request.form['monday_time']:
		alarms['1']['time'] = request.form['monday_time']
	if request.form['tuesday_time']:
		alarms['2']['time'] = request.form['tuesday_time']
	if request.form['wednesday_time']:
		alarms['3']['time'] = request.form['wednesday_time']
	if request.form['thursday_time']:
		alarms['4']['time'] = request.form['thursday_time']
	if request.form['friday_time']:
		alarms['5']['time'] = request.form['friday_time']
	if request.form['saturday_time']:
		alarms['6']['time'] = request.form['saturday_time']
	
	settings['settings']['alarms'] = alarms

	settings_manager.set_settings(settings)
	return "";

if __name__ == "__main__":
	# Generate hostname
	bonjour_address = socket.gethostname()
	# If IP address, use as is
	try:
		socket.inet_aton(bonjour_address)	
	except socket.error:
		# Otherwise make sure the address will work
		if not bonjour_address.endswith('.local'):
			bonjour_address += '.local'
	
	app.run(debug=False, host=bonjour_address)
# 	app.run(host=bonjour_address)