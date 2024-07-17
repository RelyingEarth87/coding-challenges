from typing import Tuple, Any

class Queue:
    """A First-In-First-Out Queue, built from a list
    """
    def __init__(self) -> None:
        """Initializes the Queue as a lis object
        """
        self.items: list = []
    
    def enqueue(self, item) -> None:
        """Adds an item to the end of the Queue

        Args:
            item (Any): An item to be added to the Queue
        """
        self.items.append(item)
    
    def dequeue(self) -> Any:
        """Removes an item from the front of the Queue

        Returns:
            Any: The item that was removed from the front of the Queue
        """
        item = self.items.pop(0)
        return item
    
    def front(self) -> Any:
        """Returns the first item in the Queue

        Returns:
            Any: The item at the front of the Queue
        """
        return self.items[0]
    
    def isEmpty(self) -> bool:
        """Returns whether or not the Queue is empty

        Returns:
            bool: True if the Queue is empty, False if Queue contains items
        """
        return len(self.items) == 0

class DoubleQueueStack:
    """A Last-In-First-Out Stack, built from two Queues
    """
    def __init__(self) -> None:
        """Initializes 2 Queues to keep track of the stack information
        """
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.stack_length = 0

    def push(self, value) -> None:
        """Adds an item to the end of the Stack

        Args:
            value (Any): An item to be added to the Stack
        """
        self.stack_length += 1
        self.queue1.enqueue(value)
        # Returning a null value just for the checks later on
        return None
    
    def pop(self) -> Any:
        """Removes an item from the end of the Stack, returning its value

        Returns:
            Any: The previous last value from the Stack
        """
        # moving through the first queue and adding elements to the second queue until the last element
        stack_length = self.stack_length
        while stack_length > 1:
            item = self.queue1.dequeue()
            self.queue2.enqueue(item)
            stack_length -= 1
        # removing the last element to return its value
        value = self.queue1.dequeue()
        # interchanging the names of the two queues
        temp = self.queue2
        self.queue2 = self.queue1
        self.queue1 = temp
        self.stack_length -= 1

        return value
    
    def top(self) -> Any:
        """Returns the end value from the Stack, without removing it

        Returns:
            Any: The last value currently on the Stack
        """
        # moving through the first queue and adding elements to the second queue until the last element
        stack_length = self.stack_length
        while stack_length > 1:
            item = self.queue1.dequeue()
            self.queue2.enqueue(item)
            stack_length -= 1
        # getting the end value from the first queue to return its value
        value = self.queue1.front()
        # adding the last element to the second queue
        item = self.queue1.dequeue()
        self.queue2.enqueue(item)
        # interchanging the names of the two queues
        temp = self.queue2
        self.queue2 = self.queue1
        self.queue1 = temp

        return value
    
    def empty(self) -> bool:
        """Returns whether or not the Stack is empty

        Returns:
            bool: True if the Stack is empty, False if Stack contains items
        """
        return self.stack_length == 0

class SingleQueueStack:
    """A Last-In-First-Out Stack, built from a single Queue
    """
    def __init__(self) -> None:
        """Initializes a single Queue to function as a Stack
        """
        self.queue = Queue()
        self.stack_length = 0

    def push(self, value) -> None:
        """Adds an item to the end of the Stack

        Args:
            value (Any): An item to be added to the Stack
        """
        self.stack_length += 1
        self.queue.enqueue(value)
        # Returning a null value just for the checks later on
        return None

    def pop(self) -> Any:
        """Removes an item from the end of the Stack, returning its value

        Returns:
            Any: The previous last value from the Stack
        """
        # loops through the Queue, re-appending every item back to the end of itself, until the last item
        stack_length = self.stack_length
        while stack_length > 1:
            item = self.queue.dequeue()
            self.queue.enqueue(item)
            stack_length -= 1

        # removing and returning the last item
        value = self.queue.dequeue()
        return value

    def top(self) -> Any:
        """Returns the end value from the Stack, without removing it

        Returns:
            Any: The last value currently on the Stack
        """
        # loops through the Queue, re-appending every item back to the end of itself, until the last item
        stack_length = self.stack_length
        while stack_length > 1:
            item = self.queue.dequeue()
            self.queue.enqueue(item)
            stack_length -= 1

        # removing the last item, re-appending it to the Queue, then returning its value
        value = self.queue.dequeue()
        self.queue.enqueue(value)
        return value

    def empty(self) -> bool:
        """Returns whether or not the Stack is empty

        Returns:
            bool: True if the Stack is empty, False if Stack contains items
        """
        return self.stack_length == 0

def handle_input(functions, values) -> Tuple[list, list]:
    """A function to handle the test case inputs

    Args:
        functions (list): the methods to execute for each Stack
        values (list): the positional arguments for each method

    Returns:
        Tuple[list, list]: The results, for each stack, of executing each method
    """
    output1, output2 = [], []

    for i in range(len(functions)):
        function = functions[i]
        if function == "MyStack":
            stack1 = DoubleQueueStack()
            stack2 = SingleQueueStack()
            output1.append(None)
            output2.append(None)
        elif function == "push":
            value = values[i][0]
            push1 = stack1.push(value)
            push2 = stack2.push(value)
            output1.append(push1)
            output2.append(push2)
        elif function == "pop":
            pop1 = stack1.pop()
            pop2 = stack2.pop()
            output1.append(pop1)
            output2.append(pop2)
        elif function == "top":
            top1 = stack1.top()
            top2 = stack2.top()
            output1.append(top1)
            output2.append(top2)
        elif function == "empty":
            empty1 = stack1.empty()
            empty2 = stack2.empty()
            output1.append(empty1)
            output2.append(empty2)
        
    return(output1, output2)

def main() -> None:
    """A main entry point to handle running the test cases and printing the results in a readable manner
    """
    functions = ["MyStack", "push", "push", "top", "pop", "empty"]
    values = [[], [1], [2], [], [], []]
    answers = [None, None, None, 2, 2, False]

    # verifying our outputs are correct
    output1, output2 = handle_input(functions, values)
    assert output1 == answers
    assert output1 == answers

    print(f"""Input
{functions}
{values}
Output
2 Queue Stack: {output1}
Single Queue Stack: {output2}""")

if __name__ == '__main__':
    main()