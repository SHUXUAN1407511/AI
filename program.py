# COMP30024 Artificial Intelligence, Semester 1 2025
# Project Part A: Single Player Freckers

from .core import CellState, Coord, Direction, MoveAction
from .utils import render_board
from math import sqrt
import heapq

#def two function to calculate exp_distance(fn) and exp_remain_distance(hn)
def euclidean_distance(coord1: Coord, coord2: Coord) -> float:
    return sqrt((coord1.r - coord2.r) ** 2 + (coord1.c - coord2.c) ** 2)

def manhattan_distance(coord1: Coord, coord2: Coord) -> int:
    return abs(coord1.r - coord2.r) + abs(coord1.c - coord2.c)

class Node:
    def __init__(self, position, parent = None, g = 0, h = 0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f
    
def A_star(board_list, start, end):
    
    priority_list = []
    heapq.heappush(priority_list, Node(start, None, 0, manhattan_distance(start,end)))
    used_set = set()
    
    
    while priority_list:
        current_node = heapq.heappop(priority_list)
        
    
    

def search(
    board: dict[Coord, CellState]
) -> list[MoveAction] | None:

    
    start_coord = []
    end_coord = []
    
    board_list = [[0 for i in range(8)] for j in range(8)]

    for coord, cellstate in board.items():
        
        if cellstate == CellState.RED:
            board_list[coord.r][coord.c] = 1
            start_coord.append(coord.r)
            start_coord.append(coord.c)
        elif cellstate == CellState.BLUE:
            board_list[coord.r][coord.c] = 2
        elif cellstate == CellState.LILY_PAD:
            board_list[coord.r][coord.c] = 3
            
        if cellstate != CellState.BLUE and coord.r == 7:
            end_coord.append([coord.r,coord.c])
            
    print (board_list)
    print(start_coord)
    print(end_coord)
    
    
    

    print(render_board(board, ansi=True))

    return [
        MoveAction(Coord(0, 5), [Direction.Down]),
        MoveAction(Coord(1, 5), [Direction.DownLeft]),
        MoveAction(Coord(3, 3), [Direction.Left]),
        MoveAction(Coord(3, 2), [Direction.Down, Direction.Right]),
        MoveAction(Coord(5, 4), [Direction.Down]),
        MoveAction(Coord(6, 4), [Direction.Down]),
    ]
