class Asker:
    @staticmethod
    def askall(args):
        for r in args:
            r.report()
class Sender:
    fst = True
    @classmethod
    def report(cls):
        if cls.fst:
            print("Greetings!!!")
        else:
            print("Get away!!!!!")
        cls.fst = False

s = Sender()
print(s.report())
print(s.report())
print(s.report())
a = Asker()
print(a.askall([Sender() for i in range(10)]))