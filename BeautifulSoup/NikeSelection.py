from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas as pd

url = 'https://www.nike.com/w/mens-shoes-nik1zy7ok'
html_page = urlopen(url).read()
html = soup(html_page)
product_title=html.findAll('div', {'class': 'product-card__title'})
product_price=html.findAll('div', {'class': 'product-price__wrapper'})


shoe_price = []
for i in product_price:
	spi = i.get_text().split('$')
	spi.pop(0)
	shoe_price.append(spi)

for i in shoe_price:
	if len(i)==1:
		i.append(i[0])

shoe_name = []
price_now = []
price_original = []
on_sale = []
for i in range(0, len(product_title)):
	shoe_name.append(product_title[i].get_text())
	price_now.append(float(shoe_price[i][0]))
	price_original.append(float(shoe_price[i][1]))
	if price_now[i]>=price_original[i]:
		on_sale.append(False)
	else:
		on_sale.append(True)
shoe = {
	'Name' : shoe_name,
	'Price_Now' : price_now,
	'Price_Original' : price_original,
	'On_Sale' : on_sale
}

df_shoe = pd.DataFrame(shoe)
print(df_shoe[df_shoe['On_Sale']==True])