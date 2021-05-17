import unittest

from audio import VoiceRecognition
from constants import const

voice = VoiceRecognition()

class TestAudio(unittest.TestCase):
    def test_audio_process_Command(self):
        command = "random"
        self.assertEqual(voice.processCommand(command), (None, None), "Should be (None, None)")

        command = ""
        self.assertEqual(voice.processCommand(command), (None, None), "Should be (None, None)")

        command = None
        self.assertEqual(voice.processCommand(command), (None, None), "Should be (None, None)")

        command = "Gary"
        self.assertEqual(voice.processCommand(command), (None, None), "Should be (None, None)")

        command = "cari"
        self.assertEqual(voice.processCommand(command), (None, None), "Should be (None, None)")

        command = "gary random"
        self.assertEqual(voice.processCommand(command), ('REPITE', None), "Should be ('REPITE', None)")

        orden, objeto = voice.processCommand("gary ven")
        self.assertTrue(isinstance(orden, int),  "Should be of type int")
        self.assertTrue(isinstance(objeto, int),  "Should be of type int")
        self.assertEqual(orden, const.ORDEN_VEN, f"Should be {const.ORDEN_VEN}")

        orden, _ = voice.processCommand("gary jeringuilla")
        self.assertEqual(orden, 22, "Should be 22")

        command = "gary devuelve"
        self.assertEqual(voice.processCommand(command), ('REPITE', None), "Should be (None, None)")

        command = "gary devuelve random"
        self.assertEqual(voice.processCommand(command), ('REPITE', None), "Should be ('REPITE', None)")

        command = "gary devuelve tijeras"
        self.assertEqual(voice.processCommand(command), (const.ORDEN_DEVUELVE, 21), f"Should be ({const.ORDEN_DEVUELVE}, 21)")

        command = "gary devuelve ven"
        self.assertEqual(voice.processCommand(command), ('REPITE', None), "Should be ('REPITE', None)")

        command = "gary devuelve devuelve"
        self.assertEqual(voice.processCommand(command), ('REPITE', None), "Should be ('REPITE', None)")

        command = "apágate"
        self.assertEqual(voice.processCommand(command), ('APAGAR', None), "Should be ('APAGAR', None)")



if __name__ == '__main__':
    unittest.main()