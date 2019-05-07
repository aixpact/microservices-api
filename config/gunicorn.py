# -*- coding: utf-8 -*-

bind = ':5000'  # '0.0.0.0:8000'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" in %(D)sµs'

# Replaced docker-compose.yml
      # gunicorn -b 0.0.0.0:8000
      #   --access-logfile -
      #   --reload
      #   "app_name.app:create_app()"

# gunicorn -w 1 -b :8000 app:server
