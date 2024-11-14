import qi
import time
import math
import threading

robot_ip = "192.168.2.251"
port = 9559

# Connect to the robot's session
session = qi.Session()
session.connect(f"tcp://{robot_ip}:{port}")

# Get the TextToSpeech and Motion services
tts = session.service("ALTextToSpeech")
motion = session.service("ALMotion")

# Define the talk function
def talk():
    tts.say("I am moving!", _async=True)

# Define the walk function
def walk():
    motion.moveTo(1, 0, 0, _async=True)

# Run talk() and walk() in parallel using threads
walk()
talk()