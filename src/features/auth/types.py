from typing import TypedDict


class TokenCreationResult(TypedDict):
    token: str
    expires_at: int


class TokenResult(TypedDict):
    access_token: TokenCreationResult
    refresh_token: TokenCreationResult
