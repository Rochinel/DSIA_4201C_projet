# DSIA_4201C_projet
extraction of data from centrale.fr and presentation in an application vial

# lacentrale_voitures_app

- Course : DRIO-4201C Data Engineering
- February 23, 2020
- Students : Rochinel_bienvenu NANFA, Lintao XU, Simon NOGRET
- Teacher : Raphaël Courivaud

## DISCLAIMER

This project is for informational and educational purposes, do not use it for business purposes.

## Tasks

- [x] Lacentrale scraping with Scrapy (log.py)
- [x] MongoDB database
- [x] Flask application
    - [x] basic app with MongoDB (dataapp)
	- [x] app with Elasticsearch and MongoDB (centraleapp)
	- on a fini la pluspart des codes de app(centrale) ,mais il y a des problems de configuration
-  Docker
	- [x] docker-compose.yml
	- [x] Dockerfile
	- [] run mongodb inside Docker : pas reussi
	- [] run elasticsearch inside Docker : pas reussi

## The project

Crawling/scraping of [lacentrale](http://lacentrale.fr/) for cars, with Scrapy.

Save data into MongoDB database.

Create a Flask web-app to display the data.

Dans la Flask web-app , search the data through Elasticsearch
