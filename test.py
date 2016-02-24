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

for item in computer:
    computerVarients.append(item['variants'])

keyboardVarients = []

for item in keyboard:
    keyboardVarients.append(item['variants'])

computerDetails = []

for index, item in enumerate(computerVarients):
    for index, item in enumerate(item):
        computerDetails.append(item)

keyboardDetails = []

for index, item in enumerate(keyboardVarients):
    for index, item in enumerate(item):
        keyboardDetails.append(item)

computerWeight = []
computerPrice = []

for item in computerDetails:
    computerWeight.append(float(item['grams']))
    computerPrice.append(float(item['price']))

keyboardWeight = []
keyboardPrice = []

for item in keyboardDetails:
    keyboardWeight.append(float(item['grams']))
    keyboardPrice.append(float(item['price']))

# print all the arrays.
print computerPrice
print computerWeight
print keyboardPrice
print keyboardWeight


import itertools
# for r in itertools.product(a, b): print r[0] + r[1]
