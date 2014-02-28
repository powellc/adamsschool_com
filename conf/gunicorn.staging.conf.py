import os

bind = "127.0.0.1:8882"
logfile = "/var/www/vhosts/aes_staging/logs/gunicorn.log"
max_requests = 200
workers = 2
proc_name = 'gunicorn_aes_staging'
