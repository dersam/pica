import sqlite3
import subprocess
import os
import sys
import getopt

from pica import config


def main(argv):
    #load config
    opts, args = getopt.getopt(argv, 'c:', ['configfile='])
    path = 'pica.conf'
    for opt, arg in opts:
        if opt in ('-c', '--configfile'):
            path = arg
    config.load(path)

    #get jobs
    conn = sqlite3.connect("example/sample.db")
    c = conn.cursor()
    c.execute("SELECT command, minute, hour, day_month, month, day_week, label "
              "FROM crontab WHERE enabled = 1 ORDER BY hour DESC, minute DESC")
    jobs = c.fetchall()
    conn.close()

    if len(jobs) == 0:
        print('No jobs found for specified crontab')
        exit()

    #write crontab file
    crontab = open("crontab.cr", 'w')
    for job in jobs:
        line = '#'+job[6]+"\n"
        line = line + job[1] + job[2] + job[3] + job[4] + job[5]+"\n"
        crontab.write(line)

    crontab.close()

    subprocess.call('crontab crontab.cr')

    os.remove('crontab.cr')


if __name__ == "__main__":
    main(sys.argv[1:])