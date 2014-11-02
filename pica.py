import subprocess
import os
import sys
import getopt

from pica import config
from pica import log
from pica.db import database

def main(argv):
    #load config
    opts, args = getopt.getopt(argv, 'c:', ['configfile='])
    path = 'pica.conf'
    for opt, arg in opts:
        if opt in ('-c', '--configfile'):
            path = arg
    config.load(path)

    log.debug('Loaded config from '+path)

    #get jobs
    db_driver = database.Database(config.get('Database', 'driver'))
    db_driver.load_driver()
    db_driver.connect()
    jobs = db_driver.get_job_list()
    db_driver.close()

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