import os
bind = "127.0.0.1:9888"
logfile = "/var/www/vhosts/aes_prodcution/logs/gunicorn.log"
max_requests = 1000
workers = 5
proc_name = 'gunicorn_adams_web'
