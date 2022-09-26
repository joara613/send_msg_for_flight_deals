class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.data = data
        self.fly_from = data["flyFrom"]
        self.fly_to = data["flyTo"]
        self.city_from = data["cityFrom"]
        self.city_to = data["cityTo"]
        self.price = data["price"]
        departure_data = data["local_departure"].split("T")
        self.departure_date = departure_data[0]
        self.departure_time = departure_data[1]
        arrival_data = data["route"][-1]["local_arrival"].split("T")
        self.arrival_date = arrival_data[0]
        self.arrival_time = arrival_data[1]
