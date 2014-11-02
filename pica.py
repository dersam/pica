import sqlite3
import ConfigParser
import subprocess

#load config
config = ConfigParser.ConfigParser()
config.read('pica.conf')

#get jobs
conn = sqlite3.connect("example/sample.db")
c = conn.cursor()
c.execute("SELECT command, minute, hour, day_month, month, day_week, label "
          "FROM crontab WHERE enabled = 1 ORDER BY hour DESC minute DESC")
jobs = c.fetchall()
conn.close()

#write crontab file
crontab = open("crontab.cr", 'w')
for job in jobs:
    line = '#'+job[6]+"\n"
    line = line + job[1] + job[2] + job[3] + job[4] + job[5]+"\n"
    crontab.write(line)

crontab.close()

subprocess.call('crontab crontab.cr')