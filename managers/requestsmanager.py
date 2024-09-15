from queries import requestsqueries
from database_config.db_settings import execute_query


class RequestsManager:
    @staticmethod
    def create_request(owner_id, district_id, subject, request, money_needed):
        try:
            params = (owner_id, district_id, subject, request, money_needed,)
            execute_query(requestsqueries.CREATE_REQUEST, params)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_all_requests():
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
            print(e)
            return False

    @staticmethod
    def edit_requests(new_subject, new_request, new_money_needed, request_id):
        try:
            params = (new_subject, new_request, new_money_needed, request_id)
            execute_query(requestsqueries.EDIT_REQUEST, params)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_my_requests(owner_id):
        try:
            params = (owner_id,)
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

    @staticmethod
    def delete_request(request_id):
        try:
            params = (request_id,)
            execute_query(requestsqueries.DELETE_REQUEST, params)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_null_requests():
        try:
            result = execute_query(requestsqueries.GET_NULL_REQUESTS, fetch="all")
            for request in result:
                print(f"ID: {request[0]}\n"
                      f"Subject: {request[1]}\n"
                      f"Request: {request[2]}\n"
                      f"Money needed: {request[3]}\n\n")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def approve_request(request_id):
        try:
            params = (request_id,)
            execute_query(requestsqueries.APPROVE_REQUEST, params)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def deny_request(request_id):
        try:
            params = (request_id,)
            execute_query(requestsqueries.DENY_REQUEST, params)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def see_approved_requests():
        try:
            result = execute_query(requestsqueries.GET_APPROVED_REQUESTS, fetch="all")
            for request in result:
                print(f"ID: {request[0]}\n"
                      f"Subject: {request[1]}\n"
                      f"Request: {request[2]}\n"
                      f"Money needed: {request[3]}\n\n")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def see_denied_requests():
        try:
            result = execute_query(requestsqueries.GET_DENIED_REQUESTS, fetch="all")
            for request in result:
                print(f"ID: {request[0]}\n"
                      f"Subject: {request[1]}\n"
                      f"Request: {request[2]}\n"
                      f"Money needed: {request[3]}\n\n")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_total_money_requested():
        try:
            result = execute_query(requestsqueries.GET_MONEY_REQUESTED, fetch="one")
            for request in result:
                print(f"{request}$")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_avg_money_requested():
        try:
            result = execute_query(requestsqueries.AVERAGE_MONEY_REQUESTED, fetch="one")
            for request in result:
                print(f"{request}$")
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def requests_by_district_id():
        try:
            result = execute_query(requestsqueries.REQUESTS_BY_DISTRICT, fetch="all")
            for request in result:
                print(request)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def requests_by_region_id():
        try:
            result = execute_query(requestsqueries.REQUESTS_BY_REGION, fetch="all")
            for request in result:
                print(request)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def top5_high_money_requests():
        try:
            result = execute_query(requestsqueries.TOP5_HIGH_MONEY_REQUESTS, fetch="all")
            for request in result:
                print(request)
            return True
        except Exception as e:
            print(e)
            return False
