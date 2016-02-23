import json
from pprint import pprint

with open('products.json') as data_file:
    data = json.load(data_file)

productsArr = data['products']
computerArr = []
keyboardArr = []

for index, item in enumerate(productsArr):
    string = str(item)
    if "computer" in string:
        computerArr.append(item)
    else:
         pass
    if "keyboard" in string:
        keyboardArr.append(item)
    else:
         pass

computerVarientsArr = []
keyboardVarientsArr = []
for item in computerArr:
    computerVarientsArr.append(item['variants'])
for item in keyboardArr:
    keyboardVarientsArr.append(item['variants'])

computerDetailsArr = []
keyboardDetailsArr = []

for index, item in enumerate(computerVarientsArr):
    for index, item in enumerate(item):
        computerDetailsArr.append(item)

for index, item in enumerate(keyboardVarientsArr):
    for index, item in enumerate(item):
        keyboardDetailsArr.append(item)


for item in computerDetailsArr:
    print (item['grams'])
    print (item['price'])
