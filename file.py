import json


def write_file(file, contents = ''):
    file.write(contents + '\n')

def handler_file(contents = '', file_name = 'results.txt'):
        f = open(file_name, 'w')
        write_file(f, contents)
        f.close()

def handler_file_json(contents = '', file_name = 'results.json'):
    with open(file_name, 'w') as fp:
        json.dump(contents, fp, indent=2)
    fp.close()