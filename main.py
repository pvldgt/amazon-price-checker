import requests
from bs4 import BeautifulSoup
import lxml


# scrape the price off of Amazon webpage
# header info that I got using http://myhttpheader.com
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
           "Accept-Language": "en-GB,en;q=0.9"}
# Amazon product page URL
url = "https://www.amazon.com/dp/B07CNHS3MG/ref=syn_sd_onsite_desktop_65?ie=UTF8&pd_rd_plhdr=t&th=1"

# Get the HTML of the page
response = requests.get(url, headers=headers)
amazon_html = response.text

# Make soup of the HTML
soup = BeautifulSoup(amazon_html, "lxml")

# Find the price
pre_price = soup.select(selector="div.a-section span.priceToPay span.a-offscreen")

# Get rid of the dollar sign and convert it to a float
price = float(pre_price[0].getText().replace("$", ""))

