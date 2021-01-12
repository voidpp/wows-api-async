from wows_api_async.sub_node import SubNode
from wows_api_async.tools import dict_key_transform, stringize
from .models import Achievements, AccountInfo


class Account(SubNode):
    _node_name = 'account'

    async def achievements(self, account_ids: list[int]) -> dict[int, Achievements]:
        resp = await self._fetch('achievements', account_id = stringize(account_ids))
        return {int(aid): Achievements(**dict_key_transform(data['battle'], str.lower)) for aid, data in resp.data.items()}

    async def info(self, account_ids: list[int]) -> dict[int, AccountInfo]:
        return await self._fetch_model_dict('info', AccountInfo, account_id = stringize(account_ids))
