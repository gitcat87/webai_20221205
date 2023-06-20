class PA:
    def __init__(self):
        print("부모")

class AA(PA):

    def __init__(self):
        print("ㅇㅇㅇ")
        self.doA()

    def doA(self):
        print("doA")


a = AA()

