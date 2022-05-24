print( "\nHello World\n" )

# ---------------------------------------------------------------------------------
print( "SETS :" )
# It does not repeats any item and if so, would ignore other copies
# Set items are unchangeable, meaning that we cannot change the items after the set has been created
# Unordered : Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# **SLICING** CAN ALSO BE USED IN THIS TYPE TOO

x = { 1 , 1 , 2 , 3 , 4 , 5 , 6 , 5 }
print(x)
print(type(X))

# set1 = {"apple", "banana", "cherry"}
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
# x.remove(24) #error
x.discard(23)
print( "3. When 'DISCARD' function is used :" , x )
x.remove(45)
print( "4. When 'REMOVE' function is used :" , x )
# ---------------------------------------------------------------------------------
s1 = { 'a' , 'e', 'c' }
s2 = { 'a' , 'b' , 'c' }
print( "5. INTERSECTION :" , s1.intersection(s2) )
print( "6. UNION :" , s1.union(s2) )