import logging
from typing import Any

from httpx import AsyncClient
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class Response(BaseModel):
    status: str
    meta: dict = None
    data: Any = None
    error: dict = None


class FetcherException(Exception):
    pass


class Fetcher:
    _url = 'https://api.worldofwarships.eu/wows/'

    def __init__(self, application_id: str):
        self._application_id = application_id

    async def fetch(self, path: str, args: dict) -> Response:
        url = self._url + path + "/"
        params = {"application_id": self._application_id}
        params.update(args)

        async with AsyncClient() as http_client:
            logger.debug("Fetch data from wows '%s', params: %s", url, params)
            resp = await http_client.get(url, params = params)
            logger.debug("Data received from wows api: %s", resp.content)

            if resp.status_code != 200:
                raise FetcherException(resp.text)

            content = resp.json()

            if content["status"] == "error":
                raise FetcherException(content["error"])

            return Response(**resp.json())
