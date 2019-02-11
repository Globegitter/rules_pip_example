# Tests for handlers module
import pytest
import sys

from aiohttp import web

from app.handler import handle_healthcheck

async def mock_client(handler, aiohttp_client):
    app = web.Application()
    app.router.add_get('/', handler)
    client = await aiohttp_client(app)
    resp = await client.get('/')
    return resp

async def test_handle_healthcheck_successful(aiohttp_client):
    resp = await mock_client(handle_healthcheck, aiohttp_client)

    assert resp.status == 200
    json_response = await resp.json()
    assert 'health' in json_response
    assert 'status' in json_response['health']
    assert json_response['health']['status'] == "ok"
