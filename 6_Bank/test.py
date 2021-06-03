class ZeroException(Exception):
    pass


def div(a,b):
    if b !=0:
        return a/b
    else:
        raise ZeroException("Errrororr")



try:
    result = div(1,0)
except ZeroException as err:
    print(err)
    result = 0

print(result)


print("------")


#attribut de classe
class CarFactory:
    last_id = 0

    def __init__(self):
        pass
        1
        #self.last_id = 0

    def sell(self):
        CarFactory.last_id += 1

a = CarFactory()
b = CarFactory()


