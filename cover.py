from io import BytesIO
from aiohttp import FormData, ClientSession

from vkbottle import API

import pendulum
from PIL import Image, ImageDraw, ImageFont

class CoverImage:
    WIDTH, HEIGHT = 1920,768
    FILL = "#FFFFFFF"
    STROKE_FILL = "#000000"
    FONT = "BebasNeueBold.ttf"

    def __init__(self,api:API, user_id:int) -> None:
        self._api = api
        self._user_id = user_id

        self.buffer = None
    
    async def draw_cover(self) -> None:
        img = "20231121_101915.jpg"
        img = img.resiz