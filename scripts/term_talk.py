import ollama
import qi

robot_ip = "192.168.2.251"
port = 9559
def main():
    session = qi.Session()
    
    session.connect(f"tcp://{robot_ip}:{port}")
    
    tts = session.service("ALTextToSpeech")
    conv(tts)

def conv(tts):
    tts.say("I live!")
    total_conv = "User: You are no0, a friendly and happy robot. Do not take actions, and respond with only 1 sentence.\nYou: Ok!"
    while True:
        next = input()

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"Continue this conversation {total_conv}: {next}"
                },
            ],
        )
        total_conv += f"\nUser: {next}\nYou:{response["message"]["content"]}"
        tts.say(response["message"]["content"])

if __name__ == '__main__':
    main()