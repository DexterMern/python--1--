lst1 = [1, 2, 3, 45, 6, 5, 8]


class NewList(list):
    @property
    def avg(self):
        return sum(self) / len(self)


lst2 = NewList((1, 2, 3, 4, 5, 6))

print(lst1)
print(lst2)
print(lst2.avg)
