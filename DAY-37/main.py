import requests
from datetime import datetime

#----------------- USER CREATION -----------------------#
USERNAME = "bappakamba"
TOKEN = "SM4620ab6e4904a10a4e24e655f7d43d86"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

today = datetime.now().strftime("%Y%m%d")
print(today)

# user_data = {
#     "username": USERNAME,
#     "token" : TOKEN,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes"
# }

# response = requests.post(url=f"{PIXELA_ENDPOINT}", json=user_data)
# print(response.text)

#----------------- GRAPH CREATION -----------------------#
# graph_config = {
#     "id" : GRAPH_ID,
#     "name" : "Cycling Graph",
#     "unit" : "Kg",
#     "type" : "float",
#     "color" : "shibafu",
# }

header = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(
#     url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs",
#     json=graph_config,
#     headers=header
# )

# print(response.text)

#----------------- PIXEL CREATION -----------------------#
# pixel_data = {
#     "date" : "20231002",
#     "quantity" : "40"
# }

# response = requests.post(
#     url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}",
#     json=pixel_data,
#     headers=header
# )

# print(response.text)

#----------------- PIXEL UPDATE -----------------------#
# pixel_update_data = {
#     "quantity" : "25.8",
# }

response = requests.delete(
    url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20231003",
    headers=header
)

print(response.text)


