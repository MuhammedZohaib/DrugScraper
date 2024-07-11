Certainly! Here’s a concise version of the `README.md` focusing on the essential information about your Scrapy spider:

---

# DrugScraper

This Scrapy spider (`DrugsspiderSpider`) scrapes drug information from `www.drugs.com`. It extracts drug names, generic names, drug classes, and URLs directly from the website.

## Spider Details

- **Name:** `DrugsspiderSpider`
- **Allowed Domains:** `www.drugs.com`

## Fields Extracted

- **Name:** Drug name.
- **Generic Name:** Generic name of the drug.
- **Drug Class:** Class of the drug.
- **URL:** URL of the drug page.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/MuhammedZohaib/DrugScraper.git
   cd DrugScraper
   ```

2. Run the spider:

   ```bash
   scrapy crawl drugsSpider
   ```

3. Output: Drug information (name, generic name, drug class, URL) in JSON and CSV format.

---
