import trio

from .http_manager import AsyncPoolManager
from .http_manager._backends import TrioBackend

DEFAULT_TIMEOUT = 8

async def request(
    method,
    url,
    timeout=DEFAULT_TIMEOUT,
    body=None,
    headers=None,
    preload_content=False,
    pool=None,
    **kwargs
):
    """Returns a Response object, to be awaited."""
    if not pool:
        pool = AsyncPoolManager(backend=TrioBackend())
    with pool as http:
        r = await http.request(
            method=method,
            url=url,
            headers=headers,
            preload_content=preload_content,
            **kwargs
        )
        return r


def blocking_request(
    method,
    url,
    timeout,
    body=None,
    headers=None,
    preload_content=False,
    pool=None,
):
    """Returns a Response object."""
    return trio.run(
        request,
        method,
        url,
        timeout,
        body,
        headers,
        preload_content,
        pool
    )
