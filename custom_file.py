import json
import os

# New user

# File path
file_path = "data.json"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        try:
            users = json.load(file)
        except json.JSONDecodeError:
            users = {}
else:
    users = {}
def insert_user(email, name, password):
    users[email] = {
        "name": name,
        "password": password
    }
    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)

def check_user(email, password):
    if email in users and users[email]["password"] == password:
        return True
    return False
