num=[1,2,3,4,5,6,7,8]
double=[i*3 for  i in num]
# list comprehension mens double,tripl...... the list value 
print(double)

# list comprehension use loop 
for i in num:
    j=i%2
    print(j)