from queries import regionsqueries
from database_config.db_settings import execute_query


class RegionsManagers:
    def print_all_regions(self):
        try:
            params = ()
            result = execute_query(regionsqueries.GET_ALL_REGIONS, fetch='all')
            for region in result:
                print(region)
            return True
        except Exception as e:
            print(e)
            return False
