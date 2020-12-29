import requests

HOST = "http://localhost:5000"
'''# res = requests.get(f"{HOST}/flights/Baku/Tovuz")
# print(res.json())

# invalid_data = {
#     "username": "admin",
#     "password": "wrongpassword"
# }
# res = requests.post(f"{HOST}/authentication_authorization", data=invalid_data)
# print(res)

valid_data = {
    "username": "admin",
    "password": "supersecretpassword"
}
res = requests.post(f"{HOST}/authentication_authorization", data=valid_data)
token = res.json()["token"]
# res = requests.post(f"{HOST}/end_session", data={"token": token})
# print(res.text)

data = {
    "from_city": "a",
    "to_city": "b",
    "departure_date": "05.02.2021 16:00",
    "arrival_date": "05.02.2021 20:00",
    "passenger_num": "140",
    "airplane_info": "airplane",
    "token": token
}
res = requests.post(f"{HOST}/flights", data=data)
# print(res.json())

# res = requests.post(f"{HOST}/end_session", data={"token": token})
# print(res.text)


data = {
    "from_city": "a",
    "to_city": "b",
    "departure_date": "05.02.2021 16:00",
    "arrival_date": "05.02.2021 20:00",
    "token": token
}
requests.delete(f"{HOST}/flights", data=data)
res = requests.get(f"{HOST}/flights/a/b")
print(res.json())'''
valid_data = {
    "username": "admin",
    "password": "supersecretpassword"
}
res = requests.post(f"{HOST}/authentication_authorization", data=valid_data)
token = res.json()["token"]
# res = requests.delete(f"{HOST}/flights", data = {
#     "flight_id": "5",
#     "token": token
# })
# print(res.json())

# data = {
#     "from_city": "a",
#     "to_city": "b",
#     "departure_date": "05.02.2021 16:00",
#     "arrival_date": "05.02.2021 20:00",
#     "passenger_num": "140",
#     "airplane_info": "airplane",
#     "token": token
# }

# res = requests.post(f"{HOST}/flights", data=data)
# print(res.json())

data = {
    "flight_id": "2",
    "passenger_num": "250",
    "token": token
}
res = requests.put(f"{HOST}/flights", data=data)

res = requests.get(f"{HOST}/flights/Naxchivan/Gabala")
print(res.json())