from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/first')
async def first_method(request):
    return web.Response(text="First method is good")


@routes.get('/second')
async def second_method(request):
    return web.Response(text="Second method is good")


app = web.Application()
app.add_routes(routes)
web.run_app(app)
