import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
import config


TEQUILA_SEARCH_API_ENDPOINT = config.TEQUILA_SEARCH_API_ENDPOINT
TEQUILA_API_KEY = config.TEQUILA_API_KEY

tomorrow = (dt.datetime.today() + relativedelta(days=+6)).strftime("%d/%m/%Y")
six_months_later = (dt.datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_from, fly_to):
        header = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "flight_type": "round",
            "date_from": tomorrow,
            "date_to": six_months_later,
            "return_from": tomorrow,
            "return_to": six_months_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "CAD",
            "max_sector_stopovers": 1,
            "limit": 1
        }

        res = requests.get(url=TEQUILA_SEARCH_API_ENDPOINT, params=params, headers=header)
        res.raise_for_status()
        self.searched_data = res.json()["data"][0]