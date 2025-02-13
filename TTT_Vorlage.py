# Tic Tac Toe Game
import os


# Funktion zum Ausdrucken des Spielbretts
# Diese Funktion wird verwendet, um das aktuelle Tic Tac Toe-Spielbrett
# auf der Konsole darzustellen. Es wird jede Zeile des Brettes nacheinander
# ausgedruckt, und zwischen den Zeilen wird eine Trennlinie angezeigt.
def print_board(board):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    for i in range(0, 9, 3):
        print(board[i], "|",  board[i+1], "|", board[i+2],)
        if i < 6:
            print("-" * 9)


# Funktion zur Überprüfung, ob ein Spieler gewonnen hat
# Diese Funktion überprüft, ob der angegebene Spieler (entweder "X" oder "O")
# das Spiel gewonnen hat. Es wird geprüft, ob der Spieler eine vollständige
# Reihe, Spalte oder Diagonale ausgefüllt hat. Falls ja, wird True
# zurückgegeben, andernfalls False.
def check_win(board, player):
    pass


# Funktion zur Überprüfung, ob ein bestimmtes Feld leer ist
# Der Parameter 'index' ist eine Zahl zwischen 0 und 8, die das Spielfeld
# positioniert. Falls ja, wird True zurückgegeben, andernfalls False.
def is_field_empty(board, index):
    pass


# Funktion zur Überprüfung, ob das Brett voll ist
# Diese Funktion überprüft, ob das Spielbrett vollständig ausgefüllt ist,
# d.h. ob keine leeren Felder mehr vorhanden sind. Falls das Brett voll ist,
# wird True zurückgegeben, andernfalls False.
def check_full(board):
    pass


# Hauptfunktion zum Spielen des Spiels
# Diese Funktion dient als Einstiegspunkt für das Spiel. Sie wird dafür
# verantwortlich sein, den Spielablauf zu verwalten, einschließlich der
# Spielerwechsel, der Eingabe der Züge, der Überprüfung auf einen Gewinner und
# der Anzeige des aktuellen Spielstatus.
def play_game():
    pass
