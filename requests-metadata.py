import requests
import json

metadata_url = 'http://169.254.169.254/latest/'

def expand_json(url, array):
    output = {}
    for item in array:
        updated_url = url + item
        r = requests.get(updated_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            output[item[:-1]] = expand_json(updated_url, list_of_values)
        elif is_json(text):
            output[item] = json.loads(text)
    return output

def get_metadata():
    initial = ["meta-data/"]
    result = expand_json(metadata_url, initial)
    return result

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    metadata = get_metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    print(metadata_json)
