def makeArrayConsecutive2(statues):
    statues.sort()
    return (statues[len(statues) - 1] - statues[0] + 1) - len(statues)

def almostIncreasingSequence(sequence):

    sub_sequence = []

    if sequence[0] < sequence[1]:
        sub_sequence.append(sequence[0])
    else:
        sub_sequence.append(sequence[1])

    for index in range(1, len(sequence) - 1):
        if sequence[index] < sequence[index + 1] and sequence[index] > sub_sequence[-1]:
            sub_sequence.append(sequence[index])
        elif sequence[index + 1] > sub_sequence[-1]:
            sub_sequence.append(sequence[index + 1])
        elif sequence[index] > sub_sequence[-1]:
            sub_sequence.append(sequence[index])

    if len(sequence) - len(sub_sequence) > 1:
        return False

    return True

def matrixElementsSum(matrix):

    total_room_value = 0
    invalid_index = []

    for row in matrix:
        for index, roomValue in enumerate(row):
            if index in invalid_index:
                continue

            if roomValue != 0:
                total_room_value += roomValue
            else:
                invalid_index.append(index)

    return total_room_value

def matrixElementsSum2(matrix):

    total_room_value = 0

    for colIndx in range(0, len(matrix[0])):
        for rowIndx in range(0, len(matrix)):
            if matrix[rowIndx][colIndx] != 0:
                total_room_value += matrix[rowIndx][colIndx]
            else:
                break

    print(total_room_value)
    return total_room_value

def main():
    statues = [5, 3, 1]
    assert makeArrayConsecutive2(statues) is 2

    sequence = [1, 3, 2]
    assert almostIncreasingSequence(sequence) is True

    sequence = [1, 3, 2, 1]
    assert almostIncreasingSequence(sequence) is False

    sequence = [1, 2, 1, 2]
    assert almostIncreasingSequence(sequence) is False

    sequence = [10, 1, 2, 3, 4, 5]
    assert almostIncreasingSequence(sequence) is True

    matrix = [
        [0, 1, 1, 2],
        [0, 5, 0, 0],
        [2, 0, 3, 3]]
    assert matrixElementsSum(matrix) is 9

    matrix = [
        [1,1,1,0],
        [0,5,0,1],
        [2,1,3,10]]
    assert matrixElementsSum(matrix) is 9

    matrix = [
        [1,1,1],
        [2,2,2],
        [3,3,3]]
    assert matrixElementsSum(matrix) is 18

    matrix = [[0]]
    assert matrixElementsSum(matrix) is 0

    matrix = [
        [0, 1, 1, 2],
        [0, 5, 0, 0],
        [2, 0, 3, 3]]
    assert matrixElementsSum2(matrix) is 9

    matrix = [
        [1,1,1,0],
        [0,5,0,1],
        [2,1,3,10]]
    assert matrixElementsSum2(matrix) is 9

    matrix = [
        [1,1,1],
        [2,2,2],
        [3,3,3]]
    assert matrixElementsSum2(matrix) is 18

    matrix = [[0]]
    assert matrixElementsSum2(matrix) is 0

    print("All tests success!!")

if __name__ == '__main__':
    main()
