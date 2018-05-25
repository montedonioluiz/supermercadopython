from flaskext.mysql import MySQL

mysql = MySQL()

def config_connection(main):
    main.config['MYSQL_DATABASE_USER'] = 'root'
    main.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    main.config['MYSQL_DATABASE_DB'] = 'supermercado'
    connect(main)

def connect(main):
    mysql.init_app(main)

def get_cursor():
    return mysql.get_db().cursor()