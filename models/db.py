import mysql.connector


class DB:
    def __init__(self):
        self.conn = None
        self.connect_db()

    def connect_db(self):
        self.conn = mysql.connector.connect(
            host = "127.0.0.1",  # localhost
            user = 'root',
            password = '',  # rašot savo
            database = "barbora"  # rašot savo
        )

    def close(self):
        self.conn.close()
