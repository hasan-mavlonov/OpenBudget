CREATE_REQUEST = """
INSERT INTO requests (owner_id, district_id, subject, request, money_needed)
VALUES (%s, %s, %s, %s, %s) 
"""

GET_ALL_REQUESTS = """
SELECT id, district_id, subject, request, money_needed FROM requests
"""

EDIT_REQUEST = """
UPDATE requests SET subject = %s, request = %s, money_needed = %s 
WHERE id = %s
"""

GET_MY_REQUESTS = """
SELECT id, subject, request, money_needed FROM requests where owner_id = %s
"""

DELETE_REQUEST = """
DELETE FROM requests WHERE id = %s
"""

GET_NULL_REQUESTS = """
SELECT id, subject, request, money_needed FROM requests where is_approved IS NULL
"""


APPROVE_REQUEST = """
UPDATE requests SET is_approved = TRUE WHERE id = %s
"""

DENY_REQUEST = """
UPDATE requests SET is_approved = FALSE WHERE id = %s
"""

GET_APPROVED_REQUESTS = """
SELECT id, subject, request, money_needed FROM requests where is_approved IS TRUE
"""

GET_DENIED_REQUESTS = """
SELECT id, subject, request, money_needed FROM requests where is_approved IS FALSE
"""