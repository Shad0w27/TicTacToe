# Tic Tac Toe Volage

# Diese Vorlage enthaelt die Funktionen:
# print_board, check_win, is_field_empty und check_full
# so das die alle Tests aus tic_tac_toe_tests.py bestehen.
# Um ein fertiges Tic Tac Toe Spiel zu machen muss nur noch die Funktion
# play_game geschrieben werden.

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
    pass
