GET_ALL_DISTRICTS = """
SELECT id, name from districts where region_id = %s
"""