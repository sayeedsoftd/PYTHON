#A regex is a sequence of character that forms a search pattern 
# RegEx can be used to check if a string contains the specified search pattern


import re
text="Bangladesh is a coruption country The prime menister is the quin of it"
x=re.findall("[a-z]",text)
print(x)
