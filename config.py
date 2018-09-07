import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql+psycopg2://levy:newpassword@localhost/pitch')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {"production": ProdConfig, "default": DevConfig}
