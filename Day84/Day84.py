'''
Topics to be covered:
- Project: Build a text-based version of the Tic Tac Toe game.
'''

"""
Text-based Tic Tac Toe
- Modes: Human vs Human, Human vs Computer (Easy: random, Hard: unbeatable with minimax)
- Clean input handling, replay loop, and a simple scoreboard.
"""

import random
import sys
from typing import List, Optional, Tuple

class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    GRAY = "\033[90m"

    @staticmethod
    def safe(text: str, *codes: str) -> str:
        if not sys.stdout.isatty():
            return text
        return "".join(codes) + text + Style.RESET


def header(title: str) -> None:
    print("\n" + Style.safe("╔" + "═" * 58 + "╗", Style.CYAN, Style.BOLD))
    title_line = f"  {title}  "
    pad = max(0, 58 - len(title_line))
    print(Style.safe("║", Style.CYAN, Style.BOLD) +
          Style.safe(title_line + " " * pad, Style.BOLD) +
          Style.safe("║", Style.CYAN, Style.BOLD))
    print(Style.safe("╚" + "═" * 58 + "╝\n", Style.CYAN, Style.BOLD))


# --------- Core game logic ---------
Board = List[str]  # 9-length list with ' ', 'X', or 'O'


def new_board() -> Board:
    return [" "] * 9


def draw_board(board: Board) -> None:
    # Show position guide above for clarity
    guide = "  1 | 2 | 3 \n ---+---+---\n  4 | 5 | 6 \n ---+---+---\n  7 | 8 | 9 "
    print(Style.safe("Positions:", Style.GRAY))
    print(Style.safe(guide, Style.DIM, Style.GRAY))
    # Now draw current board with colors
    def cell(i):
        c = board[i]
        if c == "X":
            return Style.safe("X", Style.MAGENTA, Style.BOLD)
        if c == "O":
            return Style.safe("O", Style.GREEN, Style.BOLD)
        return " "
    print()
    print(f"  {cell(0)} | {cell(1)} | {cell(2)} ")
    print(" ---+---+---")
    print(f"  {cell(3)} | {cell(4)} | {cell(5)} ")
    print(" ---+---+---")
    print(f"  {cell(6)} | {cell(7)} | {cell(8)} ")
    print()


def available_moves(board: Board) -> List[int]:
    return [i for i, v in enumerate(board) if v == " "]


def check_winner(board: Board) -> Optional[str]:
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if all(v != " " for v in board):
        return "Draw"
    return None


# --------- AI (minimax) ---------
def minimax(board: Board, is_maximizing: bool, ai: str, human: str) -> Tuple[int, Optional[int]]:
    winner = check_winner(board)
    if winner == ai:
        return (1, None)
    elif winner == human:
        return (-1, None)
    elif winner == "Draw":
        return (0, None)

    best_move = None

    if is_maximizing:
        best_score = -10
        for move in available_moves(board):
            board[move] = ai
            score, _ = minimax(board, False, ai, human)
            board[move] = " "
            if score > best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)
    else:
        best_score = 10
        for move in available_moves(board):
            board[move] = human
            score, _ = minimax(board, True, ai, human)
            board[move] = " "
            if score < best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)


def ai_move(board: Board, difficulty: str, ai: str, human: str) -> int:
    moves = available_moves(board)
    if difficulty == "easy":
        return random.choice(moves)
    # Hard: unbeatable
    _, best = minimax(board, True, ai, human)
    # Fallback (shouldn't happen)
    return best if best is not None else random.choice(moves)


# --------- Input handling ---------
def ask_int(prompt: str, valid: List[int]) -> int:
    while True:
        raw = input(Style.safe(prompt, Style.BOLD))
        if raw.lower().strip() in {"q", "quit", "exit"}:
            print(Style.safe("Goodbye! 👋", Style.CYAN))
            sys.exit(0)
        if not raw.isdigit():
            print(Style.safe("Please enter a number.", Style.YELLOW))
            continue
        num = int(raw)
        if num in valid:
            return num
        print(Style.safe(f"Enter one of: {valid}", Style.YELLOW))


