from typing import List, Dict, Type, TypeVar

from pydantic import BaseModel

from .cache.base import CacheBase
from .fetcher import Fetcher, Response
from .tools import generate_model_field_list

T = TypeVar('T')


class SubNode:
    _node_name: str

    def __init__(self, fetcher: Fetcher, cache: CacheBase = None):
        self._fetcher = fetcher
        self._cache = cache

    async def _fetch(self, path: str, fields: List[str] = None, **kwargs) -> Response:
        args = kwargs or {}
        if fields:
            args['fields'] = ','.join(fields)
        return await self._fetcher.fetch(self._node_name + '/' + path, args)

    async def _fetch_model(self, path: str, model: Type[BaseModel], **kwargs) -> Response:
        return await self._fetch(path, generate_model_field_list(model), **kwargs)

    async def _fetch_model_dict(self, path: str, model: Type[T], **kwargs) -> Dict[int, T]:
        resp = await self._fetch_model(path, model, **kwargs)
        return {int(aid): model(**data) for aid, data in resp.data.items() if data}
