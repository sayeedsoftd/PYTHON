class vehicle:
    def __init__(self,model,brand,component):
        self.model=model
        self.brand=brand
        self.component=component

class plane(vehicle):
    pass

p1=plane("sayeed202","sayeed","s0 s0")
print(p1.model,p1.brand,p1.component)

class car(vehicle):
    pass
c1=car("sujoki","s3200","jhs")
print(c1.model,c1.brand,c1.component)

class bike(vehicle):
    pass
b1=car("bmw","s2100","main")
print(b1.model,b1.brand,b1.component)