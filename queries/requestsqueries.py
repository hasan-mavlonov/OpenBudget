CREATE_REQUEST = """
INSERT INTO requests (owner_id, district_id, subject, request, money_needed)
VALUES (%s, %s, %s, %s, %s) 
"""

GET_ALL_REQUESTS = """
SELECT id, district_id, subject, request, money_needed FROM requests
"""

EDIT_REQUEST = """
UPDATE requests SET subject = %s, request = %s, money_needed = %s 
WHERE owner_id = %s and district_id = %s
"""

GET_MY_REQUESTS = """
SELECT id, subject, request, money_needed FROM requests where owner_id = %s
"""

DELETE_REQUEST = """
DELETE FROM requests WHERE id = %s
"""