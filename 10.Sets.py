import time

print( "\nHello World\n" )
start = time.time()

# ---------------------------------------------------------------------------------
print( "SETS :" )
# It does not repeats any item and if so, would ignore other copies
# Set items are unchangeable, meaning that we cannot change the items after the set has been created
# Unordered : Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

x = { 1 , 1 , 2 , 3 , 4 , 5 , 6 , 5 }
print(x)
print(type(x))

set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}

print("\nMETHODS IN SETS :")
# ---------------------------------------------------------------------------------

x.add(7)
print( "1. When 'ADD' function is used :" , x )
x0 = { 9 , 10 , 11 }
xlist = [ 23 , 45 ]
x.update( x0 , xlist )
print( "2. When 'UPDATE' function is used :" , x )

# Here is the difference between remove and discard
# x.remove(24) #error, since it does not exists
x.discard(23) #but discard won't raise error even if the item doesn't exists
print( "3. When 'DISCARD' function is used :" , x )
x.remove(45)
print( "4. When 'REMOVE' function is used :" , x )
x.pop()
print( "5. When 'POP' function is used :" , x )
# but sets are unordered, so it is random for which item gets removed
# "CLEAR" function removes every item from a set ( try )
# "DEL" function deleted the set raising an error of set is printed afterwards
# ---------------------------------------------------------------------------------

s0 = { 'a' , 'e', 'c' }
s1 = { 'a' , 'b' , 'c' }
print( "6. INTERSECTION :" , s0.intersection(s1) ) # can use variable instead of s0.intersection(s1)
print( "7. UNION :" , s0.union(s1) )
# ---------------------------------------------------------------------------------

# "SET" FUNCTION
# new_s0 = set( 232434234243 ) 
# print( "Integer to Set :" , new_s0 )  #ERROR

new_s1 = set( "Boy" )
print( "8. String to Set :" , new_s1 )

# new_s2 = set( True )
# print( "Bool to Set :" , new_s2 )  #ERROR

new_s3 = set( [ 12 , True , "apple"] ) #Either give an array directly or indirectly through its name
print( "9. Array to Set :" , new_s1 )

#Any datatype can be used in this way
# ---------------------------------------------------------------------------------

#ACCESSING ITEMS
print("10.")
for i in set1 :
        print( "  " , i ) #prints each item

print( "11.Is there banana in set1 ? :" , "banana" in set1 , "\n" )
# ---------------------------------------------------------------------------------

end = time.time()
print( "\nTIME TAKEN =" , (end - start) , "\n" )