import oracledb

# Inicializa o cliente Oracle com o caminho correto (sem force)
oracledb.init_oracle_client(lib_dir=r"F:\Work\python\oracle\instantclient_19_27\instantclient_19_27")

# Conexão de teste
try:
    connection = oracledb.connect(
        user="system",
        password="oracle",
        dsn="localhost:1521/xe"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM HR.REGIONS")

    print("Regiões:")
    for row in cursor:
        print(row)

    cursor.close()
    connection.close()

except oracledb.DatabaseError as e:
    print("Erro ao conectar no banco Oracle:")
    print(e)


# python test_oracle.py
