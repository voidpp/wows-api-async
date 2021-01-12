from abc import ABC, abstractmethod
from typing import Any


class CacheBase(ABC):

    @abstractmethod
    async def get(self, key: str):
        pass

    @abstractmethod
    async def mget(self, keys: list[str]) -> list[Any]:
        pass

    @abstractmethod
    async def set(self, key: str, data: Any):
        pass

    @abstractmethod
    async def mset(self, data: dict[str, Any]):
        pass
