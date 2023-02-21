import json
from operator import itemgetter
import csv

with open('data/cars.json', 'r', encoding='utf-16') as file:
    read_cars = json.load(file)

cars = read_cars['Cars']

#print(cars)

makes = [car['make'] for car in cars]

#print(set(makes))

cars_under_20 = [car for car in cars if 2023 - car['year'] < 20]
cars_under_20_by_age = sorted(cars_under_20, key = itemgetter('year'), reverse=True)

#print(cars_under_20_by_age)

dream_car = {
    "vin": "2C3CA1CV4AH46567Z",
    "make": "Toyota",
    "model": "Camry",
    "year": 2010,
    "colour": "Red"
}

cars.append(dream_car)

# with open('data/cars.json', 'w', encoding='utf-16') as file:
#     json.dump(read_cars, file)

red_ford_tempo = next(car for car in cars if car['make'] == 'Ford' and car['model'] == 'Tempo' and car['colour'] == 'Red')

red_ford_tempo['year'] = 1985

#print(cars)

for car in cars:
    car['fuel'] = 'petrol'

    #print(car)

#print(cars)

# csv_columns = cars[0].keys()
# csv_content = ','.join(csv_columns) + '\n'

# for car in cars:
#     car['year'] = str(car['year'])

#     values = car.values()
#     row = ','.join(values) + '\n'
    
#     csv_content += row

# with open('data/cars.csv', 'w', encoding='utf-8') as file:
#     file.write(csv_content)

with open('data/cars.csv', 'w', newline='') as file:
    csv_columns = cars[0].keys()
    print(csv_columns)
    writer = csv.DictWriter(file, fieldnames=csv_columns)

    writer.writeheader()

    for car in cars:
        writer.writerow(car)