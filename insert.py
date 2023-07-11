import mysql.connector

# Conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host='curso-newrelic.cr4dgmgjfzt4.us-east-1.rds.amazonaws.com',
    user='root',
    password='Sec123123',
    database='treinamento'
)

# Criação do cursor
cursor = conexao.cursor()

# Leitura do arquivo personagens.txt e inserção dos dados na tabela
with open('personagens.txt', 'r') as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(';')
        nome = dados[0]
        raca = dados[1]
        idade = dados[2]
        altura = dados[3]
        peso = dados[4]
        cor_cabelo = dados[5]
        genero = dados[6]
        filme = dados[7]
        descricao_abreviada = dados[8]
        numero_personagem = dados[9]

        # Inserção dos dados na tabela personagens
        sql = "INSERT INTO personagens (nome, raca, idade, altura, peso, cor_cabelo, genero, filme, descricao_abreviada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nome, raca, idade, altura, peso, cor_cabelo, genero, filme, descricao_abreviada)
        cursor.execute(sql, valores)

# Confirmação da transação e fechamento da conexão
conexao.commit()
cursor.close()
conexao.close()