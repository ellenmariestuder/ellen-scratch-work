class Singleton:
    _instances = {}     # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

class AClass(Singleton):
    def __init__(self):
        print("complex ops that take a long time")


obj1 = AClass()
obj2 = AClass()
obj3 = AClass()
obj4 = AClass()



# right now, if you run this script it currently prints out
# all 4 object print statements. however, what it _should_ 
# do is print out only one (once/ because we inherit the
# singleton class). why doesn't it work?