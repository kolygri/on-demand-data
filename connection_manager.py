# Third party imports
from decouple import config

# Internal package imports
from database_configuration import DatabaseConfiguration


def create_engine(db_name):
    # validate that db_name is string
    return (DatabaseConfiguration(
        user=config('DB_PASSWORD'),
        password=config('DB_PASSWORD'),
        host=config('TEST_HOST'),
        port=config('DB_PORT'),
        db_name=db_name
    )).create_alchemy_engine()
