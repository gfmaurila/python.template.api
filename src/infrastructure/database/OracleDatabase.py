import oracledb
from core.Config import GetSettings

settings = GetSettings()

# Monta a string de conexão
dsn = f"{settings.ORACLE_HOST}:{settings.ORACLE_PORT}/{settings.ORACLE_SID}"

def GetOracleConnection():
    return oracledb.connect(
        user=settings.ORACLE_USER,
        password=settings.ORACLE_PASSWORD,
        dsn=dsn
    )
