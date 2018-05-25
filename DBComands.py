from flask import Flask, request, render_template
from Connection import *

db_comands = Flask(__name__)
config_connection(db_comands)
cursor = get_cursor()

@db_comands.route('/')
def index():
    return render_template('login.html')


@db_comands.route('/servlogin')

def servlogin():
    name = request.args.get('name')
    password = request.args.get('password')

    cursor.execute(f'select name from users where name = \'{name}\' AND password = \'{password}\'')

    #str(dados[0])
    mysql.connect().close()
    return listar_produtos()

def listar_produtos():

    cursor.execute('select * from products')
    produtos = cursor.fetchall() #dictionary
    return render_template('/listarprodutos.html', produtos = produtos)

@db_comands.route('/detalhar')
def detalhar():
    cursor = get_cursor

    id = request.args.get('id')

    cursor.execute(f'select * from products WHERE id = {id}')
    produto = cursor.fetchone()
    print(produto)
    return render_template('/detalharproduto.html', produto = produto)


db_comands.run()