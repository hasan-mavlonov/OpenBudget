from queries import residentsqueries
from database_config.db_settings import execute_query
import hashlib


class ResidentsManager:
    def __init__(self, username):
        self.username = username

    def check_existence_by_username(self):
        try:
            params = (self.username,)
            result = execute_query(residentsqueries.READ_BY_USERNAME, params, fetch='one')
            if result is None:
                return False
            elif self.username in result:
                return True
        except Exception as e:
            print(e)
            return False

    def check_password(self, password):
        try:
            params = (self.username,)
            result = execute_query(residentsqueries.GET_PASSWORD_BY_USERNAME, params, fetch='one')
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if result is None:
                return False
            else:
                for passwords in result:
                    print(passwords)
                    if passwords == hashed_password:
                        return True
        except Exception as e:
            print(e)
            return False

    def create_resident(self, full_name, email, password):
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            params = (self.username, full_name, email, hashed_password)
            result = execute_query(residentsqueries.CREATE_RESIDENT, params, fetch='one')
            print(result)
            return True
        except Exception as e:
            print(e)
            return False
