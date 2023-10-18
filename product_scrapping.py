import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo1MTA4MTczNTQ4NTM1NjU1OjE2OTc2MDE0MjM6c3BfYXRmOjIwMTM1MzM0NjYzMjk4OjowOjo&url=%2FArctic-Fox-Backpack-Charging-Laptop%2Fdp%2FB089QBD333%2Fref%3Dsr_1_1_sspa%3Fcrid%3D2M096C61O4MLT%26keywords%3Dbags%26qid%3D1697601423%26sprefix%3Dba%252Caps%25252%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('div', {'data-component-type': 's-search-result'})

descriptions = soup.find_all('span', class_='a-text-bold') 
for description in descriptions:
    description = description.get_text(strip=True)      
    print(description)
