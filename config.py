import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    ENV = os.environ.get('ENV', 'dev')
    DEBUG = os.environ.get('DEBUG', ENV == 'dev')
