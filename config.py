import os

 
class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bernard:86kerubo19@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass




class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")
    

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bernard:86kerubo19@localhost/pitches'
    

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bernard:86kerubo19@localhost/pitches'

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bernard:86kerubo19@localhost/pitches'