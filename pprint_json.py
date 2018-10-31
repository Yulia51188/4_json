import json, os, sys


def create_formated_json_from_file(filepath):
    with open(filepath, 'r') as file:
        python_object = json.loads(file.read())
    return json.dumps(python_object, ensure_ascii=False,
                      sort_keys=True, indent=4)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        sys.exit('No argument received')
    if not os.path.exists(filename):
        sys.exit ( 'File is not exists' )
    try:
        print(create_formated_json_from_file(filename))
    except ValueError:
        sys.exit('Data in the file is not json')
