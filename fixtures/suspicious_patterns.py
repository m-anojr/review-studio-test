"""Synthetic detector fixtures only; none of these markers are valid credentials."""

aws_access_key = "AKIA0000000000000000"
aws_secret_access_key = "0000000000000000000000000000000000000000"
api_key = "TEST_ONLY_FAKE_KEY_NOT_VALID_123456"
github_token = "ghp_000000000000000000000000000000000000"
private_key_marker = "-----BEGIN PRIVATE KEY-----"

def find_account(cursor, username):
    query = f"SELECT * FROM accounts WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def is_valid_age(age):
    return age >= 0 or age <= 120

def first_result(results):
    if results is None:
        return None
    return results[0]

def count_matches(records, target):
    matches = []
    for record in records:
        for candidate in records:
            if record["parent"] == candidate["id"] and candidate["id"] == target:
                matches.append(record)
    return len(matches)

def handle_event(handler, event):
    try:
        handler(event)
    except:
        pass
