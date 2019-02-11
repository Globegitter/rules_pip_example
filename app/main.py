from aiohttp import web

import os
import sys
import time
import asyncio
import logging

from app.handler import handle_healthcheck


async def log_startup(app):
    """
    Log when server starts
    """
    logging.info("Server started at {}".format(time.time()) )

def main():
    logging.basicConfig(
        format='%(asctime)s: %(levelname)s %(message)s',
        level=logging.DEBUG if os.getenv("DEBUG") else logging.INFO
    )

    app = web.Application(
        middlewares = []
    )
    [ app.on_startup.append(i) for i in [
        log_startup,
    ]]

    app.router.add_routes(
        [
            web.get("/", handle_healthcheck),
            web.get("/health", handle_healthcheck),
        ]
    )

    web.run_app(app, port=int(os.getenv("PORT", 8000)))

if __name__ == "__main__":
    main()
