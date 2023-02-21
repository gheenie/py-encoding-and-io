import csv
from operator import itemgetter
import json

pizzas = []
with open('data/pizza.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        pizzas.append(row)
#print(pizzas)

capri_pizza = [pizza['Description'] for pizza in pizzas if pizza['Pizza'] == 'Capri']

ingredients = capri_pizza[0]
ingredients = ingredients.split(', ')
for ingredient in ingredients:
    #print(ingredient)
    pass

under_nine = [pizza for pizza in pizzas if float(pizza['Cost'][1:]) < 9]
under_nine_by_cost = sorted(under_nine, key = itemgetter('Cost'))

#print(under_nine_by_cost) 

new_pizza = 'BBQ Chicken,£10.70,"Cheese, tomato, BBQ sauce, onions and chicken",950kcal\n'

# with open('data/pizza.csv', 'a', encoding='utf-8') as file:
#     file.write(new_pizza)

for pizza in pizzas:
    updated_cost = float(pizza['Cost'][1:])
    updated_cost *= 1.1
    updated_cost = round(updated_cost, 2)
    updated_cost = '{:0.2f}'.format(updated_cost)
    updated_cost = '£' + str(updated_cost)
    pizza['Cost'] = updated_cost
    print(pizza)

json_pizzas = { 'pizzas': pizzas }

with open('data/pizzas.json', 'w', encoding='utf-8') as file:
    json.dump(json_pizzas, file)
