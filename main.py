import requests
from bs4 import BeautifulSoup

PRODUCT_URL = ("https://www.amazon.com.mx/Roland-conectores-chapados-aislamiento-polietileno/dp/B07284ZC25/"
               "ref=sr_1_1_sspa?__mk_es_MX=ÅMÅŽÕÑ&crid=1UEA974N00HP4&dib=eyJ2IjoiMSJ9.21S3Ul4tNFLDedfncCxT6"
               "bn1QY7mTSfOLrsF0hXfgOWu4L5isDj-bqo8EOO0l-DQ6fzp6foeRmE1sQUrpPLlEQ-RFBthocpdrGiv-DgIvADoGg79"
               "9xBg5EFtn5GK8rygbRgbLX9G6RRQhDUFjlbLgSpBDk4ktsaGib2MQudgU_d_9iXkszmxy84LGDHr7qTfs2QSP4y6uGA"
               "XLvpt2gGgoXyhpymsoNIONkkYNM7mshblx8dufGCYnfgQauKmSwQJlOPtNlqJtocCYuNKAahp-_y8zJIkqz0mx1h5bs"
               "r0xPQ.Ib258qOi1LgTRB7QDD1oU_fa-KTABinCzDsG2Tugem4&dib_tag=se&keywords=roland%2Bmidi%2Bcable"
               "%2Bgold%2Bseries&qid=1716996901&sprefix=roland%2Bmidi%2Bcable%2Bgold%2Bseries%2Caps%2C142&s"
               "r=8-1-spons&ufe=app_do%3Aamzn1.fos.242f5c11-6cfd-40d6-91f6-be3d1974080c&sp_csd=d2lkZ2V0TmFt"
               "ZT1zcF9hdGY&th=1")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "es-419,es;q=0.9",
}

response = requests.get(url=PRODUCT_URL, headers=headers)
amazon_midi_cable = response.text
soup = BeautifulSoup(amazon_midi_cable, "html.parser")

try:
    price_whole = (soup.find(name="span", class_="a-price-whole")).getText()
    price_fraction = (soup.find(name="span", class_="a-price-fraction")).getText()
    price_tag = float(price_whole + price_fraction)
except ValueError:
    price_tag = "Sorry, Roland MIDI Cable Gold Series 3ft not available at the moment."

print(price_tag)
