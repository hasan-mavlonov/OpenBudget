READ_BY_FULL_NAME = """
SELECT * FROM residents WHERE full_name = %s
"""

READ_BY_USERNAME = """
SELECT * FROM residents WHERE username = %s
"""

GET_PASSWORD_BY_USERNAME = """
SELECT * FROM residents WHERE password = %s
"""

CREATE_RESIDENT = """
INSERT INTO residents (full_name, username, password)
VALUES (%s, %s, %s)
RETURNING id
"""

