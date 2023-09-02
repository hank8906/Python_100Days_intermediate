import requests

user_endpoints = 'https://pixe.la/v1/users'

parameters = {
    "token": "qwertqwertqwert",
    "username": "hankhuang",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=user_endpoints, json=parameters )
print(response.text)

graph_endpoints = f"{user_endpoints}"

graph_config = {
    "id": "graph1",
    "name": "python100"
}