from twilio.rest import Client
import config


TWILIO_SID = config.TWILIO_SID
TWILIO_AUTH_TOKEN = config.TWILIO_AUTH_TOKEN
TWILIO_NUM = config.TWILIO_NUM
MY_NUM = config.MY_NUM


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_msg(self, price, city_from, fly_from, city_to, fly_to, departure, arrival):
        message = self.client.messages \
            .create(
                body=f"Low price alert! Only ${price} to fly from {city_from}-{fly_from} "
                     f"to {city_to}-{fly_to}, from {departure} to {arrival}.",
                from_=TWILIO_NUM,
                to=MY_NUM
            )
        print(message)
