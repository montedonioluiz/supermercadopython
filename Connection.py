from flaskext.mysql import MySQL



def get_cursor(main):
    main.config['MYSQL_DATABASE_USER'] = 'root'
    main.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    main.config['MYSQL_DATABASE_DB'] = 'supermercado'

    mysql = MySQL(main)
    mysql.init_app(main)

    conn = mysql.connect()
    cursor = conn.cursor()
    return mysql, conn, cursor
