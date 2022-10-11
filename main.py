from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.dermstore.com/is-clinical-active-serum-30ml/11291956.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

product_name = soup.find('h1', class_='productName_title').text
brand_name = soup.find(class_='productBrandLogo_image').get('title')
price = soup.find('p', class_='productPrice_price').text.strip()
main_image_url = soup.find('img', class_='athenaProductImageCarousel_image').get('src')
product_overview_block = soup.find("div", {"id": "product-description-content-lg-2"}).text.strip()
how_to_use_block = soup.find("div", {"id": "product-description-content-lg-15"}).text.strip()
col_names = ['Product_Name',
             'Brand_Name',
             'Price',
             'Main_Image_Url',
             'ProductOverviewBlock',
             'HowToUseBlock'
             ]

parameters = pd.DataFrame([[product_name, brand_name, price, main_image_url, product_overview_block, how_to_use_block]],
                          columns=['Product_Name', 'Brand_Name', 'Price',
                                   'Main_Image_Url', 'Product_Overview_Block', 'How_To_Use_Block'])

parameters.to_csv('catalog.csv', mode='a', header=False)

catalog_data = pd.read_csv('catalog.csv')
print(catalog_data.head())
