import mysql.connector

def mysqlconection():
    mysql_host = 'localhost'
    mysql_port = 3306
    mysql_username = 'root'
    mysql_password = ''
    mysql_database = 'workflowdb'

    try:
        connection = mysql.connector.connect(
            host=mysql_host,
            port=mysql_port,
            user=mysql_username,
            password=mysql_password,
            database=mysql_database
        )

        if connection.is_connected():
            print("Conexión MySQL establecida")
            return connection

    except mysql.connector.Error as mysql_error:
        print("Error de MySQL:", mysql_error)
        return None
