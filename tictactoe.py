"""
Tic Tac Toe Player
"""

from distutils.file_util import copy_file
from distutils.util import copydir_run_2to3
import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count=0
    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    if(count%2 == 1):
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = set()
    #temp = tuple()
    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                ans.add((i,j))
    
    return ans
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board=copy.deepcopy(board)
    i=action[0]
    j=action[1]
    if board[i][j] != EMPTY:
        raise 
    else:
        p=player(board)
        new_board[i][j]=p
        return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if((board[0][0]==board[0][1]==board[0][2]) or (board[0][0]==board[1][1]==board[2][2]) or (board[0][0]==board[1][0]==board[2][0])):
        return board[0][0]
    elif((board[0][1]==board[1][1]==board[2][1])):
        return board[0][1]
    elif ((board[0][2]==board[1][2]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0])):
        return board[0][2]
    elif((board[1][0]==board[1][1]==board[1][2])):
        return board[1][0]
    elif((board[2][0]==board[2][1]==board[2][2])):
        return board[2][0]
    else:
        return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count=0
    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    if ((winner(board)==X) or (count==0)or(winner(board)==O)):
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if win==X:
        return 1
    elif win==O:
        return -1
    else:
        return 0
    raise NotImplementedError

def min_value(board):
    v=float('inf')
    if(terminal(board)):
        return utility(board)
    else:
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
def max_value(board):
    v=float('-inf')
    if(terminal(board)):
        return utility(board)
    else:
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    else:
        if player(board)==X:
            v=float('-inf')
            best=()
            for action in actions(board):
                if (min_value(result(board,action)) > v):
                    v=min_value(result(board,action)) 
                    best=action
            return best
        else:
            v=float('inf')
            best=()
            for action in actions(board):
                if (max_value(result(board,action)) < v):
                    v=max_value(result(board,action)) 
                    best=action            
            return best
            
    raise NotImplementedError
