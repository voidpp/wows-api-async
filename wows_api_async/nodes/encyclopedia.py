from wows_api_async.sub_node import SubNode
from wows_api_async.tools import stringize, chunk_list
from .models import Ship
from ..cache.tools import dict_cache, DictCacheContext


class Encyclopedia(SubNode):
    _node_name = 'encyclopedia'

    async def ships(self, ship_id_list: list[int]) -> dict[int, Ship]:
        async with dict_cache(self._cache, "encyclopedia_ships_", ship_id_list) as context:  # type: DictCacheContext
            for ship_id_part in chunk_list(context.id_list, 100):
                res = await self._fetch_model_dict('ships', Ship, ship_id = stringize(ship_id_part))
                context.data.update(res)

        return context.data
