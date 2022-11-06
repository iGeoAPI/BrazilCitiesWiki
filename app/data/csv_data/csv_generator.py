from json import load

values = []

# TODO: Implement a better version of code for data collection
with open('json_data/cities_data.json') as file:
    file = load(file)[0]
    print(dir(file))
    for state in file:
        cities = file[state]
        for city in cities:
            for value in city.values():
                values += [value]
            values = ','.join(map(str, values))
            csv_file = open('cities_data.csv', 'a')
            csv_file.write(values)
            csv_file.write('\n')
            values = []
            csv_file.close()
