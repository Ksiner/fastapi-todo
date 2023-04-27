from .types import TokenResult
from utils.mixins import DBSessionMixin


class AuthorizeBasicFeature(DBSessionMixin):
    async def execute(self, email: str, password: str) -> TokenResult:
        pass
