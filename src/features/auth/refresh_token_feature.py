from .types import TokenResult
from utils.mixins import DBSessionMixin


class RefreshTokenFeature(DBSessionMixin):
    async def execute(self, refresh_token: str) -> TokenResult:
        pass
