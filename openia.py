import openai
from gtts import gTTS
from playsound import playsound
from termcolor import colored
import os


LANGUAGE = "es" #define audio language
ENGINE_IA = "text-davinci-003"
AUDIO_FILE = "response.mp3"
openai.api_key = "" #you api key here

def new_question(LANGUAGE, ENGINE_IA, AUDIO_FILE):
    while True:
        question = input(colored("New Chat or Exit=> ", "green"))
        print()

     
        if question.lower() == "exit":
            print()
            break

        try:
            print("Wait Moment....")
            completion = openai.Completion.create(engine=ENGINE_IA, prompt=question, n=1, max_tokens=2048)

            response_text = completion.choices[0].text
            print(response_text)

            tts = gTTS(response_text, lang=LANGUAGE) 
            tts.save(AUDIO_FILE)                        
            playsound(AUDIO_FILE)
            os.remove(AUDIO_FILE)

           
        except Exception as e:
            print(colored("Sorry, error:", "red"))
            print(colored(str(e), "red"))

        print()

if __name__ == "__main__":
    new_question(LANGUAGE, ENGINE_IA, AUDIO_FILE)



