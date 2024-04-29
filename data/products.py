from constants import main as const
import requests


def get_data(endpoint):
    return requests.get(f"{const.BASE_URL}/{endpoint}").json()
