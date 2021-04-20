class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = list()
        self.queue2 = list()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if x:
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))
            self.queue1.append(x)
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.queue1 and self.queue2:
            self.queue1.append(self.queue2.pop())
        if self.queue1: return self.queue1.pop()
        else: return print("queue is empty.")


    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.queue1 and self.queue2:
            self.queue1.append(self.queue2.pop())
        if self.queue1: return self.queue1[-1]
        else: return print("queue is empty.")
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.queue1 or self.queue2 : return False
        else: return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()