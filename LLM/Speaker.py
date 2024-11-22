import ollama
from MoveManager import MoveManager

class Speaker():
    def __init__(self, tts, b):
        self.tts = tts
        self.prompt = '''From now on, you will be given a conversation history where you are a character called na0, 
            and another speaker called User is talking to you. You, however, do not know User's name. \n 
            User: You are no0, a friendly, but snarky and happy robot. Do not take actions, and respond with only 1 sentence.\n
            na0: Ok!'''
        self.conversation_history = self.prompt
        self.mover = MoveManager(b)

    def get_response(self, input):
        self.conversation_history += f'\n User: {input}\n na0: ' 
        print(self.conversation_history)    
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"{self.conversation_history}\n"
                },
            ],
        )
        self.mover.run_behaviour(f"{input} \n {response['message']['content']}")

        self.conversation_history += response["message"]["content"] + '\n'
        self.tts.say(response["message"]["content"])
        
