# import maxsize from sys module
# Used to return -infinite when stack is empty
from sys import maxsize


class Stack:
    # Function to create a stack. It initializes size of stack as 0
    def __init__(self):
        self.stack = []

    # Stack is empty when stack size is 0
    def isEmpty(self):
        return len(self.stack) == 0

    # Function to add an item to stack. It increases size by 1
    def push(self, item):
        self.stack.append(item)
        print(str(item) + " pushed to stack ")  # Convert item to string

    # Function to remove an item from stack. It decreases size by 1
    def pop(self):
        if self.isEmpty():
            return str(-maxsize - 1)  # return minus infinite
        return self.stack.pop()

    # Function to return the top from stack without removing it
    def peek(self):
        if self.isEmpty():
            return str(-maxsize - 1)  # return minus infinite
        return self.stack[len(self.stack) - 1]

    # Function to reverse an array using stack
    def reverseStack(self):
        new_array = []
        while not self.isEmpty():
            new_array.append(self.pop())
        return new_array


# Function to input the above data list from the keyboard
def getInput():
    inputted_array = input("Please enter an array to be reversed (e.g. 10 20 30 40 50): ")
    # The split() method splits the input string into individual string elements based on spaces.
    # The map(int, s.split()) applies the int function to each element, converting them to integers,
    # and list() collects the results into a list.
    int_array = list(map(int, inputted_array.split()))
    # return the user inputted string as an array of numbers
    return int_array


if __name__ == "__main__":
    user_input = getInput()
    print("Original array:", user_input)

    new_stack = Stack()

    for num in user_input:
        new_stack.push(num)

    reversed_array = new_stack.reverseStack()

    print("Reversed: ", reversed_array)
