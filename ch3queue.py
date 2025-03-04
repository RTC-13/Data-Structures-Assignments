from queue import Queue


# Function to input the user input

def getInput():
    inputted_array = input("Please enter an array to be reversed (e.g. 10 20 30 40 50): ")
    # The split() method splits the input string into individual string elements based on spaces.
    # The map(int, s.split()) applies the int function to each element, converting them to integers,
    # and list() collects the results into a list.
    int_array = list(map(int, inputted_array.split()))
    # return the user inputted string as an array of numbers
    return int_array


# Function to reverse inputted array

def reverseArray(input_list):
    q = Queue()
    reversedArray = []

    for number in input_list:
        q.put(number)

    while not q.empty():
        reversedArray.insert(0, q.get())

    return reversedArray


if __name__ == "__main__":
    numbers = getInput()
    print("Input: ",numbers)
    reverse = reverseArray(numbers)
    print("Reversed: ", reverse)
