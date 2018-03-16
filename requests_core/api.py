import trio

from .http_manager import AsyncPoolManager
from .http_manager._backends import TrioBackend

async def request(method, url, pool=None, preload_content=False, **kwargs):
    """Returns a Response object, to be awaited."""
    if not pool:
        pool = AsyncPoolManager(backend=TrioBackend())

    with pool as http:
        r = await http.request(method.upper(), url, preload_content=preload_content, **kwargs)
        return r

def blocking_request(method, url, *, pool=None, preload_content=False, **kwargs):
    """Returns a Response object."""
    return trio.run(request, method, url, pool, preload_content)
