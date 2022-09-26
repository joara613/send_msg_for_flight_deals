import requests
import config


SHEETY_API_ENDPOINT = config.SHEETY_API_ENDPOINT
SHEETY_AUTH = config.SHEETY_AUTH


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        header = {
            "Authorization": SHEETY_AUTH
        }
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=header)
        response.raise_for_status()
        sheet_data = response.json()["prices"]
        self.city_list = [item["city"] for item in sheet_data]
        self.city_data = {item["city"]: item for item in sheet_data}

    def get_min_price(self, city):
        return self.city_data[city]["lowestPrice"]

    def get_city_code(self, city):
        return self.city_data[city]["iataCode"]
