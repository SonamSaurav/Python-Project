# THIS IS FOR ARRAY 1 PRACTICAL

import array as arr

arr1 = [5,10,20,8,40,55,12]

print(arr1)

# PRINT ELEMENT BY INDEXING NUMBER
print(arr1[4])

# LENGTH OF ARRAY
print(len(arr1))

# APPEND IS USE TO ADD THE ELEMENT AT THE END OF ARRAY  

arr1.append(3)
print(arr1)

# EXTEND IS USE TO ADD 
B=[16,9,7,24,40,15]
arr1.extend(B)
print(arr1)

# INSERT IS USE TO ADD AN ELEMENTS AT ANY POSITION OF ARRAY
arr1.insert(2,19)
print(arr1)
# SHORTING THE ELEMENT 
arr1.sort()
print(arr1)
# POP IS USE TO DELETE THE ELEMENT BY INDEX NUMBER 
# BY DEFAULT POP FUNCTION DELETES THE ELEMENT OF THE LAST INDEX NUMBER 
arr1.pop(7)
print(arr1)
# REMOVE IS USE TO DELETE THE ELEMENT BY NAME OR BY VALUE
arr1.remove(12)
print(arr1)

c=[11, 20, 22,24]
# LOOPS IN ARRAY
b=c[0]
while b<= c[2]:
    print(b)
    b = b+1

