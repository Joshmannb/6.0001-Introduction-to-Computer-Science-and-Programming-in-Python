
class test(object):
    def __init__(self, x):
        self.x = x

    def say(self):
        print(self.x)

class b(test):
    pass

c = b(5)
c.say()