# docker - container - iso - para usar sem instalar

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Definindo parãmetros para acesso ao banco de dados

db_user = "user"
db_password = "password_user"
db_name = "meu_banco"
db_host = "localhost"
db_port = "3306"

# Endereço (URL) para conexão com banco de dados.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#criando banco de dados.
db = create_engine(DATABASE_URL)

#Criando conexão com banco de dados
Session = sessionmaker(bind=db)
session = Session()

#Gerenciando conexão com banco de dados.
@contextmanager
def get_db():
    db = Session()
    try:
        yield db #Realiza tentativa de operação no BD
        db.commit() #Salvando no BD.
    except Exception as erro:
        db.rollback() # Caso ocorra algum erro, desfaz alterações no BD.
        raise erro # Caso ocorra algum erro, mostra mensagem de erro no terminal
    finally:
        db.close() # Fecha conexão com BD.