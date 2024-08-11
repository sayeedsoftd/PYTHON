# Read file
readtext=open("text.txt","r")
print(readtext.read())

# Write file
w=open("text1.html","w")
w.write("<p> subscribe sayeed programmer</p>")

# append file (use write multiple line)
w=open("text1.html","a\n")
w.write(" <p> subscribe sayeed programmer</p>")