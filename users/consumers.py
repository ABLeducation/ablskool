# consumers.py
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import subprocess

class TerminalConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        command = text_data.strip()
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if stdout:
            await self.send(stdout.decode('utf-8'))
        if stderr:
            await self.send(stderr.decode('utf-8'))
