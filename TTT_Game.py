# Tic Tac Toe Game

# Dies ist das fertige Spiel.

# Dieser Import ist nur fuer besseres aussehen.
# Er ist nicht weiter von bedeutung and dieser Stelle.
import os


# Funktion zum Ausdrucken des Spielbretts
# Diese Funktion wird verwendet, um das aktuelle Tic Tac Toe-Spielbrett
# auf der Konsole darzustellen. Es wird jede Zeile des Brettes nacheinander
# ausgedruckt, und zwischen den Zeilen wird eine Trennlinie angezeigt.
def print_board(board):
    # 3 Wiederholungen der Schleife mit 3er Schritten, also 0 => 3 => 6 => 9
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
    # Abfrage der Reihen
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player)):
        return True
    # Abfrage der Spalten
    if ((board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player)):
        return True
    # Abfrage der Diagonalen
    if ((board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)):
        return True
    # return False fals keine Abfrage zutrifft
    return False


# Funktion zur Überprüfung, ob ein bestimmtes Feld leer ist
# Der Parameter 'index' ist eine Zahl zwischen 0 und 8, die das Spielfeld
# positioniert. Falls ja, wird True zurückgegeben, andernfalls False.
def is_field_empty(board, index):
    # Abfrage ob das Board an der Stelle von index einen leeren String enthaelt
    if board[index] == " ":
        return True
    else:
        return False


# Funktion zur Überprüfung, ob das Brett voll ist
# Diese Funktion überprüft, ob das Spielbrett vollständig ausgefüllt ist,
# d.h. ob keine leeren Felder mehr vorhanden sind. Falls das Brett voll ist,
# wird True zurückgegeben, andernfalls False.
def check_full(board):
    round = 0
    # Wiederholung solange wie board gross ist
    for i in board:
        # Abfrage ob i, also der Wert von board an der Stelle von der Wiederholungsanzahl der For-Schleife, kein leerer String ist
        if i != " ":
            round = round + 1
    if round == 9:
        return True
    return False


# Hauptfunktion zum Spielen des Spiels
# Diese Funktion dient als Einstiegspunkt für das Spiel. Sie wird dafür
# verantwortlich sein, den Spielablauf zu verwalten, einschließlich der
# Spielerwechsel, der Eingabe der Züge, der Überprüfung auf einen Gewinner und
# der Anzeige des aktuellen Spielstatus.
def play_game():
    # Hierfuer wird der os import benoetigt.
    # Hier wird der Name des Betriebsystems abgeragt.
    # Entweder 'nt' fuer Windows wo command dann auf 'cls' gesetzt wird
    # oder Linux oder MacOS wo commnad dann auf 'clear' gesetzt wird.
    if os.name == 'nt':
        command = 'cls'
    else:
        command = 'clear'

    # Das Spielbrett
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    # Spieler 1 ist X.
    player1 = "X"
    
    # Spieler 2 ist O.
    player2 = "O"
    
    # currentPlayer entspricht dem Spieler, der gerade am Zug ist.
    currentPlayer = player1

    while True:
        # Hier wird command genutzt um die Console zu loeschen.
        os.system(command)

        # Das Spielbrett wird ausgegeben.
        print_board(board)

        # Eingabe des Feldes des Spielers. Sie wird direct -1 gerechnet um sie
        # mit der Spielbrett List compatiebel zu machen.
        choice = int(input("Spieler " + currentPlayer + ": Waehlen sie ein Feld (1 - 9): ")) - 1

        # Es wird ueberprueft ob das eingegebene Feld frei ist.
        if is_field_empty(board, choice):

            # Das Feld in der Spielbrettliste bekommt den Wert "X" fuer
            # Spieler 1 oder "O" fuer Spieler 2.
            board[choice] = currentPlayer

            # Es wird ueberprueft ob der,
            # sich gerade am Zug befindende Spieler, gewonnen hat.
            if check_win(board, currentPlayer):

                # Loeschen der Console und ausgabe des finalen Spielbretts
                # und des Spielers, der gewonnen hat.
                os.system(command)
                print_board(board)
                print("Spieler " + currentPlayer + " hat gewonnen!!!")
                break

            # Es wird ueberprueft ob das Spielbretts voll ist.
            if check_full(board):

                # Loeschen der Console, ausgabe des finalen Spielbretts und
                # Nachricht das es Unentschieden ist.
                os.system(command)
                print_board(board)
                print("Unentschieden!!!")
                break

            # Wechseln der Spieler.
            # Wenn Spieler 1 dran war ist jetzt Spieler 2 und umgekehrt.
            if currentPlayer == player1:
                currentPlayer = player2
            elif currentPlayer == player2:
                currentPlayer = player1


# Hauptfunktion des Programmes.
# Der try and exept Block sind nur fuer besseres Aussehen.
try:
    if __name__ == "__main__":
        play_game()
except KeyboardInterrupt:
    # \n sagt Python nur das es eine Neue Zeile anfangen soll.
    print("\nVerlassen...")
