from flask import Flask, request, render_template
from Connection import *
from flaskext.mysql import MySQL

db_comands = Flask(__name__)

@db_comands.route('/')
def index():
    return render_template('login.html')


@db_comands.route('/servlogin', methods=['POST'])
def servlogin():
    mysql, conn, cursor = get_cursor(db_comands)
    name = request.args.get('name')
    password = request.args.get('password')

    cursor.execute(f'select name from users where name = \'{name}\' AND password = \'{password}\'')

    #str(dados[0])
    mysql.connect().close()
    return listar_produtos()


def listar_produtos():
    mysql, conn, cursor = get_cursor(db_comands)
    cursor.execute('select * from products')
    produtos = cursor.fetchall() #dictionary
    mysql.connect().close()
    return render_template('/listarprodutos.html', produtos = produtos)


@db_comands.route('/detalhar')
def detalhar():
    mysql, conn, cursor = get_cursor(db_comands)
    id = request.args.get('id')
    cursor.execute(f'select * from products WHERE id = {id}')
    produto = cursor.fetchone()
    mysql.connect().close()
    return render_template('/detalharproduto.html', produto = produto)


db_comands.run()