import json
import urllib.request

url_strony = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'

try:
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    json_data = json.loads(data)
    print(json_data)

except Exception as e:
    print(f'Wystapił błąd podczas pobierania lub przetwarzania pliku JSON :c : {str(e)}')