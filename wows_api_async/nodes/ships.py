from wows_api_async.sub_node import SubNode
from .models import PlayerStatistics


class Ships(SubNode):
    _node_name = 'ships'

    async def stats(self, account_id: int) -> list[PlayerStatistics]:
        resp = await self._fetch('stats', account_id = str(account_id))
        ships = resp.data[str(account_id)]
        return [PlayerStatistics(**s) for s in ships]
