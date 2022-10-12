from httpx import head
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import json

from bs4 import BeautifulSoup

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Use e24 for Corpus base
url = "https://e24.no/siste?pageId="

articleLinks = []

def findArticleLinks(p):
    driver.get(url + str(p))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all(attrs={"data-test-tag": "internal-link"})

    for a in articles:
        if a:
            articleLinks.append(a['href'])

x = 0

while len(articleLinks) < 250:
    findArticleLinks(x)
    x += 1

articleDict = {"articles":[]}

for link in articleLinks:
    url = "https://e24.no"+link
    driver.get(url)
    articleSoup =  BeautifulSoup(driver.page_source, 'html.parser')
    try:
        topic = articleSoup.find("div", "running-head").get_text()
        headline = articleSoup.find(attrs={"data-test-tag": "headline"}).get_text()
        ingress = articleSoup.find(attrs={"data-test-tag": "lead-text"}).get_text()
        time = articleSoup.find("time")["datetime"]
        paragraphs = articleSoup.find(attrs={"data-test-tag": "lead-text"}).find_all_next(["p", "h2", "h3", "h4"])
        text = " ".join([w.get_text() for w in paragraphs])
        articleObject = {"topic": topic, "headline": headline, "ingress":ingress, "published": time, "textbody": text, "url": url}
        articleDict["articles"].append(articleObject)
    except: pass

file = open("corpus.json","w")

print(articleDict)

file.write(json.dumps(articleDict, indent=4, ensure_ascii=False))

file.close()