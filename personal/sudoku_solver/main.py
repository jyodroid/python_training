#! /usr/bin/env python
from sudoku_solver import SudokuSolver

def main():
    GRID_VALUES = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    GRID_VALUES_HARD = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    ROWS = 'ABCDEFGHI'
    COLUMNS = '123456789'

    BOXES = cross(ROWS, COLUMNS)
    ROW_UNITS = [cross(r, COLUMNS) for r in ROWS]
    COLUMN_UNITS = [cross(ROWS, c) for c in COLUMNS]
    SQUARE_UNITS = [cross(rs, cs) for rs in (ROWS[:3], ROWS[3:6], ROWS[6:]) for cs in (COLUMNS[:3], COLUMNS[3:6], COLUMNS[6:])]
    UNIT_LIST = ROW_UNITS + COLUMN_UNITS + SQUARE_UNITS

    solver = SudokuSolver(BOXES, UNIT_LIST)
    board_normal = solver.grid_values(GRID_VALUES)
    board_hard = solver.grid_values(GRID_VALUES_HARD)

    print("-- Normal: Unsolved --")
    print("##############################")
    solver.display(solver.grid_values(GRID_VALUES), ROWS, COLUMNS)

    # Setting all posibilities on empty spaces
    all_choises_board = solver.grid_all_posibilities(GRID_VALUES)

    # Constraints propagation https://youtu.be/aSYDBcbvC5Y
    print("-- Normal: Solved --")
    print("##############################")
    solver.display(solver.reduce_puzzle(all_choises_board), ROWS, COLUMNS)

    all_choises_board_hard = solver.grid_all_posibilities(GRID_VALUES_HARD)

    # Hard Sudoku
    print("-- Hard: Unsolved --")
    print("##############################")
    solver.display(solver.grid_values(GRID_VALUES_HARD), ROWS, COLUMNS)

    # Reduce does not work anymore with eleminate and only choise technique
    print("-- Hard: Unsolved but reduced --")
    print("##############################")
    solver.display(solver.reduce_puzzle(all_choises_board_hard), ROWS, COLUMNS)

    # Hard using DFS
    print("-- Hard: DFS --")
    print("##############################")
    solver.display(solver.search(all_choises_board_hard), ROWS, COLUMNS)

def cross(a, b):
    return [s+t for s in a for t in b]

if __name__ == '__main__':
    main()
