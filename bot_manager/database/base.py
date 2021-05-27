from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:masterkey@localhost:3306/BOT_APPLICATION')

Session = sessionmaker(bind=engine)
