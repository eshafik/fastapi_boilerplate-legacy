import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()


# host_server = os.environ.get('host_server', 'localhost')
# db_server_port = quote_plus(str(os.environ.get('db_server_port', '5432')))
# database_name = os.environ.get('database_name', 'fastapi_db2')
# db_username = quote_plus(str(os.environ.get('db_username', 'shafik')))
# db_password = quote_plus(str(os.environ.get('db_password', 'shafik')))
# ssl_mode = quote_plus(str(os.environ.get('ssl_mode', 'prefer')))  # prefer/required

host_server = os.getenv('HOST')
db_server_port = os.getenv('PORT')
database_name = os.getenv('DB_NAME')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
ssl_mode = os.getenv('SSL_MODE')
