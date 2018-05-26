from flask import Flask, request, render_template
from Dao import *

router = Flask(__name__)

@router.route('/')
def index():
    return render_template('login.html')


@router.route('/servlogin', methods=['GET', 'POST'])
def servlogin():
    sm = check_user(router)
    return render_template('/listarprodutos.html', produtos = listar_produtos(router), sucess_message = sm)


@router.route('/detalhar', methods=['GET', 'POST'])
def serv_detalhar():
    return render_template('/detalharproduto.html', produto = detalhar_dao(router))

@router.route('/incluirproduto', methods=['GET', 'POST'])
def serv_incluir():
    incluir_dao(router)
    return servlogin()

router.run()