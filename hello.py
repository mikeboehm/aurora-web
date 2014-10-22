from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    monday_time = '07:00'
    
    return render_template('index.html', monday_time=monday_time)


@app.route("/update")
def update():
	alarms = {'monday': '07:00'}
	settings = {'alarms' : alarms }
# 	print settings
	
	return jsonify(settings);
# 	f = open('settings.json', 'w')
#     return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
# 	app.run(host='0.0.0.0')