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

    return total_room_value

def allLongestStrings(inputArray):

    longest = 0
    outputArray = []

    for word in inputArray:
        if len(word) > longest:
            longest = len(word)
            outputArray.clear()
            outputArray.append(word)

        elif len(word) == longest:
            outputArray.append(word)

    return outputArray

def commonCharacterCount(s1, s2):
    dict_s1 = {}

    for char in s1:
        if char in dict_s1:
            dict_s1[char] += 1
        else:
            dict_s1[char] = 1

    dict_s2 = {}
    for char in s2:
        if char in dict_s2:
            dict_s2[char] += 1
        else:
            dict_s2[char] = 1

    totalCommon = 0
    for char in list(dict_s1):
        if char in dict_s2:
            if dict_s1[char] > dict_s2[char]:
                totalCommon += dict_s2[char]
            else:
                totalCommon += dict_s1[char]

    return totalCommon

def isLucky(n):

    sn = str(n)
    lenSn = int(len(sn)/2)

    sum1 = 0
    sum2 = 0

    for number in sn[:lenSn]:
        sum1 += int(number)
    for number in sn[lenSn:]:
        sum2 += int(number)

    return sum1 == sum2

def sortByHeight(a):

    sorted_people = []
    tree_positions = []

    for index,person in enumerate(a):
        if person != -1:
            sorted_people.append(person)
        else:
            tree_positions.append(index)

    sorted_people.sort()

    for treeIndex in tree_positions:
        sorted_people.insert(treeIndex, -1)

    return sorted_people

def reverseParentheses(s):

    # Stack
    open_par_indexes = []

    # Queue
    close_par_indexes = []

    for index, char in enumerate(s):
        if char == "(":
            open_par_indexes.append(index)
        elif char == ")":
            close_par_indexes.append(index)

    for closing_index in close_par_indexes:
        while open_par_indexes[-1] > closing_index:
            vassel = open_par_indexes[-1]
            open_par_indexes[-1] = open_par_indexes[-2]
            open_par_indexes[-2] = vassel

        init_index = open_par_indexes.pop()

        # To revert substrings
        substring = s[init_index + 1: closing_index]
        s = s[:init_index+1] + substring[::-1] + s[closing_index:]

    # remove parentesis
    s = s.replace('(','')
    s = s.replace(')','')

    return s

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

    inputArray = ["aba", "aa", "ad", "vcd", "aba"]
    assert allLongestStrings(inputArray) == ["aba", "vcd", "aba"]

    s1 = "aabcc"
    s2 = "adcaa"
    assert commonCharacterCount(s1, s2) is 3

    s1 = "a"
    s2 = "aaa"
    assert commonCharacterCount(s1, s2) is 1

    n = 1230
    assert isLucky(n) is True

    n = 239017
    assert isLucky(n) is False

    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    assert sortByHeight(a) == [-1, 150, 160, 170, -1, -1, 180, 190]

    s = "a(bc)de"
    assert reverseParentheses(s) == "acbde"

    s = "a(bcdefghijkl(mno)p)q"
    assert reverseParentheses(s) == "apmnolkjihgfedcbq"

    s = "co(de(fight)s)"
    assert reverseParentheses(s) == "cosfighted"

    s = "abc(cba)ab(bac)c"
    assert reverseParentheses(s) == "abcabcabcabc"

    print("All tests success!!")

if __name__ == '__main__':
    main()
