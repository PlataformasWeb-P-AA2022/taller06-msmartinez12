from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Paises

import requests
import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

# leer el archivo de datos


engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

response = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
response_json = response.json()


# archivo.json()

documentos = response_json



for d in documentos:
    p = Paises(cldr_display_name=d["CLDR display name"], capital=d['Capital'], continent=d['Continent'], \
            dial=d['Dial'], geoname_id=d["Geoname ID"], itu=d['ITU'],language=d['Languages'], is_independent=d['is_independent'])
    session.add(p)

# confirmar transacciones



session.commit()


