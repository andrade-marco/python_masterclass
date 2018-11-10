cities = ['Adelaide', 'Alice Springs', 'Darwin', 'Melbourne', 'Sydney']

with open('../data/cities.txt', 'w') as cityData:
    for city in cities:
        print(city, file=cityData)
 
