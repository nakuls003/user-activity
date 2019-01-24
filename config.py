
class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://ms:ms@localhost:5432/user_activity_db'


config = {
    'default': DevelopmentConfig
}
