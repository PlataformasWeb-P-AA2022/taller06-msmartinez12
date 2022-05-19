from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Paises

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

print("--------------------------------")

paises = session.query(Paises.cldr_display_name, Paises.capital).filter(or_(Paises.cldr_display_name.like("%uador%"),Paises.continent.like("%ito%") )).order_by(Paises.capital).all()
print(paises)

print("--------------------------------")

