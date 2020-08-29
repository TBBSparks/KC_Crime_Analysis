from flask import Flask 
from flask import render_template
from flask import redirect
from flask import request
from flask_pymongo import PyMongo
import scrape_wanted
from pymongo import MongoClient
import pymongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/wanted"
mongo = PyMongo(app)


@app.route("/")
def index():

    wanted = mongo.db.wanted.find_one()

    return render_template("wanted.html", wanted = wanted)

  
@app.route("/scrape")
def scrape():

    # Run the scrape function
    # wanted = client.db.wanted
    wanted = mongo.db.wanted
    wanted_web = scrape_wanted.scrape_latest()

    

    wanted.update({}, wanted_web, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)