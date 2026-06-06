from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#Setting up the connection to local database
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

#The args are specific to and required by SQLite in FastAPI.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class
Base = declarative_base()

#Defining the actual table
class User(Base):

    __tablename__ = "users"
    
    #Defining the columns
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    age = Column(Integer)
    
Base.metadata.create_all(bind=engine)
