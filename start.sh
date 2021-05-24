#!/bin/bash
# python3.6 manage.py crontab remove
# python3.6 manage.py crontab add

# systemctl restart crond.service

cd /home/pi/HelloGuest
echo "Start Django server"
python3 manage.py collectstatic --noinput
python3 manage.py runserver --insecure 0.0.0.0:80 &