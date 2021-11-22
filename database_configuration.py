# Third party imports
from sqlalchemy import create_engine


class DatabaseConfiguration:
    def __init__(self, user, password, host, port, db_name):
        self.db_name = db_name
        self.host = host
        self.password = password
        self.port = port
        self.user = user

    def create_alchemy_engine(self):
        return create_engine(
            f"mariadb+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?charset=utf8mb4",
            execution_options={"isolation_level": "READ COMMITTED"}, pool_pre_ping=True)

    def get_db_name(self):
        return self.db_name

    def get_host(self):
        return self.host

    def get_password(self):
        return self.password

    def get_user(self):
        return self.user

    def get_port(self):
        return self.port
