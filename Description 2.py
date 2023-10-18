import requests
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_csv('data.csv')

descriptions = list(data.iloc[:, 1])

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

description_texts = []

for description_url in descriptions:
    r = requests.get(description_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    descriptions = soup.find_all('li', class_='a-spacing-mini')
    for description in descriptions:
        description_text = description.get_text(strip=True)
        description_texts.append(description_text)

description_data = pd.DataFrame({'Item Description': description_texts})

merged_data = data.join(description_data)

merged_data.to_csv('merged_data.csv', index=False)
