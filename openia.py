import openai #pip install openai
from gtts import gTTS #pip install gTTS
from playsound import playsound #pip install playsound

openai.api_key = "" # Tu api-key aquí.

question = input("New Chat => ")
print()
print("Un momento por favor....")
completion = openai.Completion.create(engine="text-davinci-003", prompt=question, n=1, max_tokens=2048)
tts = gTTS(completion.choices[0].text, lang='es')

print(completion.choices[0].text)

tts.save("response.mp3")
playsound('response.mp3')

print()

