class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rec1 = Rectangle(10, 20)
for item in rec1:
    print(item)

'''
O/P:
{'length': 10}
{'width': 20}
'''
