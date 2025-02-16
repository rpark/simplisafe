import asyncio
from aiohttp import ClientSession
import simplipy


FILEPATH = "/home/simplisafe/simplisafe-python-dev"
FILENAME = ".apikey"

async def main() -> None:
        """Create the aiohttp session and run the example."""
        async with ClientSession() as session:
                api = await simplipy.API.async_from_auth(
                        "7W9A4V3Hzj43yvbx7tDcnt5Bsgvk3JgYGktV0fZmiZ6qu",
                        "sWsmlf5a6Bd4k9YLDvUf9DRJxcPr9LE3sEi5g4V2mRWEzE3s9rQ",
                        session=session,
                )

        apikey = FILEPATH + "/" + FILENAME
        f = open(apikey, "w")
        f.write(api.refresh_token)
        f.close()
        print("API KEY IS " + api.refresh_token)

asyncio.run(main())
