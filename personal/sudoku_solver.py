def cross(a,b):
    return [s+t for s in a for t in b]

def main():
    ROWS = 'ABCDEFGHI'
    COLUMNS = '123456789'

    BOXES = cross(ROWS, COLUMNS)
    ROW_UNITS = [cross(r, COLUMNS) for r in ROWS]
    COLUMNS_UNITS = [cross(ROWS, c) for c in COLUMNS]
    SQUARE_UNITS = [cross(rs, cs) for rs in (ROWS[:3], ROWS[3:6], ROWS[6:]) for cs in (COLUMNS[:3], COLUMNS[3:6], COLUMNS[6:])]

    UNITLIST = ROW_UNITS + COLUMNS_UNITS + SQUARE_UNITS

    GRID_VALUES = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    
    print(set_boxes_values(GRID_VALUES, BOXES))

def set_boxes_values(values, boxes):
    board = {}
    for index in range(len(boxes)):
        board[boxes[index]] = values[index]
    return board

def display(board):
    print(board[:9])
    print(board[9:18])

if __name__ == '__main__':
    main()
