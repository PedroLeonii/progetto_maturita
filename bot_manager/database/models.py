from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

Base = declarative_base()

class Bot(Base):
    __tablename__= 'bot'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(47), nullable=False, unique=True)
    isalive = Column(Boolean, default=True)
    id_utente = Column(Integer, ForeignKey('utenti.id'))
    comandi = relationship('Comandi')

    def get_command(self, nome):
        for comando in self.comandi:
            if comando.nome == nome:
                return comando


class TipiComando(Base):
    __tablename__ = 'tipicomando'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(300), nullable=False, unique=True)


class Comandi(Base):
    __tablename__= 'comandi'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(300), nullable=False)
    id_tipo = Column(Integer, ForeignKey('tipicomando.id'))
    id_bot = Column(Integer, ForeignKey('bot.id'))
    tipo_comando = relationship('TipiComando', uselist=False)
    help_msg = Column(String(500), nullable=False)

    def get_tipo(self):
        return self.tipo_comando.tipo

class Testuali(Base):
    __tablename__='testuali'

    id = Column(Integer, ForeignKey('comandi.id'), primary_key=True)
    risposta = Column(String(500), nullable=False)
    num_argomenti = Column(Integer)

    def controllo_args(self, list_args):
        if len(list_args) == self.num_argomenti:
            return True
        return False
        
class Api(Base):
    __tablename__='api'

    id = Column(Integer, ForeignKey('comandi.id'), primary_key=True)
    funzione = Column(String(40), nullable=False)




