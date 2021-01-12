from .cache.base import CacheBase
from .fetcher import Fetcher
from .nodes.account import Account
from .nodes.clans import Clans
from .nodes.encyclopedia import Encyclopedia
from .nodes.ships import Ships


class Wows:

    def __init__(self, application_id: str, cache: CacheBase = None):
        fetcher = Fetcher(application_id)
        self.clans = Clans(fetcher, cache)
        self.encyclopedia = Encyclopedia(fetcher, cache)
        self.ships = Ships(fetcher, cache)
        self.account = Account(fetcher, cache)
