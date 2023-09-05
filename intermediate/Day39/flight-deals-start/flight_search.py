from data_manager import DataManager as dm
from pprint import pprint
import requests

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.location_endpoint = ""
        self.fly_endpoint = ""
        self.parameters = {}
        self.headers = {}
        self.iata_code = []
        self.fly_info = {}

    def get_iata(self, city_name):
        self.location_endpoint = "https://api.tequila.kiwi.com/locations/query"

        self.headers = {
            "apikey": "NJD65aZ8iIQLAX08qN8DVl6ePKPaBw2w"
        }

        self.parameters = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport"
        }

        get_iata_response = requests.get(url=self.location_endpoint, params=self.parameters, headers=self.headers)

        self.iata_code.append(get_iata_response.json()['locations'][0]['id'])
        # print(self.iata_code)

    def get_flight_info(self, iata_code):
        self.fly_endpoint = "https://api.tequila.kiwi.com/v2/search"

        self.headers = {
            "apikey": "NJD65aZ8iIQLAX08qN8DVl6ePKPaBw2w"
        }

        self.parameters = {
            "fly_from": "TPE",
            "fly_to": iata_code,
            "date_from": "05/09/2023",
            "date_to": "05/01/2024",
            "curr": "GBP"
        }

        get_fly_response = requests.get(url=self.fly_endpoint, params=self.parameters, headers=self.headers)

        self.fly_info[get_fly_response.json()['data'][0]["flyTo"]] = get_fly_response.json()['data'][0]["price"]
        print(self.fly_info)




