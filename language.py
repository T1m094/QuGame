from settings import *

#translate Classe
class tr():
    #General
    def M0(self, content):
        language = settings.language
        self.content = content
        if (content == 0):
            text = ["ZURÜCK","BACK"]
            text = text[language]
        elif (content == 1):
            text = ["WEITER","NEXT"]
            text = text[language]
        elif (content == 2):
            text = ["HAUPMENÜ","MAIN MENUE"]
            text = text[language]
        elif (content == 3):
            text = ["SPIEL BEENDEN","STOP GAME"]
            text = text[language]
        elif (content == 4):
            text = ["PAUSE","BREAK"]
            text = text[language]
        elif (content == 5):
            text = ["ZUM PAUSIEREN LEERTASTE DRÜCKEN" ,"PRESS SPACE TO BREAK"]
            text = text[language]
        elif (content == 6):
            text = ["INFO","ABOUT"]
            text = text[language]
        elif (content == 7):
            text = ["ERGEBNIS","RESULT"]
            text = text[language]
        elif (content == 8):
            text = ["NOCHMAL","AGAIN"]
            text = text[language]

        return text

    #Mainmenue
    def M1(self, content):
        language = settings.language
        self.content = content
        if (content == 0):
            text = ["ENDE","EXIT"]
            text = text[language]
        elif (content == 1):
            text = ["START","START"]
            text = text[language]
        elif (content == 2):
            text = ["ANLEITUNG","GUIDE"]
            text = text[language]
        elif (content == 3):
            text = ["EINSTELLUNGEN","SETTINGS"]
            text = text[language]

        return text

    #Start Game Player Count
    def M2(self, content):
        language = settings.language
        self.content = content
        if (content == 0):
            text = ["ZWEI SPIELER","TWO PLAYER"]
            text = text[language]
        elif (content == 1):
            text = ["DREI SPIELER","THREE PLAYER"]
            text = text[language]
        elif (content == 2):
            text = ["VIER SPIELER","FOUR PLAYER"]
            text = text[language]
        elif (content == 3):
            text = ["ONLINE","ONLINE"]
            text = text[language]

        return text

    #Settings and Breakscreen
    def M3(self, content):
        language = settings.language
        self.content = content
        if (content == 1):
            text = ["DEUTSCH","ENGLISH"]
            text = text[language]
        elif (content == 2):
            text = ["SPRACHE","LANGUAGE"]
            text = text[language]
        elif (content == 3):
            text = [["AUS","AN"],[ "OFF","ON"]]
            text = text[language]
        elif (content == 4):
            text = ["SOUND","SOUND"]
            text = text[language]
        elif (content == 5):
            text = ["LAUTSTÄRKE","VOLUME"]
            text = text[language]

        return text

    #Instruction
    def M7(self, content):
        language = settings.language
        self.content = content
        if (content == 0):
            text = ["DIE STEUERUNG", "THE CONTROLLER"]
            text = text[language]
        elif (content == 1):
            text = ["PUNKTE", "POINTS"]
            text = text[language]
        elif (content == 2):
            text = ["SPEED - ITEM", "SPEED - ITEM"]
            text = text[language]
        elif (content == 3):
            text = ["CONFUSION - ITEM", "CONFUSION - ITEM"]
            text = text[language]
        elif (content == 4):
            text = ["DESTRUCTION - ITEM", "DESTRUCTION - ITEM"]
            text = text[language]
        # Explain points
        elif (content == 5):
            text = ["ZIEL DES SPIELES IST ES SO VIELE BLAUE QUADRATE EINZUSAMMELN", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        elif (content == 6):
            text = ["DIE PUNKTE WERDEN OBERHALB DER GESCHWINDIGKEITSANZEIGE ANGEZEIGT", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        #TODO EXPLAIN SPEED
        elif (content == 7):
            text = ["UNTERHALB DER PUNKTE WIRD DIE GESCHWINDIGKEIT ANGEZEIGT", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        elif (content == 8):
            text = ["ES KÖNNEN MAXIMAL 7 ITEMS GESAMMELT WERDEN", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        #TODO EXPLAIN CONFUSION
        elif (content == 9):
            text = ["WENN DAS GELBE ITEM GESAMMELT WIRD, DANN", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        elif (content == 10):
            text = ["WERDEN DIE GEGNER AN EINEN ANDERN ORT TELEPORTIERT", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        #TODO EXPLAIN DESTRUCTION
        elif (content == 11):
            text = ["BEI DIESEM ITEM IST VORSICHT GEBOTEN", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        elif (content == 12):
            text = ["BEIM ZUSAMMENSTOßEN, WIRD DER SPEED AUF NULL GESETZT", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]
        #TODO EXPLAIN CONTROLLER
        elif (content == 13): #Erklärung für Steuerung scheiße
            text = ["DIE STEUERUNG KANN ÜBER DIE TASTATUR STATTFINDEN ODER ÜBER EIN JOYSTICK", "MUSS NOCH ÜBERSETZT WERDEN [EN]"] #TODO übersetzen
            text = text[language]

        return text
