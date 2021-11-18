class DatabaseConfiguration:
    def __init__(self, user, password, host, port, db_name):
        self.db_name = db_name
        self.host = host
        self.password = password
        self.port = port
        self.user = user

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
