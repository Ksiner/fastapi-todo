from .token_result import TokenResult
from typing import Union


class AuthService:
    async def basic_register(
        self, email: str, password: str, first_name: Union[str, None], last_name: Union[str, None]
    ) -> TokenResult:
        pass

    async def basic_authorize(self, email: str, password: str) -> TokenResult:
        pass

    async def refresh_token(self, refresh_token: str) -> TokenResult:
        pass


AuthServiceInstance = AuthService()
