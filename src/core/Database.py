# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import declarative_base
# import os
# import urllib
# from dotenv import load_dotenv

# load_dotenv()

# Base = declarative_base()

# # Leitura das variáveis de ambiente
# server = os.getenv("SQLSERVER_HOST", "localhost")
# port = os.getenv("SQLSERVER_PORT", "1433")
# database = os.getenv("SQLSERVER_DB", "api.python.db")
# username = os.getenv("SQLSERVER_USER", "sa")
# password = os.getenv("SQLSERVER_PASSWORD", "@Poc2Minimal@Api")

# # String para conexão com o banco principal
# params_db = urllib.parse.quote_plus(
#     f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#     f"SERVER={server},{port};"
#     f"DATABASE={database};"
#     f"UID={username};"
#     f"PWD={password};"
#     f"TrustServerCertificate=yes"
# )

# # String para conexão com o banco 'master' para criar banco, se necessário
# params_master = urllib.parse.quote_plus(
#     f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#     f"SERVER={server},{port};"
#     f"DATABASE=master;"
#     f"UID={username};"
#     f"PWD={password};"
#     f"TrustServerCertificate=yes"
# )

# engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params_db}", future=True)
# engine_master = create_engine(f"mssql+pyodbc:///?odbc_connect={params_master}", future=True)

# # Importa modelos para registrar no metadata
# import infrastructure.database.models.UserModel

# def create_database_if_not_exists():
#     with engine_master.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
#         conn.execute(text(f"IF DB_ID('{database}') IS NULL CREATE DATABASE [{database}]"))

# def create_all_tables_if_not_exists():
#     Base.metadata.create_all(bind=engine)

# __all__ = ["engine", "Base"]




from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
import os
import urllib
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

# Leitura das variáveis de ambiente
server = os.getenv("SQLSERVER_HOST", "localhost")
port = os.getenv("SQLSERVER_PORT", "1433")
database = os.getenv("SQLSERVER_DB", "api.python.db")
username = os.getenv("SQLSERVER_USER", "sa")
password = os.getenv("SQLSERVER_PASSWORD", "@Poc2Minimal@Api")

# String para conexão com o banco principal
params_db = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server},{port};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"TrustServerCertificate=yes"
)

# String para conexão com o banco 'master'
params_master = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server},{port};"
    f"DATABASE=master;"
    f"UID={username};"
    f"PWD={password};"
    f"TrustServerCertificate=yes"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params_db}", future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # <-- Adicionado
engine_master = create_engine(f"mssql+pyodbc:///?odbc_connect={params_master}", future=True)

# Importa modelos
import infrastructure.database.models.UserModel

def create_database_if_not_exists():
    with engine_master.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        conn.execute(text(f"IF DB_ID('{database}') IS NULL CREATE DATABASE [{database}]"))

def create_all_tables_if_not_exists():
    Base.metadata.create_all(bind=engine)

__all__ = ["engine", "Base", "SessionLocal"]  # <-- Exporta SessionLocal
