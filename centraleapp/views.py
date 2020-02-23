#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, \
    request, url_for, make_response, redirect
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from flask_pymongo import PyMongo
import os
#from app import app

app = Flask(__name__)
es = Elasticsearch('http://localhost:9200')
# es = Elasticsearch('10.0.1.10', port=9200)


app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)


@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = es.search(
        index="scrape-sysadmins",
        size=20,
        body={
            "query": {
                "multi_match": {
                    "query": search_term,
                    "fields": [
                        "url",
                        "title",
                        "tags"
                    ]
                }
            }
        }
    )
    return render_template('results.html', res=res)


@app.route('/search')
def home():
    return render_template('search.html')


@app.route('/')  # , methods=['GET', 'POST'])
def index():
    top20 = [mongo.db.scrapy_car.find_one({"price": str(k)}) for k in range(1, 21)]
    return render_template('index.html', top=top20)


@app.route('/search')
def search():
    return render_template('index.html')


@app.route('/recommender')
def recommender():
    return render_template('recommender.html')


@app.route('/title/<marque>')
def title(marque):
    serie = mongo.db.scrapy_car.find_one({"marque": title})
    if serie is None:
        return render_template('404.html')

    try:
        l_recommandations = []
        for rec_id in serie["recommandations"]:
            rec = mongo.db.scrapy_car.find_one({"marque": rec_id})
            l_recommandations.append(rec)

    except Exception as e:
        print(e)
        recommandations = ""
    return render_template('voiture.html', **serie, l_rec=l_recommandations)


@app.route('/voiture', methods=['GET'])
def daily_post():
    return render_template("voirture.html", marque=request.args.get('marque'), price=request.args.get('price'))


@app.route('/title', methods=['POST'])
def setcookie2():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(redirect(url_for('title', title=user)))
    resp.set_cookie('userID', user)

    return resp


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response("setting_cookie")
    resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome ' + name + '</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 505


if __name__ == '__main__':
    app.run()
