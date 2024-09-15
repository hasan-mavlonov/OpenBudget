from queries import districtsqueries
from database_config.db_settings import execute_query


class DistrictsManager:
    @staticmethod
    def get_all_districts(region_id):
        try:
            params = (region_id,)
            result = execute_query(districtsqueries.GET_ALL_DISTRICTS, params, fetch='all')
            for data in result:
                print(data)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def add_district(region_id, district_name):
        try:
            params = (region_id, district_name,)
            execute_query(districtsqueries.ADD_DISTRICT, params)
            return True
        except Exception as e:
            print(e)
            return False
