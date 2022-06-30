import json
from urllib.request import urlopen

class API:
    __resultado=None
    def __init__(self):
        self.__resultado=None
    def run(self, provincia):
        nombre = provincia.getNombre()
        ciudad = nombre.replace(" ", "%20")
        url_template = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a4a4100e7ae5ed9f98787bf19137a91c'.format(ciudad)
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    def getResultado(self):
        return self.__resultado
