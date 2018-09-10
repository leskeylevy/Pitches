class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levy:newpassword@localhost/pitch'
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levy:newpassword@localhost/pitch'
    DEBUG = True


config_options = {"production": ProdConfig, "development": DevConfig}
