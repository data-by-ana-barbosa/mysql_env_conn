# 🚀 Conexão Segura com MySQL usando Python

Este projeto mostra como se conectar de forma segura a um banco de dados MySQL usando Python. A senha do banco é salva como **variável de ambiente**, evitando exposição direta no código-fonte.

Além disso, o script utiliza:
- `os.getenv()` para buscar a senha de forma segura.
- `urllib.parse.quote()` para lidar com caracteres especiais da senha (como @, $, #).
- `SQLAlchemy` + `pymysql` para montar a engine de conexão.
- `pandas` para consultar e visualizar os dados em forma de DataFrame.
 
## ✅ Requisitos

Antes de rodar, instale as dependências:

````bash
pip install -r requirements.txt
````

## 🔒 Segurança

A senha do banco **não deve** estar hardcoded no código!  
Use variáveis de ambiente para proteger suas credenciais.

### Duas opções:

1. Criar uma variável de ambiente temporária no PowerShell:
   ````powershell
   $env:DB_PASSWORD="sua@senha$complexa#"
    ````

2. Configurar a variável de ambiente de forma permanente:  
_(No Windows: Painel de Controle > Sistema > Configurações Avançadas > Variáveis de Ambiente)_

    ````
    Nome da variável: DB_PASSWORD
    Valor da variável: sua@senha$complexa#
    ````


## 📁 Estrutura do Projeto

````bash
conexao_mysql_segura/  
├── conexao_mysql.py # Script principal  
├── requirements.txt # Dependências do projeto  
└── README.md        # Documentação  
````



## 💡 Sobre o Projeto
Este script faz parte de um estudo interno para documentar e padronizar acessos aos dados do servidor interno, com foco em **segurança, clareza e reusabilidade**.

> Nomes fictícios foram utilizados para representar o banco de dados. Nenhum dado sensível foi exposto.

- Item com hífen
* Item com asterisco
+ Item com sinal de mais
