from datetime import timedelta
import os

APP_NAME = 'aixpact'

DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

DASH_URL_PREFIX = '/dash/app'

# SERVER_NAME = 'localhost:8000'  # Gunicorn (port 8000)
SERVER_NAME = 'localhost'  # NGINX (port 80)
SECRET_KEY = 'insecurekeyfordev'

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'you@gmail.com'
MAIL_PASSWORD = 'awesomepassword'

# # Celery.
# CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
# CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_REDIS_MAX_CONNECTIONS = 5

# # SQLAlchemy.
# db_uri = 'postgresql://app_name:devpassword@postgres:5432/app_name'
# SQLALCHEMY_DATABASE_URI = db_uri
# SQLALCHEMY_TRACK_MODIFICATIONS = False

# # User.
# SEED_ADMIN_EMAIL = 'dev@local.host'
# SEED_ADMIN_PASSWORD = 'devpassword'
# REMEMBER_COOKIE_DURATION = timedelta(days=90)

# # Fix werkzeug's localhost issue
# SESSION_COOKIE_SECURE = False
# SESSION_COOKIE_DOMAIN = False
# SESSION_REFRESH_EACH_REQUEST = True  # refreshes cookie every session

# TODO be fixed
ADMIN = {'username': 'admin',
         'email': 'dev@local.host',
         'password': 'devpassword'}

# # Flask-Babel.
# LANGUAGES = {
#     'en': 'English',
#     'kl': 'Klingon',
#     'es': 'Spanish'
# }
# BABEL_DEFAULT_LOCALE = 'en'
