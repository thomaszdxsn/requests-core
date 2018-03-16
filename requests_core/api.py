import trio

from .http_manager import AsyncPoolManager
from .http_manager._backends import TrioBackend


async def request(
    method,
    url,
    body=None,
    headers=None,
    # encode_multipart=True,
    # multipart_boundary=None,
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
            # encode_multipart=encode_multipart,
            # multipart_boundary=multipart_boundary,
            preload_content=preload_content,
            **kwargs
        )
        return r


def blocking_request(
    method,
    url,
    body=None,
    headers=None,
    # encode_multipart=True,
    # multipart_boundary=None,
    preload_content=False,
    pool=None,
    # **kwargs
):
    """Returns a Response object."""
    return trio.run(
        request,
        method,
        url,
        body,
        headers,
        # encode_multipart,
        # multipart_boundary,
        preload_content,
        pool
    )
