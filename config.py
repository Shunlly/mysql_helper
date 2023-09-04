import os
from pathlib import Path, PurePath
import configparser


def parse_bool(s) -> bool:
    """用来从配置文件中读取配置并返回布尔值"""
    if s in ["1", "t", "T", "true", "TRUE", "True"]:
        return True
    return False


# 读取配置
configer = configparser.ConfigParser()
current_dir = os.path.dirname(__file__)
configer.read(Path.joinpath(Path(current_dir), 'config', 'config.ini'))

MYSQL_DATABASE = configer.get('database_mysql', 'database')
MYSQL_HOST = configer.get('database_mysql', 'host')
MYSQL_PORT = configer.getint('database_mysql', 'port')
MYSQL_USER = configer.get('database_mysql', 'username')
MYSQL_PWD = configer.get('database_mysql', 'password')
MYSQL_CHARSET = configer.get('database_mysql', 'charset')
