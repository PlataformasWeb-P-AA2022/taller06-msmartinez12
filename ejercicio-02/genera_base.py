from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
# engine = create_engine('sqlite:///demobase.db')

engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):

    __tablename__ = 'paises'

    id = Column(Integer, primary_key=True)
    cldr_display_name = Column(String(200))
    capital = Column(String(200))
    continent = Column(String(200))
    dial = Column(String(200)) 
    geoname_id = Column(String(200)) 
    itu = Column(String(200)) 
    language = Column(String(200)) 
    is_independent = Column(String(200)) 


    def __repr__(self):
        return "Pais: Nombre=%s Capital=%s Continente:%s Dial:%s Geoname ID:%s ITU:%s Lenguaje:%s Independiente:%s" % (
                          self.cldr_display_name,
                          self.capital,
                          self.continent,
                          self.dial,
                          self.geoname_id,
                          self.itu,
                          self.language,
                          self.is_independent
                          )

Base.metadata.create_all(engine)

