import logging
from contextlib import asynccontextmanager, AbstractAsyncContextManager
from dataclasses import dataclass
from typing import Any

from .base import CacheBase

logger = logging.getLogger(__name__)


@dataclass
class DictCacheContext:
    id_list: list[int]
    data: dict[int, Any]


@asynccontextmanager
async def dict_cache(cache: CacheBase, id_prefix: str, id_list: list[int]) -> AbstractAsyncContextManager[DictCacheContext]:
    cached_dict = {}
    if cache:
        cached_list = await cache.mget([f"{id_prefix}{id_}" for id_ in id_list])
        cached_dict = {id_: cached_list[idx] for idx, id_ in enumerate(id_list) if cached_list[idx]}

    fetch_id_list = list(set(id_list) - cached_dict.keys())

    context = DictCacheContext(fetch_id_list, {})

    yield context

    if cache and context.data:
        await cache.mset({f"{id_prefix}{item_id}": item for item_id, item in context.data.items()})

    logger.debug("got %s item(s) from cache and %s item(s) from api", len(cached_dict), len(context.data))

    context.data.update(cached_dict)
