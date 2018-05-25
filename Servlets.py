from flask import Flask, request, render_template
from flaskext.mysql import MySQL

#instanciar a aplicação usando o Flask

Servlets = Flask(__name__)

Servlets.config['MYSQL_DATABASE_USER'] = 'root'
Servlets.config['MYSQL_DATABASE_PASSWORD'] = 'root'
Servlets.config['MYSQL_DATABASE_DB'] = 'supermercado'

mysql = MySQL()
mysql.init_app(Servlets)

@Servlets.route('/')
def index():
    return render_template('login.html')


@Servlets.route('/servlogin')

def servlogin():
    name = request.args.get('name')
    password = request.args.get('password')

    cursor = mysql.get_db().cursor()

    cursor.execute(f'select name from users where name = \'{name}\' AND password = \'{password}\'')

    #str(dados[0])
    mysql.connect().close()
    return listar_produtos()

def listar_produtos():
    cursor = mysql.get_db().cursor()

    cursor.execute('select * from products')
    produtos = cursor.fetchall() #dictionary
    return render_template('/listarprodutos.html', produtos = produtos)

@Servlets.route('/detalhar')
def detalhar():
    cursor = mysql.get_db().cursor()

    id = request.args.get('id')

    cursor.execute(f'select * from products WHERE id = {id}')
    produto = cursor.fetchone()
    print(produto)
    return render_template('/detalharproduto.html', produto = produto)


Servlets.run()