from json import load


def database_cursor(*args):
    with open('data/cities_data.json') as file:
        file = load(file)
        if not args:
            return file
        for state in file[0]:
            if args[0].title() == state:
                return {f'{state}': file[0][state]}
            else:
                return None