class Fibonacci:
    def __init__(self):
        pass

    def rec(self, n):
        if n <= 1:
            return n
        else:
            return self.rec(n - 1) + self.rec(n - 2)


print(Fibonacci().rec(n=12))
