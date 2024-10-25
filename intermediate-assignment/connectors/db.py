from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()


db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '3306')
db_user = os.getenv('DB_USERNAME', 'root')
db_password = os.getenv('DB_PASSWORD', 'DigieSora22!')
db_name = os.getenv('DB_DATABASE', 'module7_db')


engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')


connection = engine.connect()


Session = sessionmaker(bind=engine)