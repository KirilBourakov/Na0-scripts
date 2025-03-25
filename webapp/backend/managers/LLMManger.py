import ollama

class LLMManager():
    def __init__(self, session):
        self.session = session
        self.tts = session.service("ALTextToSpeech")
        self.prompt = '''From now on, you will be given a conversation history where you are a character called na0, 
            and another speaker called User is talking to you. You, however, do not know User's name. \n 
            User: You are no0, a friendly, but snarky and happy robot. Do not take actions, and respond with only 1 sentence.\n
            na0: Ok!'''

    def respond_to(self, input):  
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"{input}\n"
                },
            ],
        )
        self.tts.say(response["message"]["content"])