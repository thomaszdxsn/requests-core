# This should work on python 3.6+
import requests_core

URL = "http://httpbin.org/uuid"


async def main():
    r = await requests_core.request('GET', URL)
    print(r.headers)
    print(await r.read())


if __name__ == '__main__':
    import trio

    trio.run(main)
print(requests_core.blocking_request('GET', URL, timeout=2))
