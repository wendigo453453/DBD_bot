import json

with open('killer_icons.txt', 'r') as file:
    links = [line.rstrip('\n') for line in file.readlines()]

Killer_random_p_b = {}

for link in links:
    name = link.split('icon-Perks-')[1].split('.')[0]
    url = link

    Killer_random_p_b[name] = url


with open('Killer_random_p_b.json', 'w') as file:
    json.dump(Killer_random_p_b, file)