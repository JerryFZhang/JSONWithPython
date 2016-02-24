import json
# from pprint import pprint

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

for item in computerArr:
    computerVarientsArr.append(item['variants'])

keyboardVarientsArr = []

for item in keyboardArr:
    keyboardVarientsArr.append(item['variants'])

computerDetailsArr = []

for index, item in enumerate(computerVarientsArr):
    for index, item in enumerate(item):
        computerDetailsArr.append(item)

keyboardDetailsArr = []

for index, item in enumerate(keyboardVarientsArr):
    for index, item in enumerate(item):
        keyboardDetailsArr.append(item)

computerWeightArr = []
computerPriceArr = []

for item in computerDetailsArr:
    computerWeightArr.append(float(item['grams']))
    computerPriceArr.append(float(item['price']))

keyboardWeightArr = []
keyboardPriceArr = []

for item in keyboardDetailsArr:
    keyboardWeightArr.append(float(item['grams']))
    keyboardPriceArr.append(float(item['price']))

# print all the arrays.
print computerPriceArr
print computerWeightArr
print keyboardPriceArr
print keyboardWeightArr
