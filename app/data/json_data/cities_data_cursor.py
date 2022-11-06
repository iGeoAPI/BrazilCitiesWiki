from json import load


def json_cursor(*args, scope: str = None):
    if scope == 'states':
        with open('data/json_data/cities_data.json') as file:
            file = load(file)[0]
            if not args:
                return file
            for state in file:
                if args[0].lower() == state.lower():
                    return {f'{state}': file[state]}
            return None

# TODO: Guarantee the cities call endpoint is properly working
    def iter_func():
        with open('data/json_data/cities_data.json') as file:
            file = load(file)[0]
            if not args:
                for state in file:
                    for city in file[state]:
                        yield city
            else:
                for state in file:
                    for city in file[state]:
                        if city == args[0]:
                            yield city
                        else:
                            return None
    return iter_func()
