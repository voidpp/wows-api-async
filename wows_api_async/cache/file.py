import pickle
from pathlib import Path
from typing import Any

from .base import CacheBase


class FileCache(CacheBase):

    def __init__(self, cache_file_path: str):
        self._cache_file_path = Path(cache_file_path)

    def _load_data(self) -> dict:
        if not self._cache_file_path.exists():
            return {}
        return pickle.loads(self._cache_file_path.read_bytes())

    def _save_data(self, data: dict):
        self._cache_file_path.write_bytes(pickle.dumps(data))

    async def mget(self, keys: list[str]) -> list[Any]:
        data = self._load_data()
        return [data.get(k) for k in keys]

    async def get(self, key: str):
        data = self._load_data()
        return data.get(key)

    async def set(self, key: str, data: Any):
        cache_data = self._load_data()
        cache_data[key] = data
        self._save_data(cache_data)

    async def mset(self, data: dict[str, Any]):
        cache_data = self._load_data()
        cache_data.update(data)
        self._save_data(cache_data)
