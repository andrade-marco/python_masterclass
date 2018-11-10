from data import people, basic_plants_list, plants_list, plants_dict

if people and all([person[1] for person in people]):
    print('Sending email')
else:
    print('User must edit the list of recipients')

if any([plant.plant_type == 'Grass' for plant in plants_list]):
    print('This pack contains grass')
else:
    print('No grasses in this pack')

print('-' * 50)

if any(plants_dict[plant].plant_type == 'Cactus' for plant in plants_dict):
    print('There is Cactus in here')
else:
    print('No Cactus in here')
