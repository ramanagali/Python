# Insertion sort in Python
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertionSort(elements)
    print('Sorted Array in Ascending Order:')
    print(elements)

    # tests = [
    #     [11, 9, 29, 7, 2, 15, 28],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]
    # for elements in tests:
    #     insertionSort(elements)
