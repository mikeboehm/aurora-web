import socket
bonjour_address = socket.gethostname()

from flask import Flask, json, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/get_settings")
def get_settings():
	fp = open('settings.json')
	settings = json.load(fp)
	return jsonify(settings)



@app.route("/toggle_lights")
def toggle_lights():
	import pika
	connection = pika.BlockingConnection(pika.ConnectionParameters(
		host='localhost'))
	channel = connection.channel()	
	channel.queue_declare(queue='aurora')	
	channel.basic_publish(exchange='',
		routing_key='aurora',
		body='Hello World!')
	connection.close()
	return ""

@app.route("/update")
def update():
	alarms = {
		0 : {
			'time': '07:00',
			'day': 'Monday',
		}
	}
	settings = {'alarms' : alarms }
# 	print settings
	
	return jsonify(settings);
# 	f = open('settings.json', 'w')
#		return "Hello World!"

if __name__ == "__main__":
	app.run(debug=True, host=bonjour_address)
# 	app.run(host='aurora.local')