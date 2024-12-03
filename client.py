import websocket
from libs.logger import setup_Logger
from config import config
import json
import time
import threading
import ssl

class MemClient:
    ws_client: websocket.WebSocket
    is_connected: bool = False
    message_handler = None
    exit_handler = None
    connect_handler = None
    is_retry_connect: bool = True
    ws_url: str
    ping_interval: int = 5

    def __init__(self, url: str, message_handler: any,exit_handler: any,connect_handler: any, retry_connect: bool = True):
        self.ws_url = url
        self.message_handler = message_handler
        self.exit_handler = exit_handler
        self.connect_handler = connect_handler
        self.is_retry_connect = retry_connect
  
    def connect(self):
        #websocket.enableTrace(True)
        headers = {
            "user-agent": config.user_agent,
            "origin": "https://memhash-frontend.fly.dev"
        }
        self.ws_client = websocket.WebSocketApp(
            url=self.ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            header=headers,

        )
