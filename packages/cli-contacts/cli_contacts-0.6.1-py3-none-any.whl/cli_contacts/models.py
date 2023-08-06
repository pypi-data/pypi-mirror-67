from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

if 'BLACK_BOOK_TEST' in os.environ:
    if os.environ['BLACK_BOOK_TEST'] == 'true':
        db_path = Path('sqlalchemy_test_db.db')
        engine = create_engine(f'sqlite:///{db_path}')
else:
    db_path = Path.home() / '.contacts.db'
    engine = create_engine(f'sqlite:///{db_path}')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Contacts(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    tlf = Column(String(8), nullable=False)
    email = Column(String(255), nullable=False)
    arbejdsplads = Column(String(100), nullable=False)
