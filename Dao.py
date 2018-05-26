from flask import request
from Connection import *

def check_user(router):
    conn, cursor = get_cursor(router)
    name = request.args.get('name')
    password = request.args.get('password')

    cursor.execute(f'select name from users where name = \'{name}\' AND password = \'{password}\'')
    conn.close()
    return 'Parabéns! Você existe!'

def listar_produtos(router):
    conn, cursor = get_cursor(router)
    cursor.execute('select * from products')
    produtos = cursor.fetchall() #dictionary
    conn.close()
    return (produtos)


def detalhar_dao(router):
    conn, cursor = get_cursor(router)
    id = request.args.get('id')
    cursor.execute(f'select * from products WHERE id = {id}')
    produto = cursor.fetchone()
    conn.close()
    return produto

def incluir_dao(router):
    conn, cursor = get_cursor(router)  # name, brand, price
    name = request.args.get('name')
    brand = request.args.get('brand')
    price = request.args.get('price')
    code = request.args.get('code')

    cursor.execute(f'INSERT INTO products (description, brand, price, code) VALUES (\'{name}\', \'{brand}\', {price}, {code})')
    conn.commit()
    conn.close()

    return 'Item inserido com sucesso!'