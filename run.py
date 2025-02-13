# run.py
# Dies ist ein kleiner Launcher der einmal das Spiel starten kann
# als auch die Tests durchfueren kann.

# Benoetigte Imports
from os import name, system
from time import sleep
from TTT_Game import play_game
from tic_tac_toe_tests import testdata


# Launch Funktion. Die Hauptfunktion dieser Datei.
# Sie started alles basierend auf der Eingabe des Nutzers.
def launch():

    # Diese Variable sagt ob der Launcher laeuft oder nicht.
    running = True

    # Abfrage welches Betriebssystem genuzt wird zum loeschen der Console
    if name == "nt":
        command = 'cls'
    else:
        command = 'clear'

    while running:

        # loeschen der Console
        system(command)

        # Ausgabe der moeglichen naechsten Schritte
        print("Was moechtest du tun?")
        print("Du kannst das Spiel starten mit 1.")
        print("Du kannst die Tests starten mit 2. (nicht fuer Spieler empfohlen)")
        print("Du kannst die App verlassen mit 3.")

        # Eingabe der Wahl
        choice = int(input(""))

        # Auswertung der Eingabe
        # Auswahl 1
        if choice == 1:

            # starten des Spiels
            play_game()

            # Nach beendigung wird 3 Sekunden gewarted
            # damit das Ergebnis kurz angeschaut werden kann.
            sleep(3)

        # Auswahl 2
        elif choice == 2:

            # loeschen der Console
            system(command)

            # starten der Testdurchlaeufe
            testdata()

            # Nach beendigung der Tests wird auf Nutzer eingabe gewarted
            input("Druecke Enter um fortzufahren")

        # Auswahl 3
        elif choice == 3:

            # Ausgabe der Auswahl
            print("Gewaehlt: App verlassen!!!")

            # Nutzereingabe ob wirklich verlassen werden soll
            qt = str(input("Wilst du wirklich verlassn? (y/n): "))

            # Abfrage der Eingabe
            if qt == "y":
                print("Verlassen...")

                # Beendigung der App durch die Variable running
                running = False


try:
    if __name__ == "__main__":
        launch()
except KeyboardInterrupt:
    print("\nApp wurde vom User gestoppt!")