def ask_choice(prompt: str, choices: List[str]) -> str:
    choices_lower = [c.lower() for c in choices]
    while True:
        raw = input(Style.safe(prompt, Style.BOLD)).strip().lower()
        if raw in {"q", "quit", "exit"}:
            print(Style.safe("Goodbye! 👋", Style.CYAN))
            sys.exit(0)
        if raw in choices_lower:
            return raw
        print(Style.safe(f"Choose one of: {', '.join(choices)}", Style.YELLOW))


# --------- Main game loops ---------
def human_turn(board: Board, player_symbol: str) -> None:
    moves = available_moves(board)
    pos = ask_int(f"Player {player_symbol}, choose position (1-9): ", [m + 1 for m in moves]) - 1
    board[pos] = player_symbol


def computer_turn(board: Board, ai_symbol: str, human_symbol: str, difficulty: str) -> None:
    move = ai_move(board, difficulty, ai_symbol, human_symbol)
    board[move] = ai_symbol
    print(Style.safe(f"Computer ({ai_symbol}) chose position {move + 1}", Style.GRAY))


def game_human_vs_human() -> str:
    board = new_board()
    turn = "X"
    while True:
        header("Tic Tac Toe — Human vs Human")
        draw_board(board)
        human_turn(board, turn)
        winner = check_winner(board)
        if winner:
            header("Game Over")
            draw_board(board)
            if winner == "Draw":
                print(Style.safe("It's a draw!", Style.YELLOW, Style.BOLD))
            else:
                print(Style.safe(f"Player {winner} wins! 🎉", Style.GREEN, Style.BOLD))
            return winner
        turn = "O" if turn == "X" else "X"


def game_human_vs_computer(difficulty: str) -> str:
    board = new_board()
    # Let player pick symbol
    symbol = ask_choice("Choose your symbol (X goes first) [X/O]: ", ["X", "O"])
    human = symbol.upper()
    ai = "O" if human == "X" else "X"

    turn = "X"  # X always goes first
    while True:
        header(f"Tic Tac Toe — Human vs Computer ({difficulty.title()})")
        draw_board(board)
        if turn == human:
            human_turn(board, human)
        else:
            computer_turn(board, ai, human, difficulty)

        winner = check_winner(board)
        if winner:
            header("Game Over")
            draw_board(board)
            if winner == "Draw":
                print(Style.safe("It's a draw!", Style.YELLOW, Style.BOLD))
            elif winner == human:
                print(Style.safe("You win! 🎉", Style.GREEN, Style.BOLD))
            else:
                print(Style.safe("Computer wins! 🤖", Style.RED, Style.BOLD))
            return winner
        turn = "O" if turn == "X" else "X"


def main():
    header("Welcome to Tic Tac Toe")
    print(Style.safe("Type 'q' at any prompt to quit.\n", Style.GRAY))
    scoreboard = {"X": 0, "O": 0, "Draw": 0}

    while True:
        print("Modes:")
        print("  1) Human vs Human")
        print("  2) Human vs Computer (Easy)")
        print("  3) Human vs Computer (Hard / Unbeatable)")
        choice = ask_int("Choose a mode [1-3]: ", [1, 2, 3])

        if choice == 1:
            result = game_human_vs_human()
        elif choice == 2:
            result = game_human_vs_computer("easy")
        else:
            result = game_human_vs_computer("hard")

        scoreboard[result] += 1
        print("\nScoreboard:")
        print(f"  X wins: {scoreboard['X']}")
        print(f"  O wins: {scoreboard['O']}")
        print(f"  Draws : {scoreboard['Draw']}")

        again = ask_choice("\nPlay again? [y/n]: ", ["y", "n"])
        if again == "n":
            print(Style.safe("\nThanks for playing! 🫶", Style.CYAN, Style.BOLD))
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + Style.safe("Interrupted. Bye! 👋", Style.GRAY))