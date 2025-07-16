import sqlalchemy
from sqlalchemy import text
from core.Config import GetSettings
from core.Database import Base, engine

def create_database_if_not_exists():
    settings = GetSettings()
    database_url = settings.SQLALCHEMY_DATABASE_URL
    database_name = database_url.rsplit("/", 1)[-1]

    # Conexão com o banco master
    master_url = database_url.rsplit("/", 1)[0] + "/master"
    engine_master = sqlalchemy.create_engine(master_url, isolation_level="AUTOCOMMIT")

    with engine_master.connect() as conn:
        result = conn.execute(
            text("SELECT COUNT(*) FROM sys.databases WHERE name = :name"),
            {"name": database_name}
        )
        exists = result.scalar()
        if not exists:
            conn.execute(text(f"CREATE DATABASE [{database_name}]"))
            print(f"Banco de dados '{database_name}' criado com sucesso.")
        else:
            print(f"Banco de dados '{database_name}' já existe.")

def create_all_tables_if_not_exists():
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso (caso não existam).")
