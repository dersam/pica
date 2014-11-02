import sqlite3
from pica.db.drivers import driver
from pica import config

__author__ = 'Sam'
__name__ = 'sqlite'


class SqliteDriver(driver.Driver):
    def __init__(self):
        driver.Driver.__init__(self)
        self.conn = None

    def connect(self):
        path = config.get('Database', 'file')
        self.conn = sqlite3.connect(path)

    def get_job_list(self):
        c = self.conn.cursor()
        c.execute("SELECT command, minute, hour, day_month, month, day_week, label "
                  "FROM crontab WHERE enabled = 1 ORDER BY hour DESC, minute DESC")
        return c.fetchall()

    def close(self):
        self.conn.close()