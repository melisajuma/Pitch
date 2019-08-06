import os

class Config:
    
    SQLACHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_MODIFICATIONS = 'postgresql+psycopg2://moringa:mel123\q@localhost/pitch'
    
    SECRET_KEY = 'Im not boarding'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        
        
class DevConfig(Config):
    
     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:mel123@127.0.0.1/pitch'
     DEBUG = True
        
#class TestConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mel123@localhost/pitch'
        
        
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    #'test':TestConfig
}
