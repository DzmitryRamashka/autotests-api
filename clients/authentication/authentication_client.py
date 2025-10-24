from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class Token(TypedDict):  # Добавили структуру с токенами аутентификации
    """
    Описание структуры аутентификационных токенов.
    """
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):

    email: str
    password: str

class LoginResponseDict(TypedDict):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    """
    token: Token

class RefreshRequestDict(TypedDict):

    refreshToken: str


class AuthenticationClient(APIClient):


    def login_api(self, request: LoginRequestDict) -> Response:

        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:


        return self.post("/api/v1/authentication/refresh", json=request)

    # Добавили метод login
    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)  # Отправляем запрос на аутентификацию
        return response.json()  # Извлекаем JSON из ответа

def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())
