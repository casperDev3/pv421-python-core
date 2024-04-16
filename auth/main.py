import json


def is_admin(cid):
    with open("db/admins.json", "r") as file:
        admin_ids = json.load(file)
        if cid in admin_ids:
            return True
        return False
