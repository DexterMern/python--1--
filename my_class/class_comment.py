from datetime import datetime
from pprint import pprint
from time import sleep


# Instance Method
# Class Method
# Static Method
class Product:
    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self):
        return self.product_name


class Comment:
    website_name = 'www.learnable.ir'

    # Instance Method
    def __init__(self, product, name, description, like_count, dislike_count):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like_count = like_count
        self.dislike_count = dislike_count

    # Instance Method
    def show(self):
        pprint(f'product: {self.product}\n'
               f'name: {self.name}\n'
               f'description: {self.description}\n'
               f'date: {self.date}\n'
               f'like: {self.like_count} and dislike: {self.dislike_count}')

    @classmethod
    def info(cls):
        print(f'website name : {cls.website_name}')

    @classmethod
    def censorship(cls, product, name, description, like_count, dislike_count):
        print('this comment was censored!!!')
        sc = description.replace('bad', '*****')
        return cls(product, name, sc, like_count, dislike_count)

    @staticmethod
    def elapsed_time(time):
        sleep(3)
        print(datetime.now() - time)


python_course = Product('python expert', 0, 0)
c1 = Comment(python_course, 'poultry', 'good course!', 50, 10)
c1.show()
print('-' * 40)
Comment.info()
print('-' * 40)
c2 = Comment.censorship(python_course, 'reza', 'this is bad course', 50, 10)
c2.show()
print('-' * 40)
Comment.elapsed_time(c2.date)
print('-' * 40)
