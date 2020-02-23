# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import CarItem


class LacentraleSpider(scrapy.Spider):
    name = 'lacentrale'
    allowed_domains = ['lacentrale.fr']
    start_urls = ['http://lacentrale.fr/']

    #first level parse 
    #Goal: navigate in the main page of web site

    def parse(self, response):
    	title=response.css('title::text').extract_first()
    	main_link=response.css('.topBrandsPlusAd').css('div')[9].css('ul').css('li')[13].css('a::attr(href)').extract()[0]
    	yield Request(main_link,callback=self.parse_level_1)

    #second level parse 
    #goal: extract all the links of each car cars in the main page

    def parse_level_1(self , response):
    	all_link_modele_car = {
    	name : response.urljoin(url) for name , url in zip (
    	response.css('.ListeModeleMarque .mW10').css('ul').css('li').css('a').css('a::text').extract(),
    	response.css('.ListeModeleMarque .mW10').css('ul').css('li').css('a').css('.marqueMobLinkLogo').css('a::attr(href)').extract()) 
    	}
    	

    	for link in all_link_modele_car.values():
    	
    		yield Request(link , callback=self.parse_level_2)
    	
    		

 	#third level parse
 	#goal : extract all the car of each page in the websit	

    def parse_level_2(self , response):
    	cars= {name: response.urljoin(i) for name , i in zip (
    	  	response.css('.mainCol .adLineContainer').css('a::attr(title)').extract(),
    	  	response.css('.mainCol .adLineContainer').css('a::attr(href)').extract())
    	}


    	for car in cars.values():
    		yield Request(url=car,meta={'lien':car},callback=self.parse_item)


    	next=response.css('.arrow-btn').css('a::attr(href)').extract()[-1]

    	if next: 
    		yield Request(url=response.urljoin(next),callback=self.parse_level_2) #go to the next page if exist


    # extract all the information for each car 

    def parse_item(self,response):
        
        list=[elt.css("span")[-1].css('::text').extract_first() for elt in response.css('.cbm-moduleInfos__informationList li')]
        annee=list[0]
        km_compteur=list[3]
        energie=list[4]
        boite_de_vitesse=list[5]
        couleur=list[6]
        nb_porte=list[8]
        version=response.css('.cbm-moduleInfos__informationListFirst li').css("span")[-1].css('::text').extract()
        marque=response.css('.cbm-title--page::text').extract_first().split()[0]
        model=response.css('.cbm-title--page::text').extract_first().split()[1]
        price="".join(response.css('.cbm__priceWrapper::text').extract_first().split())
        title_info=" ".join(response.css('.cbm-title--page::text').extract_first().split())
        lien=response.meta['lien']
    	
        yield CarItem(
        annee=annee,
        km_compteur=km_compteur,
        energie=energie,
        boite_de_vitesse=boite_de_vitesse,
        couleur=couleur,
        nb_porte=nb_porte,
        version=version,
        marque=marque,
        model=model,
        price=price,
        title_info=title_info,
        lien=lien
        )
		








    	
    	

