from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///budget.db')
Session = sessionmaker(bind=engine)

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    amount = Column(Integer, nullable=False)

def initialize_database():
    Base.metadata.create_all(engine)
