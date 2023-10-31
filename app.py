from flask import Flask, render_template, request
import requests

# Create an APP
app=Flask(__name__)

# At what route it is suppose to render the HTML page:
@app.route('/')
# Render my HTML page
def homepage():
    return render_template("index.html")

@app.route("/WeatherAPI", methods=['POST','GET'])
def get_weatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"
    required_params={'q':request.form.get("city"),
                     'appid': request.form.get("appid"),
                     'units': request.form.get("metric")
    } 
    response=requests.get(url,params=required_params)
    data=response.json()
    return f"data{data}"



if __name__=='__main__':
    app.run(host="0.0.0.0",port=5002)