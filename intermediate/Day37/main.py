import requests

# --------------------------------Create a user-------------------------------- #
user_endpoints = 'https://pixe.la/v1/users'
USERNAME = "hankhuang"
TOKEN = "qwertqwertqwert"
GRAPH_ID = "graph1"

# parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=user_endpoints, json=parameters )
# print(response.text)

# ----------------------------------Create a graph------------------------------ #
# graph_endpoints = f"{user_endpoints}/{USERNAME}/graphs"
#
# headers = {
#     "X-USER-TOKEN":TOKEN
# }
#
# graph_config = {
#     "id": "graph1",
#     "name": "python100",
#     "unit": "hour",
#     "type": "float",
#     "color": "ajisai"
# }
#
# response = requests.post(url=graph_endpoints, headers=headers, json=graph_config)
# print(response.text)

# --------------------------------POST value to graph---------------------------- #

graph_endpoints = f"{user_endpoints}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_config = {
    "date": "20230904",
    "quantity": "2.5",
}

response = requests.post(url=graph_endpoints, headers=headers, json=graph_config)
print(response.text)

# --------------------------------PUT value to graph---------------------------- #

# --------------------------------DELETE value to graph---------------------------- #

