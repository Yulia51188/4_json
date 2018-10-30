import json, os, sys

def create_formated_json_from_file(filepath):
    with open(filepath, 'r') as file:
        data = json.loads(file.read())
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        sys.exit('No argument received')
    if os.path.exists(filename):
        try:
            print(create_formated_json_from_file(filename))
        except ValueError:
            sys.exit('Data in the file is not json')
    else:
        sys.exit('File is not exists')
