from pprint import pprint


class BaseClass:
    num_base_calls = 0

    def __init__(self, b, c, **kwargs):
        super().__init__(**kwargs)
        self.num_Left_calls_calls = None
        self.c = c
        self.b = b

    def call_me(self):
        print('calling method on base class!')
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_Left_calls = 0

    def __init__(self, f, a, **kwargs):
        super().__init__(**kwargs)
        self.num_Left_calls_calls = None
        self.f = f
        self.a = a

    def call_me(self):
        # baseclass.callme(self)
        super().call_me()
        print('calling method on LeftSubClass!')
        self.num_Left_calls_calls += 1


class RightSubClass(BaseClass):
    num_Right_calls = 0

    def __init__(self, d, e, **kwargs):
        super().__init__(**kwargs)
        self.num_Right_calls_calls = None
        self.d = d
        self.e = e

    def call_me(self):
        # baseclass.callme(self)
        super().call_me()
        print('calling method on RightSubClass!')
        self.num_Right_calls_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_Sub_calls = 0

    def __init__(self, g, **kwargs):
        super().__init__(**kwargs)
        self.g = g

    def call_me(self):
        # LeftSubClass.callme(self)
        # RightSubClass.callme(self)
        super().call_me()
        print('calling method on SubClass!')
        self.num_Sub_calls += 1


s = SubClass(g=5, d=6, e=4, f=9, a=1, b=2, c=3)
print(s.num_Sub_calls, s.num_Left_calls, s.num_Right_calls, s.num_base_calls)
pprint([s.a, s.b, s.c, s.d, s.e, s.f, s.g])
