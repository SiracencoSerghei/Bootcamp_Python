#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
users_data = data_manager.get_customer_emails()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "BRU"
print(users_data)
customer_email_list = [user['whatIsYourEMail?'] for user in users_data]
print(customer_email_list)
# ==================== Update the Airport Codes in Google Sheet ====================

#  In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the API.
#  You should use the code you get back to update the sheet_data dictionary.

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(5)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    
    time.sleep(2)
    
    # ============= Search for indirect flight if N/A ============

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")
    
    notification_manager = NotificationManager()
    
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        # Customise the message depending on the number of stops
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only EUR {cheapest_flight.price} to fly direct " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only EUR {cheapest_flight.price} to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.stops} stop(s) " \
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
        
        print(f"Check your email. Lower price flight found to {destination['city']}!")
        
        # notification_manager.send_sms(
        #     message_body=message
        # )
        
        # SMS not working? Try whatsapp instead.
        # notification_manager.send_whatsapp(
        #     message_body=message
        # )
        # Send emails to everyone on the list
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)