# Drugs Scraper

## Scope

- downloaded the sitemap for all drugs as a xml file
- parse the xml file using bs4 to get all the index links for all drugs
- crawl each link and get names of all drugs on that link
- send request on each and every drug url
- scrape data from the link
- save the data as json or xml

## Selectors

name = response.css("div.ddc-pronounce-title h1::text").get(default="N/A")
description = response.css("#content > p:nth-child(7)::text").get()
generic_name = response.css(".drug-subtitle > a:nth-child(2)::text").get()
drug_class = response.css(".drug-subtitle > a:nth-child(7)::text").get()
