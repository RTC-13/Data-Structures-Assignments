# Basically the same as in it was in the notes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # we only need append since all we need to do is add items to the list.
    def append(self, data):
        new_node = Node(data)
        # if there is no head yet on the linked list, set this one to it.
        if not self.head:
            self.head = new_node
            return
        # start of the list
        last_node = self.head
        # loop to ger to the end of the list
        while last_node.next:
            last_node = last_node.next
        # set the last node that we get when the loop ends to the new_node we are appending.
        last_node.next = new_node

        # remembered this method: used to represent an object as a string helps see the process.
    def __repr__(self):
        position = self.head
        items = []

        while position:
            items.append(position.data)
            position = position.next

        return str(items)

    def average_even_nums(self):
        result = 0
        num_of_evens = 0
        current = self.head

        while current:
            if current.data % 2 == 0:  # Check if the number is even
                result += current.data  # Add to the result
                num_of_evens += 1  # Increment the count of even numbers
            current = current.next  # Move to the next node

        #retuens avergae: if no even numbers returns 0.
        return result / num_of_evens if num_of_evens > 0 else 0

    def merge_sort(self):
        self.head = self.merge_sort_helper(self.head)

    def merge_sort_helper(self, head):
        if not head or not head.next:
            return head

        # Split the list into two
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        # Recursive
        left = self.merge_sort_helper(head)
        right = self.merge_sort_helper(next_to_middle)

        # Merge the sorted halves
        sorted_list = self.merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result


if __name__ == "__main__":
    # user inputs a string -> we need to input it into a list.
    user_input = input("Enter a list of integers with spaces between each number: ")
    L_list = LinkedList()
    for num in user_input.split(" "):
        # Make sure to input them as numbers: was causing issues.
        L_list.append(int(num))

    print(L_list.__repr__()) # user input: representation of inputted linked list:


    # Average value of even elements. Using the function I made for the lists assignment.
    average = L_list.average_even_nums()
    print("Average of even numbers in our linked list: ", average)

    # merge sort in ascending order.
    L_list.merge_sort()
    print("Ascending merge sorted list: ", L_list.__repr__())






