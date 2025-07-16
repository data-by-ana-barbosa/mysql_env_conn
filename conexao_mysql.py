###
# Conexão segura com MySQL utilizando SQLAlchemy + pymysql.
# Evita expor a senha diretamente no código, usando variável de ambiente
# e tratando caracteres especiais com urllib.parse.quote.
###

import os                               # Acesso ao sistema operacional
import pandas as pd                     # Manipulação de dados
from sqlalchemy import create_engine    # Conexão com o banco de dados
from urllib.parse import quote          # Escapa caracteres especiais

# Recupera a senha do banco da variável de ambiente
senha = os.getenv('DB_PASSWORD')
escaped_senha = quote(senha, safe='')

# Parâmetros da conexão
db_user = 'adm_ana'
db_host = '12.34.5.67'
db_name = 'banco_da_ana'

# String de conexão
conn_str = f'mysql+pymysql://{db_user}:{escaped_senha}@{db_host}/{db_name}'
engine = create_engine(conn_str)

# Executa a query
query = 'SELECT * FROM tabela_da_ana LIMIT 50'
df = pd.read_sql(query, engine)

# Exibe os dados
print(df.head())