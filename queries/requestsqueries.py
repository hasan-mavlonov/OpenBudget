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

GET_MONEY_REQUESTED = """
SELECT SUM(money_needed) AS total_money_requested
FROM requests;
"""
AVERAGE_MONEY_REQUESTED = """
SELECT AVG(money_needed) AS avg_money_requested
FROM requests;
"""

REQUESTS_BY_DISTRICT = """
SELECT 
    d.name AS district_name, 
    COUNT(r.id) AS total_requests
FROM 
    requests r
JOIN 
    districts d ON r.district_id = d.id
GROUP BY 
    d.name
ORDER BY 
    total_requests DESC;

"""
REQUESTS_BY_REGION = """
SELECT 
    rg.name AS region_name, 
    COUNT(r.id) AS total_requests
FROM 
    requests r
JOIN 
    districts d ON r.district_id = d.id
JOIN 
    regions rg ON d.region_id = rg.id
GROUP BY 
    rg.name
ORDER BY 
    total_requests DESC;
"""
TOP5_HIGH_MONEY_REQUESTS = """
SELECT 
    r.subject, 
    r.money_needed, 
    res.full_name AS requester_name, 
    d.name AS district_name
FROM 
    requests r
JOIN 
    residents res ON r.owner_id = res.id
JOIN 
    districts d ON r.district_id = d.id
ORDER BY 
    r.money_needed DESC
LIMIT 5;
"""
