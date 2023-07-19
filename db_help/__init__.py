from config import *
from .connect import DataClient


DATABASE = {
        "host": MYSQL_HOST,
        "port": MYSQL_PORT,
        "username": MYSQL_USER,
        "password": MYSQL_PWD,
        "database": MYSQL_DATABASE,
        "charset": MYSQL_CHARSET
    }

dataClient = DataClient(DATABASE)
