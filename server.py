import random, markupsafe
from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'keep it secret keep it safe'


@app.route("/")
def index():
    if "your_gold" not in session:
        session["your_gold"] = 0

    if "activities" not in session:
        session["activities"] = []

    activities= session["activities"]


    return render_template("index.html", activities=activities)


@app.route('/process_money', methods=["POST"])
def process_money():
    location = request.form["location"]
    activities = session["activities"]
    if location == "farm":
        golds = random.randint(10, 20)
        activities.append({
            "activityName": "Farm",
            "earnedValue": golds,
            "date": datetime.now()
        })
    elif location == "cave":
        golds = random.randint(5, 10)
        activities.append({
            "activityName": "Cave",
            "earnedValue": golds,
            "date": datetime.now()
        })
    elif location == "house":
        golds = random.randint(2, 5)
        activities.append({
            "activityName": "House",
            "earnedValue": golds,
            "date": datetime.now()
        })
    elif location == "casino":
        golds = random.randint(-50, 50)
        activities.append({
            "activityName": "Casino",
            "earnedValue": golds,
            "date": datetime.now()
        })

    session["activities"] = activities
    session["your_gold"] += golds 

    return redirect("/")

@app.route("/reset")
def reset():
        session.clear()
        return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)
