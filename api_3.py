import time
import socket
import json
import urllib.request
from urllib.error import URLError, HTTPError

url = 'https://httpbin.org/delay/2'
data = {
    'name': 'natalia'
}

headers = {
    'Content-Type': 'application/json'
}

timeout = 1
max_retries = 3
backoff_factor = 2

retry_count = 0
retry_delay = 1

while retry_count < max_retries:
    try:
        req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), headers)
        with urllib.request.urlopen(req, timeout=timeout) as response:
            response_data = response.read().decode('utf-8')
            json_data = json.loads(response_data)
            print(json_data)
            break
    except (URLError, HTTPError, socket.timeout) as e:
        print(f'Ups błąd podczas wywoływania serwisu :C Przepraszamy :c: {str(e)}')
        print(f'Ponawianie ({retry_count + 1}/{max_retries})...')
        time.sleep(retry_delay)
        retry_count += 1
        retry_delay *= backoff_factor

