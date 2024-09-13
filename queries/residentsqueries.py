READ_USER_BY_NAME = """
SELECT * FROM residents WHERE full_name = %s
"""
READ_BY_USERNAME = """
SELECT * FROM residents WHERE username = %s
"""

GET_PASSWORD_BY_USERNAME = """
SELECT password FROM residents WHERE username = %s
"""

CREATE_RESIDENT = """
INSERT INTO residents (username, full_name, email, password)
VALUES (%s, %s, %s, %s)
RETURNING id
"""

