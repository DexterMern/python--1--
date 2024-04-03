class DigitError(Exception):
    def __init__(self, s, massage='Error'):
        self.massage = massage
        self.s = s
        print(s)
        super().__init__(self.massage)

    def __str__(self):
        return 'DigitError'


def func(s):
    if not s.isdigit():
        raise DigitError(s, 'the string does not contain only number!')
        numbers = []
        for i in s:
            numbers.append(int(i))
        print(numbers)
DigitError('09931610436')
