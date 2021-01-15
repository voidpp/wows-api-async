from wows_api_async.sub_node import SubNode
from wows_api_async.tools import dict_key_transform, stringize
from .models import Achievements, AccountInfo, BaseAccountInfo
from ..cache.tools import dict_cache, DictCacheContext


class Account(SubNode):
    _node_name = 'account'

    async def achievements(self, account_ids: list[int]) -> dict[int, Achievements]:
        resp = await self._fetch('achievements', account_id = stringize(account_ids))
        return {int(aid): Achievements(**dict_key_transform(data['battle'], str.lower)) for aid, data in resp.data.items()}

    async def info(self, account_ids: list[int]) -> dict[int, AccountInfo]:
        async with dict_cache(self._cache, "encyclopedia_ships_", account_ids) as context:  # type: DictCacheContext
            if context.id_list:
                context.data.update(await self._fetch_model_dict('info', AccountInfo, account_id = stringize(context.id_list)))
        return context.data

    async def list_(self, search: str) -> list[BaseAccountInfo]:
        resp = await self._fetch('list', search = search)
        return [BaseAccountInfo(**row) for row in resp.data]
