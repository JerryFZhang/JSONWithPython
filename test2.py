import json
import itertools

with open('products.json') as data_file:
    data = json.load(data_file)
    products = data['products']


products_temp = []

for index, item in enumerate(products):
    products_temp.append(item)
products = products_temp
products_temp = [] # delete the variable

for index, item in enumerate(products):
    products_temp.append(item)

products = products_temp
products_temp = None
computers,keyboards = [],[]

for index, item in enumerate(products):
    if item ['product_type'] == 'Computer':
        computers.append((item['title'],item['options']))
        print item
        print "====="

    else: pass
    if item ['product_type'] == 'Keyboard':
        keyboards.append(item)
        print item
        print "==="
    else: pass

print computers
