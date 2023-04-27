from typing import TypedDict, Union


class UserCreatePayload(TypedDict):
    email: str
    hashed_password: str
    first_name: Union[str, None]
    last_name: Union[str, None]


class UserUpdatePayload(TypedDict):
    id: str
    email: Union[str, None]
    hashed_password: Union[str, None]
    first_name: Union[str, None]
    last_name: Union[str, None]
