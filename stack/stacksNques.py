class Empty(Exception):
    pass


class Stack:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        value = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        if self.size * 2 == self.capacity and self.capacity > 4:
            self.resize(self.capacity // 2)
        return value

    def push(self, value):
        if self.size < self.capacity:
            self.arr[self.size] = value
            self.size += 1
        else:
            self.resize(2 * self.capacity)
            self.push(value)

    def resize(self, capacity):
        old = self.arr
        self.capacity = capacity
        self.arr = [None] * capacity
        for i in range(self.size):
            self.arr[i] = old[i]


class Queue:

    def __init__(self, capacity=4):
        self.size = 0
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.front = 0
        self.back = 0

    def add(self, value):
        if self.size < self.capacity:
            available = (self.front + self.size) % self.capacity
            self.arr[available] = value
            self.size += 1
        else:
            self.resize(self.capacity * 2)
            self.add(value)

    def remove(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def resize(self, capacity):
        old = self.arr
        self.arr = [None] * capacity
        walk = self.front
        for k in range(self.size):
            self.arr[k] = old[walk]
            walk = (1 + walk) % self.capacity
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0


class DeQue:

    def __init__(self, capacity=4):
        self.size = 0
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.front = 0

    def push_front(self, value):
        if self.arr[self.front] is not None:
            self.move_front()
        self.arr[self.front] = value
        self.size += 1

    def move_front(self):
        if self.size == self.capacity:
            self.resize()
        temp = self.arr
        self.arr = [None] * self.capacity
        walk = self.front
        for i in range(self.size):
            self.arr[i+1] = temp[i]
        
    def push_back(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.arr[self.size] = value
        self.size += 1

    def pop_back(self):
        value = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        return value

    def pop_front(self):
        
        value = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
        


if __name__ == '__main__':
    queue = DeQue() 
    queue.push_front(1)
    print(queue.arr)
    queue.push_front(2)
    print(queue.arr)
    queue.push_back(3)
    print(queue.arr)
    queue.push_back(4)
    print(queue.arr)
    queue.pop_back()
    print(queue.arr)
    queue.pop_front()
    print(queue.arr)
    queue.pop_front()
    print(queue.arr)
    # print(queue.arr)
    # queue.remove()
    # print(queue.arr)
    # queue.add(5)
    # print(queue.arr)
    # queue.add(6)
    # print(queue.arr)
    # queue.add(7)
    # print(queue.arr)
    # queue.add(8)
    # print(queue.arr)
    # queue.add(9)
    # print(queue.arr)
    # queue.add(10)
    # queue.add(5)
    # print(queue.arr)
    # queue.add(6)
    # print(queue.arr)
    # queue.add(7)
    # print(queue.arr)
    # queue.add(8)
    # print(queue.arr)
    # queue.add(9)
    # print(queue.arr)
    # queue.add(10)
    # print(queue.remove())
    # print(queue.arr)  
    # print(queue.remove())
    # print(queue.arr)  
    # print(queue.remove())
    # print(queue.arr)  
    # print(queue.remove())
    # print(queue.arr)  
    # print(queue.remove())
    # print(queue.arr)  
    # print(queue.remove())
    # print(queue.arr)  
    # print(queue.remove())
    # print(queue.arr)  
    
    # stack = Stack()
    # stack.push(3)
    # stack.push(4)
    # stack.push(5)
    # stack.push(6)
    # stack.push(7)
    # stack.push(8)
    # stack.push(9)
    # stack.push(10)
    # stack.push(3)
    # stack.push(4)
    # stack.pop()
    # stack.push(5)
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.push(6)
    # stack.push(7)
    # stack.push(8)
    # stack.push(9)
    # stack.push(10)
    # stack.push(3)
    # stack.push(4)
    # stack.push(5)
    # stack.push(6)
    # stack.push(7)
    # stack.push(8)
    # stack.push(9)
    # stack.push(10)
    # stack.push(3)
    # stack.push(4)
    # stack.push(5)
    # stack.push(6)
    # stack.push(7)
    # stack.push(8)
    # stack.push(9)
    # stack.push(10)

    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)

    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    

    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    

    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    # print(stack.pop())
    # print(stack.arr)
    
