import ollama
from google import genai

class LLMManager():
    def __init__(self, session):
        self.session = session
        self.tts = session.service("ALTextToSpeech")
        self.sysprompt = '''From now on, you will be given a conversation history where you are a character called Nao, 
            and another speaker called User is talking to you. Do not take actions, and respond briefly sentence. \n User: '''
        
        self.client = genai.Client(api_key="[INSERT HERE]")

    def respond_to(self, input):  
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=self.sysprompt + input
        )
        self.tts.say(response.text)