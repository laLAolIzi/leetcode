class MaxQueue:

    def __init__(self):
        self.que=[]
        self.max=0
    def max_value(self) -> int:
        return self.max

    def push_back(self, value: int) -> None:
        self.que.append(value)
        self.max=value if value>self.max else self.max
        if value>self.max:
            self.max=value

    def pop_front(self) -> int:
        a=self.que[0]
        self.que=self.que[1:]
        return a
