# encoding: utf-8
# Instalar SpeechRecognition: pip install SpeechRecognition
#Instalar PyAudio: (linux) pip install pyaudio (&) sudo apt-get install python3.7-dev
                #(windows) pip install pipwin (&) pipwin install pyaudio

#Realizamos el import de speech_recognition como sr

import re

import speech_recognition as sr

from constants import colors, const
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
        #cmd_input = input("Escribe la orden:\n")
        cmd_input = cmd_input.lower()

        return self.processCommand(cmd_input)


    def processCommand(self, command):

        if type(command) != str:
            return None, None

        cmd_input = command

        # considerar la entrada si la orden empieza con la palabra "gaari"
        if re.search("^(gary|cari)", cmd_input):
            orden_list = cmd_input.split()

            # comprobamos que la orden tiene almenos dos palabras
            if len(orden_list) > 1:
                # solo nos interesa la segunda palabra
                orden = orden_list[1]
            else:
                return None, None


            # comprobar si la orden existe
            orden_existe = False
            orden_solicitada = { "label": None, "codigo": None }

            for _orden in const.ORDENES:
                if orden == _orden["label"]:
                    orden_existe = True
                    orden_solicitada = _orden

            # comprobar si laorden era "devuelve"

            objeto_retorno = 0
            orden_existe_2 = False
            if orden_existe == True and orden_solicitada["label"] == "devuelve" and len(orden_list) == 3:
                obj = orden_list[2]

                for _objeto in const.ORDENES[4:]:
                    if obj == _objeto["label"]:
                        objeto_retorno = _objeto["codigo"]
                        orden_existe_2 = True

            print(orden_solicitada, objeto_retorno)

            # Comprobar si la secuencia del orden es posible
            if orden_existe == True:
                if orden_solicitada["label"] != "devuelve":
                    return orden_solicitada["codigo"], objeto_retorno
                elif orden_solicitada["label"] == "devuelve" and orden_existe_2 == True:
                    return orden_solicitada["codigo"], objeto_retorno
                else:
                    echo(const.GAARI_SAYS + "No te he entendido, repite porfavor.", color=colors.FAIL)
                    return "REPITE", None
            else:
                echo(const.GAARI_SAYS + "No te he entendido, repite porfavor.", color=colors.FAIL)
                return "REPITE", None

        # parar la ejecución
        elif cmd_input == 'apágate' or cmd_input == 'adiós':
            return "APAGAR", None

        return None, None

    def voiceInput(self, source):
        echo("GAAR-I le escucha", color=colors.OKGREEN)
        RECONGNIZER.adjust_for_ambient_noise(source)
        audio = RECONGNIZER.listen(source)

        try:
            command = RECONGNIZER.recognize_google(audio, language="es-ES")
            echo('Ha dicho: {}'.format(command), color=colors.WARNING)
        except:
            echo(const.GAARI_SAYS + "Disculpa, no se le escucha", color=colors.FAIL)
            echo(const.GAARI_SAYS + "Vuelva a probar", color=colors.FAIL)
            command = ""

        return command
