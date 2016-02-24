import json
# from pprint import pprint

with open('products.json') as data_file:
    data = json.load(data_file)
    products = data['products']

computer = []
keyboard = []

for index, item in enumerate(products):
    string = str(item)
    if "computer" in string:
        computer.append(item)
    else:pass
    if "keyboard" in string:
        keyboard.append(item)
    else:pass

computerVarients = []
computerDetails = []
keyboardVarients = []
keyboardDetails = []

for index, item in enumerate(computer):
    computerVarients.append(item['variants'])
for index, item in enumerate(computerVarients):
    for index, item in enumerate(item):
        computerDetails.append(item)
for index, item in enumerate(keyboard):
    keyboardVarients.append(item['variants'])
for index, item in enumerate(keyboardVarients):
    for index, item in enumerate(item):
        keyboardDetails.append(item)

computerWeightAndPrice = []
keyboardWeightAndPrice = []
tax_rate = 1.13
for item in computerDetails:
    computerWeightAndPrice.append((float(item['grams']),float(item['price']),(item['id'])))
for item in keyboardDetails:
    keyboardWeightAndPrice.append((float(item['grams']),float(item['price']),(item['id'])))

import itertools

permutation = []

for r in itertools.product(computerWeightAndPrice, keyboardWeightAndPrice):
    permutation.append( ( int(r[0][0] + r[1][0]), round((r[0][1] + r[1][1]),4), str(r[0][2])+ " and " +str(r[1][2])))

sumAllPriceAndWeight = [sum(x) for x in zip(*((item[0],item[1],)for item in permutation))]
print sumAllPriceAndWeight

final = []
for r in itertools.product(computerWeightAndPrice,keyboardWeightAndPrice):
    final.append((sumAllPriceAndWeight[0]- int(r[0][0]) - int(r[1][0]),round((sumAllPriceAndWeight[1]- int(r[0][1]) - int(r[1][1]))*tax_rate,5)))


print final
