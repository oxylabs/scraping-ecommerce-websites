import requests
from bs4 import BeautifulSoup
from pprint import pprint


username, password = 'USERNAME', 'PASSWORD'
url = "https://sandbox.oxylabs.io/products"

payload = {
    'source': 'universal_ecommerce',
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
