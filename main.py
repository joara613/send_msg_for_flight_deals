from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


sheet = DataManager()
notification_manager = NotificationManager()

city_list = sheet.city_list

for city in city_list:
    city_code = sheet.get_city_code(city)
    search = FlightSearch(fly_from="YYC", fly_to=city_code)
    result = FlightData(search.searched_data)

    if sheet.get_min_price(city) > result.price:
        notification_manager.send_msg(
            price=result.price,
            city_from=result.city_from,
            fly_from=result.fly_from,
            city_to=result.city_to,
            fly_to=result.fly_to,
            departure=result.departure_date,
            arrival=result.arrival_date
        )