from time import*

print( "\nHello World\n" )
start = time()

print( "LISTS :\n" )
# List items are ordered, changeable, and allow duplicate values
# List items are indexed
lst = [ "apple" , 2 , "banana" , 4 , "mango" , 6 , True , False ]
print( "1. Example :" , lst )
print( "2. Length :" , len(lst) )
print( "3. Type :" , type(lst) )

x = list( ( "apple" , "banana" , "cherry" ) ) # always use double small brackets while constructing 
print( "4. Constructed List :" , x )
# ---------------------------------------------------------------------------------

print( "\nAccesing List Items :\n" )

print( "5. 3rd item of lst :" , lst[2] )
print( "6. 2nd last item of lst :" , lst[-2] ) # -1 refers to last item, -2 refers to 2nd last item.....
# allows slicing too
print( "7. 2nd to 5th item :" , lst[ 2 : 6 ]) # you may try all slicing methods
# ---------------------------------------------------------------------------------

print( "\nChanging List Items :\n" )

x[0] = "apple2"
x[ 1 : ] = [ "banana2" , "cherry2" ] # try other slice methods too
print( "8. Changed x :" , x )

# ---------------------------------------------------------------------------------

print( "\nAdding List Items :\n" )

# Inserting :
x.insert( 2 , "watermelon") # pushes the item without removing any existing one
print( "9. Insert :" , x )

# Appending :
x.append( "orange" )
print( "10. Append :" , x)
# Extending : 
x.extend(lst) # the item to be added can be of an data type (e.g. string, sets, booleans, dictionaries, number, tuple etc) 
                        # Integer not allowed
                        # in case of dictionaries, only keys are added from items
print( "11. Extend :" , x )
# ---------------------------------------------------------------------------------

print( "\nRemove List Items :\n" )

x.remove(True)
print( "12. True Removed :\n" , x )
x.pop()
print( "13. Just Popped :\n" , x )
x.pop(4) 
print( "14. Orange popped specifically :\n" , x)
del x[2] #deleted specifically
print( "15. Watermelon deleted specifically :\n" , x )

# del x # x eradicated
# print(x) # ERROR

x.clear() # x emptied
print( "16. x cleared :" , x )
# ---------------------------------------------------------------------------------


end = time()
print( "\nTIME TAKEN  =" , end - start , "\n" ) 