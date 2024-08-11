# Dictionaries are used to store data values in key : value pairs 
# Dictionaries is a collection which is ordered changable and do not allow duplicate
stuinfo={
    "Kamal":{
        "location":"comilla",
        "study":"Honourse",
        "subject":"CSE",
        "roll":210088,
        "number":+8801762525468
    },
    "sayeed":{
        "location":"Dhaka",
        "study":"Honourse",
        "subject":"CSE",
        "roll":210089,
        "number":+8801849355949
    },
    "year":2002
}
print(stuinfo)
print(stuinfo["sayeed"])#specific data 
print(stuinfo["sayeed"]["number"])
x=stuinfo.keys()# saw key data 
print(x)
stuinfo["year"]=2000 # change value 
#stuinfo.update({"sayeed":"sayeed is an cse student "})
#stuinfo.pop("year") # remove key(year)

# loop dictionaryes
for i in stuinfo:
    print(i)
for j in stuinfo.values(): # print all values 
        print(j)
