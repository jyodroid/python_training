def missingNumber(arr):
    vaseel = [False] * (len(arr) + 1)

    for number in range(0, len(arr)):
        vaseel[arr[number]] = True

    for index in range(0, len(vaseel)):
        if vaseel[index] == False:
            return index

    return -1

def missingNumberPySerach(arr):

    for number in range(0, len(arr) + 1):
        try:
            arr.index(number)
        except Exception:
            return number
    return -1

def missingNumberGaussSum(arr):

    gauss_sum = (len(arr)*(len(arr)+1))/2
    obt_sum = 0

    for number in range(0, len(arr)):
        obt_sum += arr[number]

    return gauss_sum - obt_sum

def main():
    print missingNumber([3,1,0])
    print missingNumberPySerach([3,1,0])
    print missingNumberGaussSum([3,1,2,0])

if __name__ == '__main__':
    main()
