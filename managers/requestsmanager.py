import requests
from queries import requestsqueries
from database_config.db_settings import execute_query


class RequestsManager:
    def create_request(self, owner_id, district_id, subject, request, money_needed):
        try:
            params = (owner_id, district_id, subject, request, money_needed,)
            execute_query(requestsqueries.CREATE_REQUEST, params)
            return True
        except Exception as e:
            return False

    def get_all_requests(self):
        try:
            result = execute_query(requestsqueries.GET_ALL_REQUESTS, fetch="all")
            for request in result:
                print(f"Owner ID: {request[0]}\n"
                      f"District ID: {request[1]}\n"
                      f"Subject: {request[2]}\n"
                      f"Request: {request[3]}\n"
                      f"Money needed: {request[4]}\n\n")
            return True
        except Exception as e:
            return False

    def edit_requests(self, new_subject, new_request, new_money_needed, request_id):
        try:
            params = (new_subject, new_request, new_money_needed, request_id)
            execute_query(requestsqueries.EDIT_REQUEST, params)
            return True
        except Exception as e:
            return False

    def get_my_requests(self, owner_id):
        try:
            params = (owner_id, )
            result = execute_query(requestsqueries.GET_MY_REQUESTS, params, fetch="all")
            for request in result:
                print(f"ID: {request[0]}\n"
                      f"Subject: {request[1]}\n"
                      f"Request: {request[2]}\n"
                      f"Money needed: {request[3]}\n\n")
            return True
        except Exception as e:
            print(e)
            return False

    def delete_request(self, request_id):
        try:
            params = (request_id, )
            result = execute_query(requestsqueries.DELETE_REQUEST, params)
            return True
        except Exception as e:
            print(e)
            return False

