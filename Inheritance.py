class father:
    homr="duplex"
    deposite=1000000
    car="audi"
    position="political power "
class youngerFather(father):
    brokenhome=""
    broken=""

k=youngerFather()
print(k.car)

#MULTIPLE INHERITANCE
class firstson:
   homr="duplex"
   deposite=1000000
   car="audi"
   position="political power "

class secondson:
    camera="DSLR"
    gr="2"

class thirdson:
    land="50 viga"
    flat="5"
    tk=1232476

class fourson(firstson,secondson,thirdson):
    loan=""


u=fourson()
print(u.camera)


