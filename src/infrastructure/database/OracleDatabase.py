import oracledb
from core.Config import GetSettings

settings = GetSettings()

if oracledb.is_thin_mode():
    oracledb.init_oracle_client(lib_dir=settings.ORACLE_LIB_DIR)

def GetOracleConnection():
    dsn = f"{settings.ORACLE_HOST}:{settings.ORACLE_PORT}/{settings.ORACLE_SID}"
    return oracledb.connect(
        user=settings.ORACLE_USER,
        password=settings.ORACLE_PASSWORD,
        dsn=dsn
    )
