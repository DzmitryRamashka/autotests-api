import httpx

login_payload = {
    "email": "user123@example.com",
    "password": "123@5"
}


login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
print(login_response_data)

accessToken = login_response_data["token"]["accessToken"]

me_users_headers = {"Authorization": "Bearer " + accessToken}

me_users_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=me_users_headers)
me_users_response_data = me_users_response.json()

print(me_users_response.status_code)
print(me_users_response_data)

