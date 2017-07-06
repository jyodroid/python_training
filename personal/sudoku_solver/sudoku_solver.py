# Class https://docs.python.org/3/tutorial/classes.html
class SudokuSolver:

    def __init__(self, boxes, unitlist):
        self.boxes = boxes
        self.unitlist = unitlist

    # My solution
    def set_boxes_values(values):
        board = {}
        for index in range(len(self.boxes)):
            board[self.boxes[index]] = values[index]
        return board

    #Better solution
    def grid_values(self, values):
        assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
        return dict(zip(self.boxes, values))

    # The elimination technique https://youtu.be/6rFOX2jHB2g
    #Adding Grid values with elimination technique so we can add possible values to grid
    def grid_all_posibilities(self, values):
        assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
        board = {}
        for index in range(len(self.boxes)):
            value = values[index]
            if value == ".":
                board[self.boxes[index]] = "123456789"
            else:
                board[self.boxes[index]] = value
        return board

    # Udacity solution
    def another_grid_all_posibilities(values):
        values = []
        all_digits = '123456789'
        for c in grid:
            if c == '.':
                values.append(all_digits)
            elif c in all_digits:
                values.append(c)
        assert len(values) == 81
        return dict(zip(self.boxes, values))

    # Find board places with one digit element and discard from peers other options
    def __eliminate(self, values):

        units = dict((s, [u for u in self.unitlist if s in u]) for s in self.boxes)
        peers = dict((s, set(sum(units[s],[]))-set([s])) for s in self.boxes)

        solved_values = [box for box in values.keys() if len(values[box]) == 1]
        for box in solved_values:
            digit = values[box]
            for peer in peers[box]:
                values[peer] = values[peer].replace(digit, '')
        return values

    # Only choise technique: https://youtu.be/sSjYn-Kex1A
    def __only_choise(self, values):
        for unit in self.unitlist:
            for digit in '123456789':
                dplaces = [box for box in unit if digit in values[box]]
                if len(dplaces) == 1:
                    values[dplaces[0]] = digit
        return values

    # Constraints propagation on solving puzzle
    def reduce_puzzle(self, values):
        stalled = False
        while not stalled:
            # Check how many boxes have a determined value
            solve_values_before = len([box for box in values.keys() if len(values[box]) == 1])

            #Use eliminate strategy
            self.__eliminate(values)

            #Use Only choise strategy
            self.__only_choise(values)

            #Check how many boxes have a determined value to compare
            solve_values_after = len([box for box in values.keys() if len(values[box]) == 1 ])

            #If no new values were added, stop the loop.
            stalled = solve_values_before == solve_values_after

            #Sanity check: return false if there is a box with zero available values:
            if len([box for box in values.keys() if len(values[box]) == 0]):
                return False

        return values

    # search strategy https://youtu.be/omveZu2gRLs
    def search(self, values):
    # "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
        values = self.reduce_puzzle(values)
        if values is False:
            return False #Error propagation
        if all(len(values[s]) == 1 for s in self.boxes):
            return values # Solved

        # Choose one of the unfilled squares with the fewest possibilities
        n, s = min((len(values[s]), s) for s in self.boxes if len(values[s]) > 1)

        # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
        for value in values[s]:
            new_sudoku = values.copy()
            new_sudoku[s] = value
            attempt = self.search(new_sudoku)
            if attempt:
                return attempt

    def display(self, values, rows, columns):

        """
        Display the values as a 2-D grid.
        Input: The sudoku in dictionary form
        Output: None
        """
        width = 1+max(len(values[s]) for s in self.boxes)
        line = '+'.join(['-'*(width*3)]*3)
        for r in rows:
            print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                          for c in columns))
            if r in 'CF': print(line)
        return
