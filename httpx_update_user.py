import httpx
from fakers import get_random_email

# Список эндпоинтов
new_user_endpoint = 'http://localhost:8000/api/v1/users'
login_endpoint = 'http://localhost:8000/api/v1/authentication/login'

# Создание нового пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post(new_user_endpoint, json=create_user_payload)
create_user_response_json = create_user_response.json()
print(create_user_response.status_code)
print(create_user_response_json, '\n')

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post(login_endpoint, json=login_payload)
login_response_json = login_response.json()
print(login_response.status_code)
print(login_response_json, '\n')

# Обновление пользователя
update_user_endpoint = f'http://localhost:8000/api/v1/users/{create_user_response_json['user']['id']}'
headers = {"Authorization": f"Bearer {login_response_json['token']['accessToken']}"}
update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
update_user_response = httpx.patch(update_user_endpoint, headers=headers, json=update_user_payload)
update_user_response_json = update_user_response.json()
print(update_user_response.status_code)
print(update_user_response_json)
