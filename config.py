from pymongo import MongoClient

class Config:
    SECRET_KEY = 'B!weNAt1T^%kvhUI*s^' 
    MONGO_URI = 'mongodb://localhost:27017/flask'

class DevelopmentConfig(Config):
    DEBUG = True
    # Configuración de la base de datos MongoDB
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB = 'flask'
    MONGO_COLLECTION = 'user'
    
def init_mongo(app):
    # Establecer la conexión a la base de datos MongoDB
    mongo_host = app.config.get('MONGO_HOST')
    mongo_port = app.config.get('MONGO_PORT')
    mongo_db = app.config.get('MONGO_DB')
    mongo_collection = app.config.get('MONGO_COLLECTION')
    mongo_uri = f'mongodb://{mongo_host}:{mongo_port}/{mongo_db}'
    mongo_client = MongoClient(mongo_uri)
    mongo_db = mongo_client[mongo_db]
    collection = mongo_db[mongo_collection]
    return collection    
def get_mongo_collection():
    mongo_host = DevelopmentConfig.MONGO_HOST
    mongo_port = DevelopmentConfig.MONGO_PORT
    mongo_db = DevelopmentConfig.MONGO_DB
    mongo_collection = DevelopmentConfig.MONGO_COLLECTION
    mongo_uri = f'mongodb://{mongo_host}:{mongo_port}/{mongo_db}'
    client = MongoClient(mongo_uri)
    collection = client[mongo_db][mongo_collection]
    return collection

config ={
     'development':DevelopmentConfig
}