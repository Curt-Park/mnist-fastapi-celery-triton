# -*- coding: utf-8 -*-
"""Send requests to the API server asynchronously."""
import argparse
import asyncio
import sys
import time

import aiohttp

sys.path.append("src")

parser = argparse.ArgumentParser(description="Client Test")
parser.add_argument(
    "--backend-url",
    type=str,
    default="http://localhost:8000",
    help="http://backend-ip:port",
)
parser.add_argument("--n-req", type=int, default=10, help="Number of requests")
args = parser.parse_args()


async def get_number(session: aiohttp.ClientSession, url: str) -> None:
    """Get a produced number from the server."""
    print("Send a request")
    async with session.get(url) as response:
        res = await response.json()
        print("Got a produced value", res["value"])


async def produce() -> None:
    """Request producing a number to the server."""
    url = f"{args.backend_url}/produce"

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(args.n_req):
            tasks.append(asyncio.ensure_future(get_number(session, url)))
        await asyncio.gather(*tasks)


begin = time.time()
asyncio.run(produce())
print("Spent", time.time() - begin, "Sec")
