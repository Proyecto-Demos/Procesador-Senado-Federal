from urllib import request
from bs4 import BeautifulSoup

while(True):
    req = request.get("https://www.senado.gob.mx/64/votacion/1")
    soup = BeautifulSoup(req, "html.parser")

