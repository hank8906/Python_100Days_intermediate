from data_manager import DataManager as dm
from flight_search import FlightSearch as fs
import requests
from pprint import pprint

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

# initial class

dataManager = dm()
flightSearch = fs()

sheet_data = dataManager.sheet_data
# pprint(sheet_data)

# update "iataCode" value to "Testing"

# has_iata_codes = any(entry['iataCode'] for entry in sheet_data)
#
# if not has_iata_codes:
#     for entry in sheet_data:
#         entry['iataCode'] = "Testing"

# dataManager.put_iata(sheet_data)

# for entry in sheet_data:
#     flightSearch.get_iata(entry['city'])

# dataManager.put_iata_code(sheet_data, flightSearch.iata_code)

for entry in sheet_data:
    flightSearch.get_flight_info(entry['iataCode'])
