from naoqi import ALProxy
import time, math

motion = ALProxy("ALMotion", "192.168.2.251", 9559)
tts = ALProxy("ALTextToSpeech", "192.168.2.251", 9559)
motion.setStiffnesses("Body", 1.0)
motion.moveInit()

def talk():
    tts.post.say("I am moving!")

def walk():
    motion.post.moveTo(0, 0, math.pi/2)

talk()


while True: 
    walk()
    time.sleep(0.1)