import configparser
import os
import random
import string

basedir = os.path.dirname(os.path.realpath(__file__))


config = configparser.ConfigParser()
config.read(f'{basedir}/config.ini')

# DB  Configurations
sgbd = config['DATABASE']['sgbd']
user = config['DATABASE']['user']
passwd = config['DATABASE']['passwd']
database = config['DATABASE']['db']
host = config['DATABASE']['host']
port = int(config['DATABASE']['port'])
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for _ in range(12))
# ----------------------------------------------------------------#


SQLALCHEMY_DATABASE_URI = f'{sgbd}://{user}:{passwd}@{host}:{port}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
DEBUG = True