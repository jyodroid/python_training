import sys
# Problem with matrix with more columns that rows
def spiral_matrix(dummy_matrix):

    if len(dummy_matrix) == 0:
        print "Empty"
        return

    col_ini = 0
    col_end = len(dummy_matrix[0])

    row_ini = 0
    row_end = len(dummy_matrix)

    while ((row_ini < row_end) and (col_ini < col_end)):
        # Run from start top from left to rigth
        for top in range(col_ini, col_end):
            print dummy_matrix[row_ini][top],

        # When reach right start from top to bottom
        # First to print is last printed in last step so avoid to print it (start from row_ini + 1)
        for rigth in range(row_ini + 1, row_end):
            print dummy_matrix[rigth][col_end-1],

        # When reach bottom go from right to left
        # First to print is last printed in last step so avoid to print it (start from col_end - 1)
        for bottom in go_back_range(col_end - 1, col_ini):
            print dummy_matrix[row_end - 1][bottom - 1],

        # When reach left go to top again
        # First to print is last printed in last step so avoid to print it (start from row_end - 1)
        # Last to print is first printed in top step so avoid to print it (end in row_ini + 1)
        for left in go_back_range(row_end - 1, row_ini + 1):
            print dummy_matrix[left - 1][col_ini],

        # Reduce the matrix borders
        row_ini += 1
        row_end -= 1
        col_ini += 1
        col_end -= 1

# Helper go back method
def go_back_range(start, end):
    while start > end:
        yield start
        start -= 1

# sig_file: toma un archivo con texto y firma digitalmente el texto
# @autor: John Jairo Tangarife Abril 6 del 2017
def main():
    spiral_matrix([[1,2,3],[11,12,13],[21,22,23],[31,32,33]])
    print
    spiral_matrix([[1,2,3],[8,9,4],[7,6,5]])
    print
    spiral_matrix([[1]])
    print
    spiral_matrix([[0,3],[5,5]])
    print
    spiral_matrix([[33,29,-15,-20,-41,-1,34,20,-41,44],[14,-11,-27,-35,29,-14,34,-41,49,19],[-12,-44,44,-43,-13,-6,40,-24,-6,8],[-40,4,27,2,2,15,38,4,-13,15],[-42,3,5,10,15,34,-18,-22,9,38]])
    print
    spiral_matrix([])
    print
    spiral_matrix([[19,-17,23,44,12,-23,-37,26,-38,-36],[38,26,7,-3,-48,40,36,-20,22,-50],[39,50,-29,48,44,-31,-17,32,-42,-27],[-44,-47,47,43,31,11,-14,-22,-46,-18],[-38,31,0,-14,-6,48,30,-41,31,-24],[21,39,-39,-4,45,22,-23,-40,24,-16],[33,-1,46,-36,26,-36,4,29,16,-12],[7,-3,46,36,-4,-22,17,12,-13,-28],[-33,-1,30,27,-44,-7,6,-37,31,48],[50,23,43,36,-29,5,-45,33,-24,41]])

if __name__ == '__main__':
    main()
