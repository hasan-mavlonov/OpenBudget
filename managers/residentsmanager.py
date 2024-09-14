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
            for row in result:
                if self.username == row:
                    return True
            else:
                return False
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
                    if passwords == hashed_password:
                        return True
        except Exception as e:
            print(e)
            return False

    def create_resident(self, full_name, district_id, email, password):
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            params = (self.username, full_name, district_id, email, hashed_password)
            result = execute_query(residentsqueries.CREATE_RESIDENT, params, fetch='one')
            return True
        except Exception as e:
            print(e)
            return False

    def get_resident_id(self):
        try:
            params = (self.username,)
            result = execute_query(residentsqueries.GET_RESIDENT_ID, params, fetch='one')
            for i in result:
                return i
            return False
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_resident_username(resident_id):
        try:
            params = (resident_id,)
            result = execute_query(residentsqueries.GET_RESIDENT_USERNAME, params, fetch='one')
            for i in result:
                return i
            return False
        except Exception as e:
            print(e)
            return False

    def get_resident_data(self):
        try:
            params = (self.username,)
            result = execute_query(residentsqueries.READ_BY_USERNAME, params, fetch='one')
            print(f'Full name: {result[0]}')
            print(f'Username: {result[1]}')
            print(f'Email: {result[2]}')
            return True
        except Exception as e:
            print(e)
            return False

    def update_resident(self, new_full_name, new_username, new_email):
        try:
            params = (new_full_name, new_username, new_email, self.username, )
            result = execute_query(residentsqueries.EDIT_RESIDENT, params)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_resident(self):
        try:
            params = (self.username, )
            result = execute_query(residentsqueries.DELETE_RESIDENT, params)
            return True
        except Exception as e:
            print(e)
            return False

    def get_district_id(self):
        try:
            params = (self.username,)
            result = execute_query(residentsqueries.GET_DISTRICT_ID, params, fetch='one')
            for i in result:
                return i
            return False
        except Exception as e:
            print(e)
            return False
