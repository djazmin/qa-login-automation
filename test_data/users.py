from typing import TypedDict


class User(TypedDict):
    username: str
    password: str

STANDARD_USER: User = {
    "username": "standard_user",
    "password": "secret_sauce"
}

INVALID_USER: User = {
    "username": "standard_user",
    "password": "12332"
}

LOCKED_USER: User = {
    "username": "locked_out_user",
    "password": "secret_sauce"
}

EMPTY_USER: User = {
    "username": "",
    "password": "secret_sauce"
}

EMPTY_PASSWORD: User = {
    "username": "standard_user",
    "password": ""
}

EMPTY_CREDENTIALS: User = {
    "username": "",
    "password": ""
}

NON_EXISTENT_USER: User = {
    "username": "any_user",
    "password": "any_pass"
}
