HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'linuxtry'
USERNAME = 'root'
PASSWORD = '1234'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SECRET_KEY = "adcfcvvff"
