from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
	return render_template('menu.html')


@app.route('/', methods=['POST'])
def my_form_post():
    time = request.form['time']
    horoscope = request.form['horoscope']
    info = get_data(time, horoscope)

    return info

#http://horoscope-api.herokuapp.com/horoscope/today/scorpio

def get_data(time, horoscope):
	r = requests.get(f"http://horoscope-api.herokuapp.com/horoscope/{time}/{horoscope}")

	data = json.loads(r.content)

	data = data['horoscope']

	return render_template('result.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
