import sys, numpy as np
import re
from aoclib import *

def check_board(board):
    for k in range(len(board)):
        nx, ny = 0, 0
        for l in range(len(board)):
            if board[k][l] == 'x':
                nx += 1
            if board[l][k] == 'x':
                ny += 1
        if ny == 5 or nx == 5:
            return True
    return False

if "--test" in sys.argv or "-t" in sys.argv:
    test = True
else:
    test = False

input_file = (sys.argv[0].split(".")[0][1:])
input_file += "test.txt" if test==True else ".txt"

with open(input_file, "r") as f:
    input_ = f.read().strip()

segments = input_.split("\n\n")

drawn = [int(x) for x in segments[0].split(",")]
boards = segments[1:]
for i, b in enumerate(boards):
    boards[i] = [[int(x) for x in  re.findall(r'(\d+)', line)] for line in b.splitlines()]

# Part 1
def part1():
    for d in drawn:
        for i, b in enumerate(boards.copy()):
            for j in range(5):
                for k in range(5):
                    if b[j][k] == d: b[j][k] = 'x'
            if check_board(b):
                score = sum([int(s) if s != 'x' else 0 for row in b for s in row])
                print(score * d)
                return

# Part 2
N = len(boards)
won = 0
for d in drawn:
    for i, b in enumerate(boards.copy()):
        for j in range(5):
            for k in range(5):
                if b[j][k] == d: b[j][k] = 'x'
        if check_board(b):
            won += 1
            if won == N:
                score = sum([int(s) if s != 'x' else 0 for row in b for s in row])
                print(score * d)
                quit()
            else:
                boards.remove(b)
            continue