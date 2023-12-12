import xml.etree.ElementTree as ET

import requests as re

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = re.get(url)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)

table_name = root.find(".//Table").text
print(table_name)

rates = root.findall('.//Rate')
print(type(rates))
for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"Currency: {currency}: code: {code} mid: {mid}")
