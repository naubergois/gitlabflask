import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:{5432}/{POSTGRES_DB}"
    )

    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ROOT = ''
    POST_DIR = 'posts'
    POST_PER_PAGE = 10
