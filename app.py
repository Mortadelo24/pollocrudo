# python -m venv env //crear un entorno
# inclopeto la activacion del entorno
# ejemplos en https://drive.google.com/drive/folders/1fupyz03n6XqOZiYsiOzF6gJ9fWEDc0QY


import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
load_dotenv()

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL no esta disponible")

# set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


nombre= "Juan"
apellido= 'Larios'
query = text("INSERT INTO registro(nombre, apellidos) VALUES(:nombre, :apellidos)")

db.execute(query, {'nombre': nombre, 'apellidos': apellido})

db.commit()
