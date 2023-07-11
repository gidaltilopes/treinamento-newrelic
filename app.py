from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import requests, json, logging, os
import mysql.connector

app = Flask(__name__, template_folder='template')
Bootstrap(app)

# Dados de autenticação
USERNAME = 'foo'
PASSWORD = 'bar'

# Rota de autenticação
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME and password == PASSWORD:
            # Autenticação bem-sucedida, redirecionar para a página inicial
            status = 'c'
            return render_template('home.html', status=status)
        else:
            app.logger.error(f'Invalid login attempt: username={username}, password={password}')
            app.logger.info(f'Try resetting your password!')
            status = 'x'
            return render_template('login.html', status=status)
        
    return render_template('login.html')

# Rota da página inicial
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/consulta-externa', methods=['GET', 'POST'])
def consulta_externa():

    if request.method == 'POST':
        id = request.form['id']
        
        # Realizar chamada GET para a API
        url = f'https://swapi.dev/api/people/{id}'
        response = requests.get(url)
        data = response.json()
        result = json.dumps(data, indent=6)
        
        # Renderizar o template com o resultado da consulta
        return render_template('consulta-externa.html', data=result)
    
    return render_template('consulta-externa.html')

@app.route('/consulta-banco', methods=['GET', 'POST'])
def consulta_banco():
    
    if request.method == 'POST':
        if int(request.form['id']) >= 20 or int(request.form['id']) == 0:
            return render_template('consulta-banco.html', data="Not found")
        
        else:
            id = request.form['id']

            conn = mysql.connector.connect(
                host='curso-newrelic.cr4dgmgjfzt4.us-east-1.rds.amazonaws.com',
                database='treinamento',
                user='root',
                password='Sec123123'
            )
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM personagens where numero_personagem = {}'.format(id))
            data = cursor.fetchall()
            dados = data[0]

            # Convertendo para uma estrutura de dicionário
            personagem = {
                "id": dados[10],
                "nome": dados[1],
                "raca": dados[2],
                "idade": dados[3],
                "altura": dados[4],
                "peso": dados[5],
                "cor_cabelo": dados[6],
                "genero": dados[7],
                "filme": dados[8],
                "descricao_abreviada": dados[9]
            }

            # Convertendo para JSON
            json_data = json.dumps(personagem, indent=6)
            return render_template('consulta-banco.html', data=json_data)
    return render_template('consulta-banco.html')
# Função auxiliar para verificar autenticação
def is_authenticated():
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    
    return username == USERNAME and password == PASSWORD

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)