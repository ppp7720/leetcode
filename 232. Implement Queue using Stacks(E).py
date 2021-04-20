class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()
        self.temp = list()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack:
            while self.stack: self.temp.append(self.stack.pop())
            pop = self.temp.pop()
            while self.temp: self.stack.append(self.temp.pop())
            return pop
        else: return print('queue is empty!')
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack: return self.stack[0]
        else: return print('queue is empty!')
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack: return False
        else: return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()