def cross(a,b):
    return [s+t for s in a for t in b]

# My solution
def set_boxes_values(values, boxes):
    board = {}
    for index in range(len(boxes)):
        board[boxes[index]] = values[index]
    return board

#Better solution
def grid_values(values, boxes):
    assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, values))

# The elimination technique https://youtu.be/6rFOX2jHB2g
#Adding Grid values with elimination technique so we can add possible values to grid
def grid_all_posibilities(values, boxes):
    assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
    board = {}
    for index in range(len(boxes)):
        value = values[index]
        if value == ".":
            board[boxes[index]] = "123456789"
        else:
            board[boxes[index]] = value
    return board

# Udacity solution
def another_grid_all_posibilities(values, boxes):
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))

# Find board places with one digit element and discard from peers other options
def eliminate(values, boxes, unit_list):

    units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values

# Only choise technique: https://youtu.be/sSjYn-Kex1A
def only_choise(values, unitlist):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def display(values, boxes, rows, cols):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# Constraints propagation on solving puzzle
def reduce_puzze(values, boxes, unitlist):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solve_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        #Use eliminate strategy
        eliminate(values, boxes, unitlist)

        #Use Only choise strategy
        only_choise(values, unitlist)

        #Check how many boxes have a determined value to compare
        solve_values_after = len([box for box in values.keys() if len(values[box]) == 1 ])

        #If no new values were added, stop the loop.
        stalled = solve_values_before == solve_values_after

        #Sanity check: return false if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False

    return values


def main():
    ROWS = 'ABCDEFGHI'
    COLUMNS = '123456789'

    BOXES = cross(ROWS, COLUMNS)
    ROW_UNITS = [cross(r, COLUMNS) for r in ROWS]
    COLUMNS_UNITS = [cross(ROWS, c) for c in COLUMNS]
    SQUARE_UNITS = [cross(rs, cs) for rs in (ROWS[:3], ROWS[3:6], ROWS[6:]) for cs in (COLUMNS[:3], COLUMNS[3:6], COLUMNS[6:])]

    UNITLIST = ROW_UNITS + COLUMNS_UNITS + SQUARE_UNITS

    GRID_VALUES = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

    board = grid_values(GRID_VALUES, BOXES)
    print("-- Unsolved --")
    print("##############################")
    display(board, BOXES, ROWS, COLUMNS)
    # print("-- Setting all posibilities --")
    # print("##############################")
    all_choises_board = grid_all_posibilities(GRID_VALUES, BOXES)
    # display(all_choises_board, BOXES, ROWS, COLUMNS)
    #
    # # Eliminate
    # print("-- Discarting with elimination --")
    # print("##############################")
    # eliminated_values_board = eliminate(all_choises_board, BOXES, UNITLIST)
    # display(eliminated_values_board, BOXES, ROWS, COLUMNS)
    #
    # # Only Choise
    # print("-- Discarting with OnlyChoise after elimination --")
    # print("##############################")
    # only_choise_board = only_choise(eliminated_values_board, UNITLIST)
    # display(only_choise_board, BOXES, ROWS, COLUMNS)

    # Constraints propagation https://youtu.be/aSYDBcbvC5Y
    print("-- Solved --")
    print("##############################")
    display(reduce_puzze(all_choises_board, BOXES, UNITLIST), BOXES, ROWS, COLUMNS)

if __name__ == '__main__':
    main()
