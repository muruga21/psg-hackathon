from flask import Flask,render_template
import requests

app = Flask(__name__)

response = requests.get('https://script.google.com/macros/s/AKfycbxMV_S4qmvtA_NDo6fgJozS58MqINHSyty4MGu6HBIEIpEU_AmCrm_Yt4I5x1d4R-G0Vg/exec').json()


@app.route('/')
def hello():
    return render_template('home.html',response=response)

# @app.route('/kishore')
# def kishore():
#     return "kishore"
