GET_ALL_DISTRICTS = """
SELECT id, name from districts where region_id = %s
"""
ADD_DISTRICT = """
INSERT INTO districts (region_id, name) VALUES (%s, %s)
"""