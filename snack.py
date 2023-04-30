import queue
q = queue.Queue()

# Adding elements to a queue
q.put('a')
q.put('b')
q.put('c')

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.empty())
print(q.get())
print(q.empty())



class Snake:
    def __init__(cls) -> None:
        cls.q = queue.Queue()

    @classmethod
    def ate_apple(cls, apple):
        pass

    @classmethod
    def move(cls):
        pass


