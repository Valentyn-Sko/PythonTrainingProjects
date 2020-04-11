import pandas
import requests
from bs4 import BeautifulSoup


def replace_str(str):
    return str.replace('\n', '').replace('  ', '')

http2="https://www.century21.com/real-estate/rock-spring-ga/LCGAROCKSPRING/"
http_source = "https://www.century21.com/real-estate/rocks-md/LCMDROCKS/"

r = requests.get(http2)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
properties = soup.find_all("div", {'class': 'property-card'})

l = []

for item in properties:
    price = replace_str(item.find("a", {'class': 'listing-price'}).text)
    address = replace_str(item.find('div', {'class': 'property-address-info'}).text)
    try:
        beds = item.find('div', {'class': 'property-beds'}).find('strong').text
    except AttributeError:
        beds = None

    try:
        baths = item.find('div', {'class': 'property-baths'}).find('strong').text
    except AttributeError:
        baths = None

    try:
        half_baths = item.find('div', {'class': 'property-half-baths'}).find('strong').text
    except AttributeError:
        half_baths = None
    try:

        property_sqft = item.find('div', {'class': 'property-sqft'}).find('strong').text
    except AttributeError:
        property_sqft = None

    d = {'Price': price, 'Address': address, 'Beds': beds, 'Baths': baths, 'Half-baths': half_baths,
         'Square': property_sqft}
    print(d)
    l.append(d)

df = pandas.DataFrame(l)
print(df)
df.to_csv('Output.csv')




