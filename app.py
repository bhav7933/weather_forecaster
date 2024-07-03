from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getWeather', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')
    url = f'https://wttr.in/{city_name}?format=3'
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return "Error Occurred"

if __name__ == '__main__':
    app.run(debug=True)
