from time import time as current_time
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

while True:
    user = int(input("Enter the choice: "))
    if user == 1:
        number = input("Enter the mobile number: ")
        phone = phonenumbers.parse(number)
        time_zones = timezone.time_zones_for_number(phone)
        v = str(carrier.name_for_number(phone, "en"))
        region = geocoder.description_for_number(phone, "en")

        print(phone)
        print(time_zones)
        print(v)
        print(region)
  
    elif user == 2:
        print("shutting...")
        break