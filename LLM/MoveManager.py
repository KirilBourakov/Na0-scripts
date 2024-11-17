import ollama

class MoveManager():
    def __init__(self, behaviour):
        self.behaviour = behaviour
        self.prompt = '''You will be given a set of sentences. 
        Choose one of the following words that best describe the sentences. 
        Respond with only the word you choose. For example, your response should only be 'Shocked' when the sentences seem to align with that.
        The list is: \n
        Fear, Late, Fearful, Sorry, Angry, Bored, Sad, Shocked, Disappointed, Surprise, Fear, Angry, Humiliated, Hurt, Bored, Exhausted, Frustrated, Angry
        Peaceful, Interested, Enthusiastic, Proud, Hungry, Happy, Relived, Laugh, Excited, Mocker, Ecstatic, Amused, Confident, Optimistic, Shy, Winner, Proud, Sure, 
        Innocent, Hesitation, Confused, Lonely, Suspicious, Mischievous, Alienated \n
        The sentence is: '''

        self.negative = ['Fear', 'Late', 'Fearful', 'Sorry', 'Angry', 'Bored', 'Sad', 'Shocked', 'Disappointed', 'Surprise', 'Fear', 'Angry', 'Humiliated', 'Hurt', 'Bored', 'Exhausted', 'Frustrated', 'Angry']
        self.positive = ['Peaceful', 'Interested', 'Enthusiastic', 'Proud', 'Hungry', 'Happy', 'Relived', 'Laugh', 'Excited', 'Mocker', 'Ecstatic', 'Amused', 'Confident', 'Optimistic', 'Shy', 'Winner', 'Proud', 'Sure']
        self.neutral = ['Innocent', 'Hesitation', 'Confused', 'Lonely', 'Suspicious', 'Mischievous', 'Alienated']
    
    def run_behaviour(self, response):
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"{self.prompt}{response}"
                },
            ],
        )
        folder = ''
        response = response["message"]["content"]
        print(response)
        if response in self.negative:
            folder = 'Negative'
        elif response in self.positive:
            folder = 'Positive'
        elif response in self.neutral:
            folder = 'Neutral'
        else:
            folder = 'Neutral'
            response = 'Puzzled'
        
        print(f'System/animations/Stand/Emotions/{folder}/{response}_1')
        self.behaviour.runBehavior(f'System/animations/Stand/Emotions/{folder}/{response}_1', _async = True)



