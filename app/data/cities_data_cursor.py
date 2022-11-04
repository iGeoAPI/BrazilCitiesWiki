from json import load


def json_cursor(*args, scope: str = None):
    if scope == 'states':
        with open('data/cities_data.json') as file:
            file = load(file)[0]
            if not args:
                return file
            for state in file:
                if args[0].lower() == state.lower():
                    return {f'{state}': file[state]}
            return None

    def iter_func():
        with open('data/cities_data.json') as file:
            file = load(file)[0]
            for state in file:
                for city in file[state]:
                    yield city

    return iter_func()
