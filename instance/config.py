import os

class Config(object):

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    DATABASE_URL = os.getenv(DATABASE_URL)
    DATABASE_URL_TEST = os.getenv(DATABASE_URL_TEST) 

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = True
    TESTING = True

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'staging': StagingConfig,
    'production' : ProductionConfig,
    }                                                                                                                                                                                                                                                                                                  mmmmmmmmmmmm                                                                                                                                                                     