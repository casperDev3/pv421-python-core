import json


async def get_list_of_admins():
    try:
        with open("../db/admins.json", "r") as file:
            list_of_admins = json.load(file)
            return {
                "success": True,
                "data": list_of_admins
            }
    except Exception as err:
        return {
            "success": False,
            "data": None,
            "error": err
        }
