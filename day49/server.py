from flask import Flask, render_template
import random
import datetime
import requests

# parameter = {
#         "name": f"alex"
#     }
#
# response = requests.get("https://api.agify.io", params=parameter)
# response.raise_for_status()
# data = response.json()
# print(data["count"])

app = Flask(__name__)


@app.route("/guess/<name>")
def home(name):
    parameter = {
        "name": f"{name}"
    }

    age = requests.get("https://api.agify.io", params=parameter)
    age.raise_for_status()
    data = age.json()

    gender = requests.get("https://api.genderize.io", params=parameter)
    gender.raise_for_status()
    res = gender.json()


    year = datetime.datetime.now().year
    return render_template('index.html', count=data["count"], name=data["name"], age=data["age"], year=year, gender=res["gender"], probab=res["probability"])


if __name__ == "__main__":
    app.run(debug=True)
