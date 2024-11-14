import qi

robot_ip = "192.168.2.251"
port = 9559

# Initialize a session
session = qi.Session()
try:
    session.connect(f"tcp://{robot_ip}:{port}")
    print("Connected to the robot.")
except RuntimeError:
    print("Failed to connect to the robot.")

try:
    tts = session.service("ALTextToSpeech")
    tts.say("Hello.!")
except RuntimeError:
    print("Service not available.")