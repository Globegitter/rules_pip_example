import time
import os
from aiohttp import web

start_time = time.time()

async def handle_healthcheck(request):
    status = 200
    health = {
        "status": "ok",
    }

    response = web.json_response({
        "health": health,
        "running_since": start_time
    })

    response.set_status(status)
    return response
