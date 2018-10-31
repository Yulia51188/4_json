import json
import os
import sys


def load_python_object_from_file(filepath):
    with open(filepath, 'r') as file:
        str_data = file.read()
    try:
        python_object = json.loads(str_data)
        return python_object
    except ValueError:
        return None


def get_formatted_json(python_object):
    return json.dumps(python_object, ensure_ascii=False,
                      sort_keys=True, indent=4)


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        exit('No argument received')
    filename = sys.argv[1]
    if not os.path.exists(filename):
        exit('File is not exists')
    python_object = load_python_object_from_file((filename))
    if python_object is None:
        exit('Data in the file is not json or file is empty')
    print(get_formatted_json(python_object))
