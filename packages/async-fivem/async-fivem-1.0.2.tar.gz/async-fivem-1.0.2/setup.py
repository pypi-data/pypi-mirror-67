# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fivem']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp', 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'async-fivem',
    'version': '1.0.2',
    'description': 'Async API for FiveM endpoints',
    'long_description': '# async-fivem\nAsynchronous FiveM package for retrieving Player and Server infos utilizing the [aiohttp](https://docs.aiohttp.org/en/stable/) package.\n\n## Usage\n```python\nimport asyncio\nfrom fivem import FiveM\n\nip = "127.0.0.1"\nport = 30120\n\nasync def main():\n    fivem = FiveM(ip=ip, port=port)\n    # raw list of players like you get from /players.json\n    players = await fivem.get_players_raw()\n    # raw json of server-info like you get from /info.json\n    info = await fivem.get_info_raw()\n    # raw json of server-info like you get from /dynamic.json\n    dynamic = await fivem.get_dynamic_raw()\n    # parsed list of Player objects \n    players = await fivem.get_players()\n    # parsed Server object\n    server = await fivem.get_server_info()\n\nloop = asyncio.get_event_loop()\nloop.run_until_complete(main())\n```\n\n## Api Reference\n\n### FiveM\n\n*class* FiveM(ip: *str*, port: *int*):\n- **await get_players_raw()** -> list: */players.json endpoint - raw list of players*\n- **await get_info_raw()** -> dict: */info.json endpoint - raw dict with server-info*\n- **await get_dynamic_raw()** -> dict: */dynamic.json endpoint - raw dict with server-info*\n- **await get_players()** -> [[Player](#Player)]: *returns parsed list of [Player](#Player) objects*\n- **await get_server_info()** -> [Server](#Server): *returns parsed server info [Server](#Server)*\n\n### Player\n*class* Player:\n- **name**: *player username*\n- **id**: *player id*\n- **ping**: *current player ping*\n- **xbl_id**: *xbl id, None if not available*\n- **steam_id**: *steam id, None if not available*\n- **discord_id**: *discord id, None if not available*\n- **live_id**: *live id, None if not available*\n- **license_id**: *license id, None if not available*\n\n### Server\n*class* Server:\n- **hostname**: *servers hostname*\n- **clients**: *current number of clients*\n- **max_clients**: *max clients allowed on server*\n- **game_type**: *servers game type*\n- **map_name**: *servers map name*\n\n# Requirements\n- Python >= 3.6\n- [aiohttp](https://docs.aiohttp.org/en/stable/)\n\n# Issues and Features\nIf you\'re having any issues or want additional features please create an Issue on [github](https://github.com/makupi/async-fivem/issues).\n\n[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/A0A015HXK)',
    'author': 'makubob',
    'author_email': 'makupi@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/makupi/async-fivem',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
