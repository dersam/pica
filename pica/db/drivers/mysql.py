import MySQLdb
from pica.db.drivers import driver
from pica import config

__author__ = 'Sam'
__name__ = 'mysql'


class MySqlDriver(driver.Driver):
    def __init__(self):
        driver.Driver.__init__(self)
        self.conn = None

    def connect(self):
        self.conn = MySQLdb.connect(config.get('Database', 'host'),
                                    config.get('Database', 'user'),
                                    config.get('Database', 'password'),
                                    config.get('Database', 'database'))

    def get_job_list(self):
        c = self.conn.cursor()
        c.execute("SELECT command, minute, hour, day_month, month, day_week, label "
                  "FROM crontab WHERE enabled = 1 ORDER BY hour DESC, minute DESC")
        return c.fetchall()

    def close(self):
        self.conn.close()