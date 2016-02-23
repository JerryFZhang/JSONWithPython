import json
from pprint import pprint

with open('products.json') as data_file:
    data = json.load(data_file)

productsArr = data['products']
computerArr = []
keyboardArr = []

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
    print item

for item in keyboardArr:
    print item
