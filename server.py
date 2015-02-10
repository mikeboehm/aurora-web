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

@app.route("/update_alarm", methods=['POST'])
def update_alarm():
	settings_manager = SettingsManager()
	settings = settings_manager.get_settings()

# 	print request.form

	day_map = {
		'sunday_time': '0',
		'monday_time': '1',
		'tuesday_time': '2',
		'wednesday_time': '3',
		'thursday_time': '4',
		'friday_time': '5',
		'saturday_time': '6',
	}
	
	form_day_name = request.form['day']

	alarms = settings['settings']['alarms']
	
	if form_day_name in day_map:
		weekday_number = day_map[form_day_name]
		alarms[weekday_number]['time'] = request.form['alarm_time']
		
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