from .token_result import TokenResult
from typing import Union


class AuthService:
    async def basic_register(
        email: str, password: str, first_name: Union[str, None], last_name: Union[str, None]
    ) -> TokenResult:
        pass

    async def basic_authorize(email: str, password: str) -> TokenResult:
        pass

    async def refresh_token(refresh_token: str) -> TokenResult:
        pass
