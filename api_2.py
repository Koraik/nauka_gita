import urllib.request
import json

url = 'https://httpbin.org/post'

data = {
    'name': 'natalia'
}
headers = {
    'Content-Type': 'application/json'
}

try:
    req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), headers)
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        json_data = json.loads(response_data)
        print(json_data)

except Exception as e:
    print(f'Ups błąd podczas wywoływania serwisu :C Przepraszamy :c: {str(e)}')
