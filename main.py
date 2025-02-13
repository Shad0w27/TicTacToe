# tic_tac_toe_tests.py

# Wichtig!!! tictactoe_main durch den Namen der zutestenden Python-Datei ersetzen (ohne .py)
from TTT_Vorlage import print_board
from TTT_Vorlage import check_win
from TTT_Vorlage import is_field_empty
from TTT_Vorlage import check_full

# TESTDATEN: Beispiel Spielstände, um die Funktionen zu testen
# Testfall 1: Ein vollständig leeres Brett
empty_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# Testfall 2: Ein Beispielbrett, bei dem "X" gewonnen hat (Reihe)
winner_x = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
# Testfall 3: Ein Beispielbrett, bei dem "O" gewonnen hat (Diagonale)
winner_o = ["O", "X", " ", "X", "O", " ", " ", " ", "O"]
# Testfall 4: Ein Beispielbrett, das voll ist und ein Unentschieden zeigt
draw_board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
# Testfall 5: Ein Beispielbrett, das noch nicht voll ist
in_progress_board = ["X", "O", " ", "O", "X", " ", "X", " ", "O"]


def testdata():
    print("Teste Funktion 'print_board()")
    print_board(draw_board)
    print_board(in_progress_board)

    retval = check_full(draw_board)  # Board ist voll
    if (retval is True):
        print("Test check_full(draw_board): OK")
    else:
        print("Test check_full(draw_board): Error")

    retval = check_full(in_progress_board)  # Board ist nicht voll
    if (retval is False):
        print("Test check_full(in_progress_board): OK")
    else:
        print("Test check_full(in_progress_board): Error")

    retval = check_win(winner_x, "X")  # winner_x is 'X'
    if (retval is True):
        print("Test check_win(winner_x, 'X'): OK")
    else:
        print("Test check_win(winner_x, 'X'): Error")

    retval = check_win(winner_x, "O")  # winner_x is 'X'
    if (retval is False):
        print("Test check_win(winner_x, 'O'): OK")
    else:
        print("Test check_win(winner_x, 'O'): Error")

    retval = check_win(winner_o, "O")  # winner_o is 'O'
    if (retval is True):
        print("Test check_win(winner_o, 'O'): OK")
    else:
        print("Test check_win(winner_o, 'O'): Error")

    retval = check_win(winner_o, "X")  # winner_o is 'O'
    if (retval is False):
        print("Test check_win(winner_o, 'X'): OK")
    else:
        print("Test check_win(winner_o, 'X'): Error")

    retval = check_win(draw_board, "X")  # in_progress_board no winner
    if (retval is False):
        print("Test check_win(draw_board, 'X'): OK")
    else:
        print("Test check_win(draw_board, 'X'): Error")

    retval = check_win(draw_board, "O")  # in_progress_board no winner
    if (retval is False):
        print("Test check_win(draw_board, 'O'): OK")
    else:
        print("Test check_win(draw_board, 'O'): Error")

    retval = is_field_empty(in_progress_board, 2)  # in_progress_board 2 is empty
    if (retval is True):
        print("Test is_field_empty(in_progress_board, 2): OK")
    else:
        print("Test is_field_empty(in_progress_board, 2): Error")

    retval = is_field_empty(in_progress_board, 0)  # in_progress_board 2 is empty
    if (retval is False):
        print("Test is_field_empty(in_progress_board, 0): OK")
    else:
        print("Test is_field_empty(in_progress_board, 0): Error")

    retval = check_full(in_progress_board)  # in_progress_board is not full
    if (retval is False):
        print("Test check_full(in_progress_board): OK")
    else:
        print("Test check_full(in_progress_board): Error")

    retval = check_full(draw_board)  # draw_board is full
    if (retval is True):
        print("Test check_full(draw_board): OK")
    else:
        print("Test check_full(draw_board): Error")


if __name__ == "__main__":
    testdata()
