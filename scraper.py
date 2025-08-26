import requests
from bs4 import BeautifulSoup
import json
from deep_translator import GoogleTranslator

URL = "https://www.da.gov.ph/category/news/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select(".td_module_10")[:5]
news = []

for article in articles:
    title_en = article.select_one(".entry-title").text.strip()
    date = article.select_one(".td-post-date").text.strip()
    summary_en = article.select_one(".td-excerpt").text.strip()

    title_tl = GoogleTranslator(source='auto', target='tl').translate(title_en)
    summary_tl = GoogleTranslator(source='auto', target='tl').translate(summary_en)

    news.append({
        "petsa": date,
        "pamagat": title_tl,
        "buod": summary_tl
    })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)
