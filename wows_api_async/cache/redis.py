import pickle
from typing import Any

from aioredis import Redis, create_redis_pool

from .base import CacheBase


class RedisCache(CacheBase):

    def __init__(self, url: str):
        self._url = url
        self.__client: Redis = ...

    @property
    def _client(self) -> Redis:
        if self.__client is ...:
            raise Exception("Please call the RedisCache.connect method!")
        return self.__client

    async def connect(self):
        self.__client = await create_redis_pool(self._url)

    async def get(self, key: str):
        return pickle.loads(await self._client.get(key))

    async def mget(self, keys: list[str]) -> list[Any]:
        items = await self._client.mget(*keys)
        return [pickle.loads(item) if item else None for item in items]

    async def set(self, key: str, data: Any):
        await self._client.set(key, pickle.dumps(data))

    async def mset(self, data: dict[str, Any]):
        await self._client.mset({k: pickle.dumps(v) for k, v in data.items()})
