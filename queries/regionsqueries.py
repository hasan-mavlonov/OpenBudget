GET_ALL_REGIONS = """
SELECT id, name from regions 
"""

ADD_REGION = """
INSERT INTO regions (name)
VALUES (%s)
"""