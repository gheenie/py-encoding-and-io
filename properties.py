from xml.etree.ElementTree import parse
from xml.etree import ElementTree
tree = parse('data/properties.xml')

for sale in tree.findall('sale'):
    for detached in sale.findall('detached'):
        index_highest_sqft = 0
        highest_sqft = 0
        for i, home in enumerate(detached):
            current_sqft = int(home[4].text[0:4])
            if current_sqft > highest_sqft:
                index_highest_sqft = i 
                highest_sqft = current_sqft

        print(detached[index_highest_sqft][0].text)
      

for sale in tree.findall('sale'):
    for bungalow in sale.findall('bungalow'):
       print(bungalow[2][1].text)


for rent in tree.findall('rent'):
    for flat in rent.findall('flat'):
        print(flat[0][3].text)

bungalows = []

for sale in tree.findall('sale'):
    for bungalow in sale.findall('bungalow'):
        for each_bungalow in bungalow:
            bungalows.append(each_bungalow)

for rent in tree.findall('rent'):
    for bungalow in rent.findall('bungalow'):
        for each_bungalow in bungalow:
            bungalows.append(each_bungalow)

bungalows_in_string =[]

for bungalow in bungalows:
    bungalow_in_string = ElementTree.tostring(bungalow, encoding='unicode')
    bungalows_in_string.append(bungalow_in_string)


print(bungalows_in_string)