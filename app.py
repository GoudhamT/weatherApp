from flask import Flask, render_template, request
import requests


app = Flask(__name__)


#show basic UI page

@app.route('/', methods=['POST','GET'])
def homepageUI():
    return render_template('index.html')

# get Weather Data for giuven City and API key
@app.route('/weatherapp',methods=['POST','GET'])
def getWeatherData():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    weatherInput = {
        'q': request.form.get('city'),
        'appid': request.form.get('appid'),
        'units': request.form.get('units')
    }

    weather_dtl = requests.get(url,params=weatherInput)
    weather_json = weather_dtl.json()
    return f"{weather_json}"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)

