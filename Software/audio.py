#Instalar SpeechRecognition: pip install SpeechRecognition
#Instalar PyAudio: (linux) pip install pyaudio (&) sudo apt-get install python3.7-dev 
                #(windows) pip install pipwin (&) pipwin install pyaudio
    
#Realizamos el import de speech_recognition como sr

import speech_recognition as sr

#Asignamos el objeto Recognizer a r

r = sr.Recognizer() 

#Utilizamos el objeto Microphone para escuchar el audio
#Utilizamos el bloque try-catch para convertir el audio en texto.

with sr.Microphone() as source:
    print('GAAR-I le escucha : ')
    audio = r.listen(source)
 
    try:
        text = r.recognize_google(audio, language="es-ES")
        print('Ha dicho: {}'.format(text))
    except:
        print('Disculpa, no se le escucha')