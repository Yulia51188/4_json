import json, os, sys

def load_data(filepath):
    with open(filepath, 'r') as file:
        yield json.loads(file.read())


def create_formated_json(data_list):
    formated_json_data = json.dumps(data_list, ensure_ascii=False, sort_keys=True, indent=4)
    return formated_json_data


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('No argument get')
        sys.exit()
    if os.path.exists(filename):
        print(create_formated_json(list(load_data(filename))))
    else:
        print('File is not exists')

