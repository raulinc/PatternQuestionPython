#Pattern 1
print("Pattern 1")
print()
for row in range(6):
    for col in range(5):
        print("*",end=" ")
    print()

print()

#Pattern 2

'''
*
* *
* * *
* * * *
'''

print("Pattern 2")
print()
for row in range(6):
    for col in range(row+1):
        print("*",end=' ')
    print()

print()
print("Pattern 3")
print()
for row in range(6):
    for col in range(6-row):
        print("*",end=' ')
    print()



print()
print("Pattern 3")
print()
for row in range(1,7):
    for col in range(1,row):
        print(col,end=' ')
    print()

print()
print('Pattern 5')
print()
for row in range(5):
    for col in range(row):
        print("*",end=" ")
    print()
for row in range(5):
    for col in range(5-row):
        print("*",end=" ")
    print()


print()
print('Pattern 6')
print()
for row in range(6):
    for col in range(6-row):
        print(" ",end="")
    for col in range(row):
        print("*",end="")
    print()

print()
print('Pattern 7')
print()
for row in range(6):
    for col in range(row):
        print(" ",end="")
    for col in range(6-row):
        print("*",end="")
    print()

print()
print('Pattern 10')
print()
for row in range(6):
    for col in range(6-row):
        print(" ",end="")
    for col in range(row):
        print("*",end=" ")
    print()


print()
print('Pattern 11')
print()
for row in range(6):
    for col in range(row):
        print(" ",end="")
    for col in range(6-row):
        print("*",end=" ")
    
    print()


print()
print('Pattern 12')
print()

for row in range(6):
    for col in range(row):
        print(" ",end="")
    for col in range(6-row):
        print("*",end=" ")
    if row==5:
        break 
    print()
for row in range(6):
    for col in range(6-row):
        print(" ",end="")
    for col in range(row):
        print("*",end=" ")
    print()


