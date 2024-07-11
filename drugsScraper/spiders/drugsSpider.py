import scrapy
from bs4 import BeautifulSoup

class DrugsspiderSpider(scrapy.Spider):
    name = "drugsSpider"
    allowed_domains = ["www.drugs.com"]
    
    def __init__(self):
        super().__init__()
        self.start_urls = []
        self.drug_urls = []
        with open('alpha.xml', 'r') as sites_xml:
            soup = BeautifulSoup(sites_xml, 'lxml')
            self.start_urls = [link.text for link in soup.find_all("loc")]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.get_all_drugs_urls)
        for drug_url in self.drug_urls:
            yield scrapy.Request(f"https://www.drugs.com{drug_url}", callback=self.parse)    
    
    def get_all_drugs_urls(self, response):
        self.drug_urls.extend(response.css("div#content ul.ddc-list-unstyled li > a::attr(href)").getall())
        
    
    def parse(self, response):
        yield {
            "name" : response.css("div#content h1::text").get(default="N/A"),
            "generic_name" : response.css('p.drug-subtitle > b:contains("Generic name:") + a::text').get(default="N/A"),
            "drug_class" : response.css('p.drug-subtitle > b:contains("Drug class:") + a::text').get(default="N/A"),
            "url": response.url
        }
