# Estabelecendo conexão com MySQL

# É necessário instalar um pacote específico para trabalhar com o banco MySQL (mysql-connector)
# Para estabelecer a conexão precisamos das informações de porta, usuario, senha, host

from mysql.connector import connect

con = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='med111202',
)

print(type(con))

# Realizamos as operações e depois fechamos a conexão

con.close()
