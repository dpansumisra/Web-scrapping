import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%252"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

data = {'Product Name': [], 'Product URL': [], 'Price': [], 'Rating': [], 'No. of Reviews': []}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('div', {'data-component-type': 's-search-result'})


for result in results:
    product_name = result.find('span', class_='a-text-normal').text.strip()
    product_url = "https://www.amazon.in" + result.find('a', class_='a-link-normal')['href']
    product_price = result.find('span', class_='a-price-whole').text.strip()
    rating_element = result.find('span', {'class': 'a-icon-alt'})
    rating = rating_element.text.strip() if rating_element else "N/A"
    review = result.find('span',{'class':'a-size-base s-underline-text'})
    reviews = review.text.strip() if review else "N/A"
    
    
    data['Product Name'].append(product_name)
    data['Product URL'].append(product_url)
    data['Price'].append(product_price)
    data['Rating'].append(rating)
    data['No. of Reviews'].append(reviews)

df = pd.DataFrame.from_dict(data)
df.to_csv('data.csv', index=False)
