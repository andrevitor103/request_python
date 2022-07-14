import requests

import codes
import file

def request(code = 1):
    result = requests.get('https://jsonplaceholder.typicode.com/todos/' + str(code))

    result = result.json()
    return result

payload_array = []

codes = codes.getCodes()

for code in codes:
    result = request(code)

    payload = {
        'id': result.get('userId'),
        'title': result.get('title') 
    }

    payload_array.append(payload)
    
payload = payload_array
file.handler_file_json(payload)

# print(payload_array)
# print(payload)

# print(codes)
