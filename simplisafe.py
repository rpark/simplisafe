import asyncio
import logging
import sys
from optparse import OptionParser
import argparse

from aiohttp import ClientSession

import simplipy
from simplipy.errors import SimplipyError

FILEPATH = "/home/simplisafe/simplisafe-python-dev"
FILENAME = ".apikey"

_LOGGER = logging.getLogger()

async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as session:
        refresh_token = await async_get_refresh_token()
        api = await simplipy.API.async_from_refresh_token(
            refresh_token,
            session=session,
        )
        apikey = FILEPATH + "/" + FILENAME
        f = open(apikey, "w")
        f.write(api.refresh_token)
        f.close()
        systems = await api.async_get_systems()
        logging.basicConfig(level=logging.INFO)

        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('--state', help='Desired Alarm State', required=True)
            args = vars(parser.parse_args())
            state = args['state']
            if state not in ('Off', 'Away', 'Home'):
                sys.exit("State must be Off, Away, or Home")

            systems = await api.async_get_systems()
            for system in systems.values():
                if state == "Off":
                    await system.async_set_off()
                elif state == "Away":
                    await system.async_set_away()
                elif state == "Home":
                    await system.async_set_home()
        except SimplipyError as err:
            _LOGGER.error(err)

async def async_get_refresh_token() -> str:
    apikey = FILEPATH + "/" + FILENAME
    f = open(apikey, "r")
    return f.read()

asyncio.run(main())
