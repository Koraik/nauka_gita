# Notatki - Nauka Gita
## circuit breakers
### Circuit breakers są jednym z ważnych elementó aplikacji Netflix ze względu na rozległą architekturę opartą na mikroserwisach (!!!). 
### Netflix obsługuje ogromne ilości żądań, a wiele zależy od integracji z zewnętrznymi usługami (przesyłanie strumieniowe wideo czy systemy płatności) --> circuit breakers pozwalają izolować awarie i problemy z zewnętrznymi usługami --> zapobiegając rozprzestrzenianiu się tych problemów na inne części systemu

curl --fail -X POST
-H "Content-Type: application/json"
-d '{"name":"natalia"}' https://httpbin.org/get

odpowiedź:
curl: (22) The requested URL returned error: 405

curl --fail -X GET \
-H "Content-Type: application/json"
https://httpbin.org/get

odpowiedź:
{ "args": {}, "headers": { "Accept": "/", "Content-Type": "application/json", "Host": "httpbin.org", "User-Agent": "curl/7.68.0", "X-Amzn-Trace-Id": "Root=1-64576e3e-3d2a167970b909c812d74a04" }, "origin": "156.17.55.193", "url": "https://httpbin.org/get" }

-X DELETE
-H "Content-Type: application/json" https://httpbin.org/delete

odpowiedź:
{ "args": {}, "data": "", "files": {}, "form": {}, "headers": { "Accept": "/", "Content-Type": "application/json", "Host": "httpbin.org", "User-Agent": "curl/7.68.0", "X-Amzn-Trace-Id": "Root=1-64576e95-5db01fef24773f163c3cc9ca" }, "json": null, "origin": "156.17.55.193", "url": "https://httpbin.org/delete" }
