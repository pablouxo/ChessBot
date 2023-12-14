import random

import chess
from chess import Board


def main():
    board = Board()
    i = 0
    while not board.is_game_over():
        i += 1
        if i == 1:
            print(board)
        if i % 2 == 0:
            print("White's turn")
            bot_move(board)
        else:
            print("Black's turn")
            legal_moves = board.legal_moves
            print("Legal moves: ", legal_moves)
            move = input("Enter move: ")
            move = chess.Move.from_uci(move)
            board.push(move)
        print(board)


def scape_checkmate(board):
    legal_moves = list("k" in m for m in board.legal_moves)
    print(legal_moves)
    if legal_moves:
        auto_move = legal_moves[random.randint(0, len(legal_moves) - 1)]
        board.push(auto_move)
        print("Bot's move: ", auto_move)
    else:
        print("Checkmate")
        board.reset()


# Function to compute which move should the bot do
def bot_move(board):
    if board.is_checkmate():
        print("Checkmate")
        scape_checkmate(board)
        return
    legal_moves = list(board.legal_moves)
    auto_move = legal_moves[random.randint(0, len(legal_moves) - 1)]
    board.push(auto_move)
    print("Bot's move: ", auto_move)


# Function to evaluate the best move
def eval_move(board, movement):
    score = 0
    if board.is_checkmate():
        score = 100
    elif board.is_stalemate():
        score = 0
    elif board.is_insufficient_material():
        score = 0
    elif board.is_check():
        score = 50
    else:
        score = board.is_capture(movement)
    return score



main()
