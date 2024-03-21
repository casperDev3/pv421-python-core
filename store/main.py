import requests
import json

# constants
from constants import main as const


def get_all_products():
    try:
        resp = requests.get(url=f"{const.BASE_URL}/products")
        return {
            "success": True,
            "data": resp.json().copy()
        }
    except ConnectionError as err:
        return {
            "success": False,
            "data": {
                "msg": f"Connection Error: {err}"
            }
        }
    except Exception as err:
        return {
            "success": False,
            "data": {
                "msg": f"Error: {err}"
            }
        }


def run():
    products = get_all_products()
    if products['success']:
        filter_prod = []
        products_list = products["data"]
        for product in products_list:
            if product['price'] <= 50:
                filter_prod.append(product)
            else:
                continue
        with open(f"{const.SERVER_PATH}filtered.json",
                  "w", encoding="cp1251") as file:
            json.dump(filter_prod, file)
    else:
        print("Something wrong!")
