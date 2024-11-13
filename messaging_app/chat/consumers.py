import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connected")
        await self.accept()

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected: {close_code}")
        pass

    async def receive(self, text_data):
        logger.info(f"Message received: {text_data}")
        data = json.loads(text_data)
        message = data['message']

        # Echo the message back to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
