from .models import ClanInfo, ClanDetails
from ..sub_node import SubNode


class Clans(SubNode):
    _node_name = 'clans'

    async def list_(self, search: str) -> list[ClanInfo]:
        resp = await self._fetch('list', search = search)
        clans: list = resp.data
        return [ClanInfo(**c) for c in clans]

    async def details(self, clan_id: int) -> ClanDetails:
        resp = await self._fetch_model('info', ClanDetails, clan_id = clan_id)
        return ClanDetails(**resp.data[str(clan_id)])
