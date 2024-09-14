READ_RESIDENT_BY_RESIDENT_ID = """
SELECT * FROM residents WHERE id = %s
"""
READ_BY_USERNAME = """
SELECT full_name, username, email FROM residents WHERE username = %s
"""

GET_PASSWORD_BY_USERNAME = """
SELECT password FROM residents WHERE username = %s
"""

CREATE_RESIDENT = """
INSERT INTO residents (username, full_name, district_id, email, password)
VALUES (%s, %s, %s, %s, %s)
RETURNING id
"""
GET_RESIDENT_ID = """
SELECT id FROM residents WHERE username = %s
"""
GET_RESIDENT_USERNAME = """
SELECT username FROM residents WHERE id = %s
"""

EDIT_RESIDENT = """
UPDATE residents SET full_name = %s, username = %s, email = %s
WHERE username = %s
"""

DELETE_RESIDENT = """
DELETE FROM residents WHERE username = %s
"""

GET_DISTRICT_ID = """
SELECT district_id FROM residents WHERE username = %s
"""
SEE_ALL_RESIDENTS = """
SELECT id, full_name, email FROM residents 
"""
SEE_RESIDENTS_BY_DISTRICT = """
SELECT id, full_name, email FROM residents WHERE district_id = %s
"""