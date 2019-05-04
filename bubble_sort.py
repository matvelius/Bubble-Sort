array = [-10, -4, 8, -5, 2, 9, 5, 6, 3]
# array = [1, 2]
print("original array: ")
print(array)

def bubbleSort(array):

    lowerIndex = 0
    upperIndex = len(array) - 1

    # repeat until we're at index 0
    while upperIndex > lowerIndex:

        for index in range(upperIndex):
            if array[index] > array[index + 1]:
                #swap the numbers
                temp = array[index + 1]
                array[index + 1] = array[index]
                array[index] = temp

        upperIndex -= 1


        # # first find the largest number, and save its index (and/or write helper swap function?)
        # currentLargestNumber = 0
        # indexOfCurrentLargestNumber = 0
        #
        # for index in range(upperIndex + 1):
        #     # tempIndex = 0
        #     # tempLargestNumber = array[tempIndex]
        #     print(f"current index: {index}, value at current index: {array[index]}")
        #     if array[index] > currentLargestNumber:
        #         indexOfCurrentLargestNumber = index
        #         currentLargestNumber = array[index]
        #
        # print(f'current largest number found is: {currentLargestNumber} at index {indexOfCurrentLargestNumber}')
        #
        # # put largest number at the end of the array
        # temp = array[upperIndex]
        # array[upperIndex] = currentLargestNumber
        # # put whatever was at the end of the array where the largest number was
        # array[indexOfCurrentLargestNumber] = temp
        #
        # # decrease upperIndex by 1
        # upperIndex -= 1
        print(f'upper index is now {upperIndex}')

        print(f'result: {array}')
        print("")

    return array







    # then swap that number with whatever the last number in the array is


    # then go through the array again, but swap with the 2nd to last number




        # while number > array[lowerIndex + 1]:
        #     temp = array[lowerIndex + 1]
        #     array[lowerIndex + 1] = array[lowerIndex]
        #     array[lowerIndex] = temp
        #
        #     print(array)
        #     lowerIndex += 1

    # while lowerIndex < upperIndex:
    #     if array[lowerIndex] > array[lowerIndex + 1]:
    #         temp = array[lowerIndex + 1]
    #         array[lowerIndex + 1] = array[lowerIndex]
    #         array[lowerIndex] = temp
    #
    #     print(array)
    #     lowerIndex += 1

result = bubbleSort(array)
print(result)