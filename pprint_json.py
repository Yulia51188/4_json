import json, os

def load_data(filepath):
    with open(filepath, 'r') as file:
        json_data = json.loads(file.read())
        return json_data

def create_pretty_print_json(json_data):
    pretty_json_data = json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4)
    return pretty_json_data


if __name__ == '__main__':
    filename = input('Введите имя файла: ')
    if os.path.exists(filename):
        pretty_json = create_pretty_print_json(load_data(filename))
        print(pretty_json)
    else:
        print('Файл не существует')

