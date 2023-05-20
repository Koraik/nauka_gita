# Notatki - Nauka Gita
## circuit breakers
### Circuit breakers są jednym z ważnych elementó aplikacji Netflix ze względu na rozległą architekturę opartą na mikroserwisach (!!!). 
### Netflix obsługuje ogromne ilości żądań, a wiele zależy od integracji z zewnętrznymi usługami (przesyłanie strumieniowe wideo czy systemy płatności) --> circuit breakers pozwalają izolować awarie i problemy z zewnętrznymi usługami --> zapobiegając rozprzestrzenianiu się tych problemów na inne części systemu
