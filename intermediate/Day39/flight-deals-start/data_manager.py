import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.get_url = "https://api.sheety.co/803ec7a2efbc565f7d287ea7662171bc/flightDealsHank/prices"
        self.response = requests.get(url=self.get_url)
        self.sheet_data = self.response.json()["prices"]
        self.put_url = ""
        self.put_parameters = {}
        self.put_response = ""

    def put_iata(self, sheet_data):
        for data in range(2, len(sheet_data)+2):
            self.put_url = f"https://api.sheety.co/803ec7a2efbc565f7d287ea7662171bc/flightDealsHank/prices/{data}"
            self.put_parameters = {
                "price": {
                    "city": sheet_data[data-2]['city'],
                    "iataCode": sheet_data[data-2]['iataCode'],
                    "lowestPrice": sheet_data[data-2]['lowestPrice']
                }
            }
            self.put_response = requests.put(url=self.put_url, json=self.put_parameters)
            print(self.put_response.text)

    def put_iata_code(self, sheet_data, city_name):
        for data in range(2, len(sheet_data)+2):
            self.put_url = f"https://api.sheety.co/803ec7a2efbc565f7d287ea7662171bc/flightDealsHank/prices/{data}"
            self.put_parameters = {
                "price": {
                    "city": sheet_data[data-2]['city'],
                    "iataCode": city_name[data-2],
                    "lowestPrice": sheet_data[data-2]['lowestPrice']
                }
            }
            self.put_response = requests.put(url=self.put_url, json=self.put_parameters)
            print(self.put_response.text)




