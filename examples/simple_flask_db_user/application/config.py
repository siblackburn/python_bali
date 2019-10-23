class Config(object):

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '12345'
    
    # sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # postgres
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='mysecretpassword',url='localhost',db='postgres')
    # mysql
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'

    # Flask-User configuration
    USER_APP_NAME = "Books Sample App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True