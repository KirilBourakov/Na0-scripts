import ollama

class LLMManager():
    def __init__(self, session):
        self.session = session
        self.tts = session.service("ALTextToSpeech")
        self.sysprompt = '''From now on, you will be given a conversation history where you are a character called Nao, a happy but snarky robot 
            and another speaker called User is talking to you. Do not take actions, and respond briefly sentence. \n User: '''

    def respond_to(self, input):  
        print('responding...')
        response = response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": self.sysprompt + input
                },
            ],
        )
        self.tts.say(response.message.content)