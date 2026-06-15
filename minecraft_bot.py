"""
Minecraft Bot Automation Script
Automates joining a Minecraft server and executing commands
"""

import time
import subprocess
import os
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController

# Initialize controllers
mouse = Controller()
keyboard = KeyboardController()

class MinecraftBot:
    def __init__(self, username="Player"):
        self.username = username
        self.login_credentials = "RtxRtxHH"
        self.target_coords = (-7, 48, -42)
        self.start_time = None
        
    def join_server(self):
        """Joins the Minecraft server with the specified username"""
        print(f"[BOT] Joining server with username: {self.username}")
        self.start_time = time.time()
        # Note: Actual join mechanism depends on your server setup
        # This would typically be handled by a launcher or direct connection
        return True
    
    def execute_command(self, command):
        """
        Executes a Minecraft command by typing it in chat
        """
        print(f"[BOT] Executing command: {command}")
        keyboard.type(command)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
    
    def login(self):
        """Logs in with the stored credentials"""
        print("[BOT] Logging in...")
        self.execute_command(f"/login {self.login_credentials}")
        time.sleep(2)
    
    def travel_to_coordinates(self):
        """
        Waits 10 seconds then travels to target coordinates and left-clicks
        """
        wait_time = 10
        print(f"[BOT] Waiting {wait_time} seconds before traveling to coordinates...")
        time.sleep(wait_time)
        
        x, y, z = self.target_coords
        print(f"[BOT] Traveling to coordinates: {x} {y} {z}")
        self.execute_command(f"/tp @s {x} {y} {z}")
        time.sleep(1)
        
        print("[BOT] Left-clicking at target location")
        mouse.click(Button.left, 1)
        time.sleep(0.5)
    
    def return_home(self):
        """
        Waits 20 seconds then returns home using /team home
        """
        wait_time = 20
        elapsed = time.time() - self.start_time
        remaining = wait_time - (elapsed - 10)  # Subtract time already spent traveling
        
        if remaining > 0:
            print(f"[BOT] Waiting {remaining:.1f} more seconds before returning home...")
            time.sleep(remaining)
        
        print("[BOT] Executing /team home command")
        self.execute_command("/team home")
        print("[BOT] Bot routine complete!")
    
    def run(self):
        """Runs the complete bot automation sequence"""
        try:
            self.join_server()
            self.login()
            self.travel_to_coordinates()
            self.return_home()
        except Exception as e:
            print(f"[BOT ERROR] An error occurred: {e}")


if __name__ == "__main__":
    # Create and run the bot
    bot = MinecraftBot(username="MinecraftBot")
    print("Starting Minecraft Bot Automation...")
    print("=" * 50)
    bot.run()
    print("=" * 50)
