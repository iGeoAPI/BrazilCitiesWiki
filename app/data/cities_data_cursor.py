from json import load


def json_cursor(*args):
    with open('data/cities_data.json') as file:
        file = load(file)
        if not args:
            return file[0]
        for state in file[0]:
            if args[0].lower() == state.lower():
                return {f'{state}': file[0][state]}
        return None
