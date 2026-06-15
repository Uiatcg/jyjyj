#!/usr/bin/env python3
"""
Minecraft Bot - Connects to Minecraft servers and performs automated tasks
"""

import asyncio
import logging
from config import USERNAME, PASSWORD, SERVER_IP, SERVER_PORT
from minecraft import authentication
from minecraft.exceptions import YggdrasilError
from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound, serverbound
from minecraft.utility import ChatUtility

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MinecraftBot:
    def __init__(self, username, password, host, port=25565):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.authenticated = False
        
    def authenticate(self):
        """Authenticate with Minecraft servers"""
        try:
            logger.info(f"Authenticating as {self.username}...")
            auth_token = authentication.authenticate(self.username, self.password)
            self.authenticated = True
            logger.info("Authentication successful!")
            return auth_token
        except YggdrasilError as e:
            logger.error(f"Authentication failed: {e}")
            return None
    
    def connect(self):
        """Connect to the Minecraft server"""
        try:
            logger.info(f"Connecting to {self.host}:{self.port}...")
            self.connection = Connection(
                self.host,
                self.port,
                username=self.username
            )
            self.connection.connect()
            logger.info(f"Successfully connected to {self.host}!")
            return True
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            return False
    
    def send_chat(self, message):
        """Send a chat message to the server"""
        try:
            if self.connection:
                packet = serverbound.play.ChatPacket()
                packet.message = message
                self.connection.write_fields(packet)
                logger.info(f"Sent chat: {message}")
                return True
        except Exception as e:
            logger.error(f"Failed to send chat: {e}")
        return False
    
    def disconnect(self):
        """Disconnect from the server"""
        try:
            if self.connection:
                self.connection.disconnect()
                logger.info("Disconnected from server")
        except Exception as e:
            logger.error(f"Error during disconnect: {e}")
    
    def run(self):
        """Main bot loop"""
        if not self.connect():
            logger.error("Failed to connect to server")
            return False
        
        try:
            # Send initial chat messages
            self.send_chat("Hello! I'm a bot joining this server!")
            
            # Keep bot running
            while self.connection.socket_connect:
                asyncio.sleep(0.1)
            
        except KeyboardInterrupt:
            logger.info("Bot interrupted by user")
        except Exception as e:
            logger.error(f"Bot error: {e}")
        finally:
            self.disconnect()
        
        return True


def main():
    """Main entry point"""
    logger.info("Starting Minecraft Bot...")
    logger.info(f"Connecting to: {SERVER_IP}:{SERVER_PORT}")
    logger.info(f"Username: {USERNAME}")
    
    bot = MinecraftBot(
        username=USERNAME,
        password=PASSWORD,
        host=SERVER_IP,
        port=SERVER_PORT
    )
    
    # Authenticate
    auth_token = bot.authenticate()
    if not auth_token:
        logger.error("Could not authenticate. Check your credentials.")
        return
    
    # Connect and run
    bot.run()


if __name__ == "__main__":
    main()
