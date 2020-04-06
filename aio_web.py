# -*- coding: utf-8 -*-
# 一个简单的异步web服务器

import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)
    await site.start()
    print('Server started at http://127.0.0.1:8000...')
    return site

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
