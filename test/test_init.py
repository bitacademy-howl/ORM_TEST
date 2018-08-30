class CC1:
    def __init__(self, list):
        self.list = list
    def print_list(self):
        print(self.list)


cc1 = CC1(["hi", "hello"])
cc1.print_list()
print(cc1.list)