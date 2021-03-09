import os


class MailClientConfig:
    username = os.getenv('USER_NAME'),
    password = os.getenv('USER_PASSWORD')


class DbConfig:
    dialect = 'mysql'
    driver = 'mysqlconnector'
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    passwd = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')


class FlaskAppConfig:
    FLASK_ADMIN_SWATCH = 'cerulean'
    SQLALCHEMY_DATABASE_URI = (
        f'{DbConfig.dialect}+{DbConfig.driver}://'
        f'{DbConfig.user}:{DbConfig.passwd}@'\
        f'{DbConfig.host}/{DbConfig.db_name}'
    )