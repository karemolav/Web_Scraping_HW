from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts

@app.route("/")
def index():
    mars_info = db.mars.find_one()
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape():
    mars_info = db.mars
    mars_dict= scrape_mars.Scrape()
    mars_info.update(
        {},
        mars_dict,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)