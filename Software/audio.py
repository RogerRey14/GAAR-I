#Instalar SpeechRecognition: pip install SpeechRecognition
#Instalar PyAudio: (linux) pip install pyaudio (&) sudo apt-get install python3.7-dev
                #(windows) pip install pipwin (&) pipwin install pyaudio

#Realizamos el import de speech_recognition como sr

import re
from constants import const, colors
import speech_recognition as sr
from utils import echo

#Asignamos el objeto Recognizer a RECONGNIZER
RECONGNIZER = sr.Recognizer()


# Classe para la cinematica inversa
class VoiceRecognition(object):

    def __init__(self):
        pass


    def recognize(self, audio_source):

        # por el momento leer la orden por la consola
        cmd_input = self.voiceInput(audio_source)
        cmd_input = cmd_input.lower()

        # considerar la entrada si la orden empieza con la palabra "gaari"
        if re.search("^(gary|cari)", cmd_input):
            orden = cmd_input.split()

            # comprobamos que la orden tiene almenos dos palabras
            if len(orden) > 1:
                # solo nos interesa la segunda palabra
                orden = orden[1]

            # comprobar si la orden existe
            orden_existe = False
            orden_solicitada = { "label": None, "codigo": None }

            for _orden in const.ORDENES:
                if orden == _orden["label"]:
                    orden_existe = True
                    orden_solicitada = _orden


            print(orden_solicitada)

            # Comprobar si la secuencia del orden es posible
            if orden_existe == True:
                return orden_solicitada["codigo"]
            else:
                echo(const.GAARI_SAYS + "No te he entendido, repite porfavor.", color=colors.FAIL)
                return "REPITE"

        # parar la ejecución
        elif cmd_input == 'apágate' or cmd_input == 'adiós':
            return "APAGAR"


    def voiceInput(self, source):
        echo("GAAR-I le escucha", color=colors.OKGREEN)
        RECONGNIZER.adjust_for_ambient_noise(source)
        audio = RECONGNIZER.listen(source, phrase_time_limit=2)

        try:
            command = RECONGNIZER.recognize_google(audio, language="es-ES")
            echo('Ha dicho: {}'.format(command), color=colors.WARNING)
        except:
            echo(const.GAARI_SAYS + "Disculpa, no se le escucha", color=colors.FAIL)
            echo(const.GAARI_SAYS + "Vuelva a probar", color=colors.FAIL)
            command = ""

        return command