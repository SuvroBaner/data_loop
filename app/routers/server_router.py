"""
This module enables both the servers -
"""
__version__ = '0.1'
__author__ = 'suvrobaner@gmail.com'

import os
import yaml
from typing import List

# APIRouter to break apart your api into routes
from fastapi import APIRouter, Path, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# an application specific key like from query params, header, cookie
from fastapi.security.api_key import APIKey 

from app.utils.constants import fetch_constants
from app.utils.logging import get_logger
from app.middlewares.auth_apikey import get_api_key
from app.routers.datamodels import InputRequest

_LOG_FILE = 'application.log'
logger = get_logger(name = "app_log", filename = _LOG_FILE, write_file = False)

app_config = fetch_constants()

router = APIRouter(
    tags = ["Inference"],
    responses = {404: {'description': "Not Found"}}
)

@router.post("/server1_call")
async def server1_call(inputs: InputRequest, api_key: APIKey = Depends(get_api_key)):
    server2_output = await server2_call(inputs.text)
    count = 0
    while server2_output == 'pong' and count < 10:
        count += 1
        print('Server - 2', server2_output)
        server2_output = await server2_call("ping")

@router.post("/server2_call")
async def server2_call(inputs: InputRequest, api_key: APIKey = Depends(get_api_key)):
    print('Server - 1', inputs)
    if inputs == 'ping':
        return "pong"

