# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
	annee=scrapy.Field()
	km_compteur=scrapy.Field()
	energie=scrapy.Field()
	boite_de_vitesse=scrapy.Field()
	couleur=scrapy.Field()
	nb_porte=scrapy.Field()
	version=scrapy.Field()
	marque=scrapy.Field()
	model=scrapy.Field()
	price=scrapy.Field()
	title_info=scrapy.Field()
	lien=scrapy.Field()
        
