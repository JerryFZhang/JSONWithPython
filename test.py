import json
from pprint import pprint

with open('products.json') as data_file:
    data = json.load(data_file)

productsArr = data['products']
computerArr = []
keyboardArr = []
computerVarientsArr = []
keyboardVarientsArr = []
computerDetailsArr = []
for item in productsArr:
    string = str(item)
    index = str(productsArr.index(item))
    if "computer" in string:
        print ("Item "+ index + " is a computer.")
        computerArr.append(item)
    else:
         pass

    if "keyboard" in string:
        print ("Item "+ index + " is a keyboard.")
        keyboardArr.append(item)
    else:
         pass

print ("There is(are) " + str(len(computerArr)) + " computer(s) " + str(len(keyboardArr)) + " keyboard(s)." )

for item in computerArr:
    computerVarientsArr.append(item['variants'])
for item in keyboardArr:
    keyboardVarientsArr.append(item['variants'])

for index, item in enumerate(computerVarientsArr):
    print("-------")
    # print item
    computerDetailsArr.append(item[index])
    print computerDetailsArr[index]['grams']


for item in keyboardVarientsArr:
    print ("------")
    print item
