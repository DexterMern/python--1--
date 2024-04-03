class PowTwo:
    def __init__(self, max_pow):
        self.n = 0
        self.max_pow = max_pow

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max_pow:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration


n = PowTwo(5)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(40 * '*')
n1 = iter(n)
for i in n1:
    print(i)
