class UserList(list['User']):
    def search(self, user_name: str) -> list['User']:
        matching_user: list['User'] = []
        for user in self:
            if user_name in user.user_name:
                matching_user.append(user)
        return matching_user

    def append(self, obj) -> None:
        self.clear()
        if not isinstance(obj, User):
            raise TypeError('this is only accepts User')
        return super().append(obj)


class User(object):
    all_users: list['User'] = UserList()

    def __init__(self, user_name: str, email: str, password: str, **kwargs) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_name!r},{self.email!r}," \
               f"{self.password!r}"


def __str__(self):
    return f"{self.user_name}"


class Order:
    pass


class Seller(User):
    def __init__(self, shaba, **kwargs) -> None:
        super().__init__(**kwargs)
        self.shaba = shaba

    def order(self, order: "Order") -> None:
        print(f"{self.user_name},From Your Products, {order} was sold!")


class Buyer(User):
    def __init__(self, phone: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.phone = phone

    def __repr__(self):
        return f"[[{self.__class__.__name__}  {self.user_name!r},{self.email!r} {self.password!r},{self.phone!r}]]"


class SellerAndBuyer(Seller, Buyer):
    def __init__(self, score, **kwargs):
        super().__init__(**kwargs)
        self.score = score


def main():
    b = Buyer(user_name='reza', email='email', password='123', phone='0993')
    s = Seller(user_name='pouya', email='p.ouyua', password='8190', phone='0938', shaba='IR1235')
    sb = SellerAndBuyer(user_name='pouya', email='p.ouyua', password='8190', phone='0938', shaba='IR1235', score=5)
    sb.order('helloo')
    # print(User.all_users)


if __name__ == "__main__":
    main()
