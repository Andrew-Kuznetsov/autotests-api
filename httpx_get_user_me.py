import httpx

# Список эндпоинтов
login_endpoint = "http://localhost:8000/api/v1/authentication/login"
user_endpoint = "http://localhost:8000/api/v1/users/me"

# Запрос на получение accessToken
data = {
    "email": "andreiK@example.com",
    "password": "qwerty1234"
}
login_response = httpx.post(login_endpoint, json=data)
# print(login_response.status_code)
# print(login_response.json())

#  Извлекаем accessToken
login_response_json = login_response.json()
access_token = login_response_json["token"]["accessToken"]

# Запрос на получение данных о пользователе
headers = {"Authorization": f"Bearer {access_token}"}
user_response = httpx.get(user_endpoint, headers=headers)
print(user_response.status_code)
print(user_response.json())
