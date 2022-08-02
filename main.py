import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from credentials import my_email, my_password

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
product_price = float(pre_price[0].getText().replace("$", ""))

# Set up an email alert if the price gets lower than the target price
target_price = 200

# Get the product title
product_title = soup.find(id="productTitle").get_text().split("–")[0].strip()

# Send an email alert if the product price is lower than thhe target price
if product_price <= target_price:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Time to buy!\n\n{product_title} you wanted is now only ${product_price}")