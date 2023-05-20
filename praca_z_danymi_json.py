import json
import urllib.request

url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))

    for member in data['members']:
        print(member['name'])



