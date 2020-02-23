from flask import Flask, render_template,request,redirect
#import pandas as pd
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
app.config['SECRET_KEY'] = 'you-will-never-guess'

mongo = PyMongo(app)


# http://127.0.0.1:5000/search_b/AUDI
@app.route('/search_b/<string:marque>')
def query_car1(marque):
    if marque:
        cars = mongo.db.scrapy_car.find({'marque': marque})
        # print(type(cars))
        # print(cars)
        if cars is not None:
            return render_template('search_marque.html', cars=cars)
        else:
            return render_template('nocar.html')


# http://127.0.0.1:5000/search_p/37600%E2%82%AC
@app.route('/search_p/<string:price>')
def query_car2(price):
    if price:
        cars = mongo.db.scrapy_car.find({'price': price})
        if cars is not None:
            return render_template('search_price.html', cars=cars)
        else:
            return render_template('nocar.html')


# ici on peux aussi creer un search pour l'annee

@app.route('/')
def rien():
    return "Nothing here... <a href='/recommendation'> click me </a> "

@app.route('/recommendation')
def recommendation():
    annee2020 = mongo.db.scrapy_car.find({'annee': "2020"})
    return render_template('recommendation.html', cars=annee2020)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 505


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
