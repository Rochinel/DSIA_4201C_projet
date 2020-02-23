# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient


class CarPipeline(object):
	collection_name='scrapy_car'

	def open_spider(self , spider):
		self.client = pymongo.MongoClient()
		self.db = self.client["test"]

	def close_spider(self , spider):
		self.client.close()

		


	def process_item(self, item, spider):
		if item['version']:
 			item['version']= item['version'][0]

		if item['km_compteur']:
			item['km_compteur']=clean_spaces(item['km_compteur'])
		
		self.db[self.collection_name].insert_one(dict(item)) #stockage dans la base de donnée
    	
		return item


def clean_spaces(string):
	if string:
		return " ".join(string.split())

def clean_repetion(string):
	pass


