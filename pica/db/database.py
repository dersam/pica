__name__ = 'database'
__author__ = 'Sam'


class Database:
    def __init__(self, db_type):
        self.db_type = db_type
        self.driver = None

    def load_driver(self):
        if self.db_type == 'sqlite':
            from pica.db.drivers import sqlite
            self.driver = sqlite.SqliteDriver()
        elif self.db_type == 'mysql':
            from pica.db.drivers import mysql
            self.driver = mysql.MySqlDriver()
        else:
            return False

    def connect(self):
        self.driver.connect()

    def get_job_list(self):
        return self.driver.get_job_list()

    def close(self):
        self.driver.close()

