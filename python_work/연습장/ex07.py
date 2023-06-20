class Person:
    def __init__(self):
        self.hello = '왜 안됨?.'

    def greeting(self):
        print(self.hello)

 
james = Person()
james.greeting()    # 안녕하세요
