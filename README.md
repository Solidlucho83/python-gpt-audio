# AI Chatbot GTP con AUDIO
[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

Este es un chatbot impulsado por inteligencia artificial que utiliza la API de OpenAI para generar respuestas y la librería de Google Text-to-Speech (gTTS) para convertir las respuestas en audio.

# Requerimientos
    Python 3.x
    pip install openai
    pip install gtts
    pip install playsound
    pip install termcolor
    pip install speech_recognition

> #### TU API-KEY de openia, puedes conseguirla aquí: **[https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)** 
 
# Uso
Para utilizar el chatbot, simplemente ejecute el script.
   
A continuación, se le pedirá que formules tu pregunta al micrófono de tu equipo. El chatbot generará una respuesta utilizando la API de OpenAI y la convertirá en audio utilizando la librería de gTTS. La respuesta se reproducirá automáticamente a través de su sistema de audio predeterminado.

# Personalización
Puede personalizar el comportamiento del chatbot modificando las siguientes variables en el archivo main.py:

    LANGUAGE: El idioma del audio generado (por defecto: "es")
    ENGINE_IA: El motor de IA utilizado para generar respuestas (por defecto: "text-davinci-003")
    AUDIO_FILE: El nombre del archivo de audio generado (por defecto: "response.mp3")

# Licencia
Este proyecto se distribuye bajo la licencia MIT. Siéntete libre de usar, modificar y distribuir el código de acuerdo con los términos de la licencia.
