# How to Scrape E-Commerce Websites With Python

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.io/pages/gitoxy?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=scraping-ecommerce-websites-github&transaction_id=102f49063ab94276ae8f116d224b67)


[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/Pds3gBmKMH)

Scraping e-commerce websites is easy with Python and Oxylabs [E-Commerce Scraper API](https://oxylabs.io/products/scraper-api/ecommerce) (now a part of Web Scraper API). Follow this quick guide to build your e-commerce scraper while utilizing a **1-week free API trial**.

See this [blog post](https://oxylabs.io/blog/scraping-ecommerce-websites) for a complete tutorial with detailed insights and images.

- [1. Project setup](#1-project-setup)
- [2. Install dependencies](#2-install-dependencies)
- [3. Import libraries](#3-import-libraries)
- [4. Retrieve API credentials](#4-retrieve-api-credentials)
- [5. Prepare the payload](#5-prepare-the-payload)
- [6. Send a POST request to the API](#6-send-a-post-request-to-the-api)
- [7. Parse Data](#7-parse-data)
  * [Title](#title)
  * [Price](#price)
  * [Availability](#availability)
  * [All products](#all-products)
- [Full source code](#full-source-code)
- [Output](#output)

## 1. Project setup
First, you’ll have to install Python. Please download it from [here](https://www.python.org/downloads/). 

## 2. Install dependencies

```bash
pip install bs4 requests
```

## 3. Import libraries

```python
import requests
from bs4 import BeautifulSoup
from pprint import pprint
```

## 4. Retrieve API credentials
Next, you’ll have to log in to your Oxylabs account to retrieve API credentials. If you don’t have an account yet, you can simply [sign up](https://dashboard.oxylabs.io/en/registration?_gl=1*1d3w2bu*_ga*MTYxNzk4NTY4OS4xNjkzMzg1MTgy*_ga_FC1FV63ZQ4*MTcwNDg4NjM5NS4xNDEuMS4xNzA0ODk3MDc3LjYwLjAuMA..*_gcl_aw*R0NMLjE3MDIwMjkzNjMuQ2p3S0NBaUFtc3VyQmhCdkVpd0E2ZS1XUEdPNkxWQkRrS2hUT0VVUGpNQzM2QURsQ1dzWElBbXVCQUVfbGFaMDFJT3lqdndkNEhOSkRCb0Nob0FRQXZEX0J3RQ..*_gcl_au*MTM0MTc1OTcxNy4xNzAxMDY5ODYxLjQ3MDAwMTI5MC4xNzA0ODczMjI5LjE3MDQ4NzU2ODM.) for a **free trial** and go to the dashboard. There, you’ll get the necessary credentials to replace the `USERNAME` and `PASSWORD` variables in the code below:

```python
username, password = 'USERNAME', 'PASSWORD'
```

## 5. Prepare the payload

```python
url = "https://sandbox.oxylabs.io/products"
payload = {
    'source': 'universal',
    'render': 'html',
    'url': url,
}
```
## 6. Send a POST request to the API

```python
response = requests.post(
    'https://realtime.oxylabs.io/v1/queries',
    auth=(username, password),
    json=payload,
)
print(response.status_code)
```
## 7. Parse Data

```python
content = response.json()["results"][0]["content"]
soup = BeautifulSoup(content, "html.parser")
```
Let's use CSS selectors to select specific elements in the HTML file of [https://sandbox.oxylabs.io/products](https://sandbox.oxylabs.io/products), which you can inspect via **Developer Tools** on your web browser:

### Title

```python
title = soup.find('h4', {"class": "title"}).get_text(strip=True)
```
### Price

```python
price = soup.find('div', {"class": "price-wrapper"}).get_text(strip=True)
```
### Availability

```python
availability = soup.find('p', {"class": ["in-stock", "out-of-stock"]}).get_text(strip=True)
```
### All products

```python
data = []
for elem in soup.find_all("div", {"class": "product-card"}):
    title = elem.find('h4', {"class": "title"}).get_text(strip=True)
    price = elem.find('div', {"class": "price-wrapper"}).get_text(strip=True)


    availability = elem.find('p', {"class": ["in-stock", "out-of-stock"]}).get_text(strip=True)
    data.append({
        "title": title,
        "price": price,
        "availability": availability,
    })
pprint(data)
```

## Full source code

```python
import requests
from bs4 import BeautifulSoup
from pprint import pprint


username, password = 'USERNAME', 'PASSWORD'
url = "https://sandbox.oxylabs.io/products"

payload = {
    'source': 'universal',
    'render': 'html',
    'url': url,
}
response = requests.post(
    'https://realtime.oxylabs.io/v1/queries',
    auth=(username, password),
    json=payload,
)
print(response.status_code)


content = response.json()["results"][0]["content"]
soup = BeautifulSoup(content, "html.parser")


data = []
for elem in soup.find_all("div", {"class": "product-card"}):
    title = elem.find('h4', {"class": "title"}).get_text(strip=True)
    price = elem.find('div', {"class": "price-wrapper"}).get_text(strip=True)


    availability = elem.find('p', {"class": ["in-stock", "out-of-stock"]}).get_text(strip=True)
    data.append({
        "title": title,
        "price": price,
        "availability": availability,
    })
pprint(data)
```
By using the techniques described in this article, you can perform large-scale web scraping on websites that employ bot protection and CAPTCHAs.

## Output

```json
200
[
  {
    "title": "The Legend of Zelda: Ocarina of Time",
    "price": "91,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Super Mario Galaxy",
    "price": "91,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Super Mario Galaxy 2",
    "price": "91,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Metroid Prime",
    "price": "89,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Super Mario Odyssey",
    "price": "89,99 €",
    "availability": "In stock"
  },
  {
    "title": "Halo: Combat Evolved",
    "price": "87,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "The House in Fata Morgana - Dreams of the Revenants Edition -",
    "price": "83,99 €",
    "availability": "In stock"
  },
  {
    "title": "NFL 2K1",
    "price": "62,99 €",
    "availability": "In stock"
  },
  {
    "title": "Uncharted 2: Among Thieves",
    "price": "88,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Tekken 3",
    "price": "91,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "The Legend of Zelda: The Wind Waker",
    "price": "90,99 €",
    "availability": "In stock"
  },
  {
    "title": "Gran Turismo",
    "price": "86,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Metal Gear Solid 2: Sons of Liberty",
    "price": "88,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Grand Theft Auto Double Pack",
    "price": "81,99 €",
    "availability": "In stock"
  },
  {
    "title": "Baldur's Gate II: Shadows of Amn",
    "price": "91,99 €",
    "availability": "In stock"
  },
  {
    "title": "Tetris Effect: Connected",
    "price": "88,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "The Legend of Zelda Collector's Edition",
    "price": "89,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Gran Turismo 3: A-Spec",
    "price": "84,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "The Legend of Zelda: A Link to the Past",
    "price": "90,99 €",
    "availability": "In stock"
  },
  {
    "title": "The Legend of Zelda: Majora's Mask",
    "price": "91,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "The Last of Us",
    "price": "92,99 €",
    "availability": "In stock"
  },
  {
    "title": "Persona 5 Royal",
    "price": "84,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "The Last of Us Remastered",
    "price": "92,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "The Legend of Zelda: Ocarina of Time 3D",
    "price": "90,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Chrono Cross",
    "price": "88,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Gears of War",
    "price": "84,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Sid Meier's Civilization II",
    "price": "88,99 €",
    "availability": "In stock"
  },
  {
    "title": "Halo 3",
    "price": "81,99 €",
    "availability": "In stock"
  },
  {
    "title": "Ninja Gaiden Black",
    "price": "88,99 €",
    "availability": "In stock"
  },
  {
    "title": "Super Mario Advance 4: Super Mario Bros. 3",
    "price": "89,99 €",
    "availability": "Out of Stock"
  },
  {
    "title": "Jet Grind Radio",
    "price": "83,99 €",
    "availability": "In stock"
  },
  {
    "title": "Grim Fandango",
    "price": "91,99 €",
    "availability": "Out of Stock"
  }
]
```
