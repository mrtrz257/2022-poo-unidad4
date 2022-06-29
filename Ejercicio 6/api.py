import json
from urllib.request import urlopen

class API:
    __resultado=None
    def __init__(self):
        self.__resultado=None
    def run(self, ciudad):
        url_template1 = 'https://api.openweathermap.org/data/2.5/weather?q='+ciudad+'&units=metric&appid=a4a4100e7ae5ed9f98787bf19137a91c'
        url_template = url_template1.replace(" ", "%20")
        print(url_template)
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    def getResultado(self):
        return self.__resultado
