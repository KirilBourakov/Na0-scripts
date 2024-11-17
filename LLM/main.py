import qi
from Speaker import Speaker

def main():
    robot_ip = "192.168.2.251"
    port = 9559

    session = qi.Session()
    session.connect(f"tcp://{robot_ip}:{port}")
    tts = session.service("ALTextToSpeech")

    speaker = Speaker(tts)
    tts.say("I live.")
    while True:
        next = input("Prompt: ")
        speaker.get_response(next)

if __name__ == '__main__':
    main()