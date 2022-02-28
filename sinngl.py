class app1:
    def show1(self):
        print("show1")

class app2(app1):
    def show2(self):
        print("show2")


obj=app2()
obj.show1()
obj.show2()
