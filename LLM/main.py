import qi
from Speaker import Speaker
from RealtimeSTT import AudioToTextRecorder

def main():
    robot_ip = "192.168.2.251"
    port = 9559

    session = qi.Session()
    session.connect(f"tcp://{robot_ip}:{port}")
    tts = session.service("ALTextToSpeech")

    speaker = Speaker(tts, session.service("ALBehaviorManager"))
    recorder = AudioToTextRecorder()
    tts.say("I live.")
    
    while True:
        recorder.start()
        input("Press Enter to stop recording...")
        recorder.stop()
        speaker.get_response(recorder.text())
        input("Press Enter to start recording...")

if __name__ == '__main__':
    main()