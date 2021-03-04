import os

class DbConfig:
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    passwd = os.getenv('DB_PASSWORD')
    db = os.getenv('DB_NAME')

class FlaskAppConfig:
    FLASK_ADMIN_SWATCH = 'cerulean'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://'
                              f'{DbConfig.user}:{DbConfig.passwd}@'
                              f'{DbConfig.host}/{DbConfig.db_name}'