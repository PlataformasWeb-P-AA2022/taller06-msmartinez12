from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Paises

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la entidad docentes
paises = session.query(Paises).all() # [docente1, docente2, docente3]

# Se recorre la lista a través de un ciclo
# repetitivo for en python


# Obtener todos los registros de
# la tabla docentes que tengan como valor en
# el atributo especifico
paises_dos = session.query(Paises).filter(Paises.continent=="NA").all()
print(docentes_dos)

print("--------------------------------")

