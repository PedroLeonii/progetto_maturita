from base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlaclhemy import Integer, Text, String, ForeignKey, Boolean

Base = declarative_base()

class Utenti(Base):
    __tablename__='utenti'

    id = Column('username', String(200), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    mail = Column(String(255), unique=True, nullable=False)

class Bot(Base):
    __tablename__='botManagers'

    id = Column('token', String(47), primary_key=True)
    username = Column(String(200), ForeignKey('utenti.username'))
    isalive = Column(Boolean, default=True)
