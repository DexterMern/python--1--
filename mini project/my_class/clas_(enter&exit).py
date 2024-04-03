# class C:
#     def __enter__(self):
#         print('start!')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('End!')
#
#
# with C() as c:
#     print(40 * '-')
#     print(c.__class__)
#     print('reza')
#     print(40 * '-')


# ....................................
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('this file was opened!')
        self.file = open(self.filename, self.mode)
        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('this file was closed!')
        self.file.close()


with FileManager('text.txt', 'w') as s:
    s.write('hello!')
