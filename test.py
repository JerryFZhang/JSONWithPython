import json
import itertools

with open('products.json') as data_file:
    data = json.load(data_file)
    products = data['products']

computer = []
keyboard = []

# Find all the computer and keyboards and append them it to new list for the next step.
for index, item in enumerate(products):
    string = str(item)
    if "computer" in string:
        computer.append(item)
    else:pass
    if "keyboard" in string:
        keyboard.append(item)
    else:pass


computer_varients = []
computer_varient_details = []
keyboard_varients = []
keyboard_varient_details = []

# Find all the varients and apppend them into a new array.
for index, item in enumerate(computer):
    computer_varients.append(item['variants'])
for index, item in enumerate(computer_varients):
    for index, item in enumerate(item):
        computer_varient_details.append(item)
for index, item in enumerate(keyboard):
    keyboard_varients.append(item['variants'])
for index, item in enumerate(keyboard_varients):
    for index, item in enumerate(item):
        keyboard_varient_details.append(item)


computer_weight_price = []
keyboard_weight_price = []

tax_rate = 1.13 # For taxable items.

# Find price, weight and unique item id. Parse them as a tuple list.
for item in computer_varient_details:
    computer_weight_price.append((float(item['grams']),float(item['price']),(item['id'])))
for item in keyboard_varient_details:
    keyboard_weight_price.append((float(item['grams']),float(item['price']),(item['id'])))

#Find all the permutations between a keyboard and computer.
permutation = []
for r in itertools.product(computer_weight_price, keyboard_weight_price):
    permutation.append( ( int(r[0][0] + r[1][0]), round((r[0][1] + r[1][1]),4), str(r[0][2])+ " and " +str(r[1][2])))

# Add them up and see if the total price is over $100.
sum_price_weight = [sum(x) for x in zip(*((item[0],item[1],)for item in permutation))]
print ("The total weight of all combinations is " + str(sum_price_weight[0]) + " grams and the total price is "+ str(round(sum_price_weight[1],2)) +" dollars after tax.")

# Subtrack one combination from the overweighted combinations and see which one is smaller than 100.
sub_result = []
for r in itertools.product(computer_weight_price,keyboard_weight_price):
    sub_result.append((sum_price_weight[0]- int(r[0][0]) - int(r[1][0]),round((sum_price_weight[1]- int(r[0][1]) - int(r[1][1]))*tax_rate,2)))

# Print All the combination that is less than 100,000g, aka, 100kg.
can_carry = []
for item in sub_result:
    if (item[0] <= 100000):
        can_carry.append(item)
    else:pass

print "There are " + str(len(can_carry)) +" different sets of "+str(len(permutation) - 1)+" combinations under 100kg."
print ("Lighest under 100kg:" + str(min(can_carry, key = lambda t: t[0])))
print ("Cheapest under 100kg:" + str(min(can_carry, key = lambda t: t[1])))
