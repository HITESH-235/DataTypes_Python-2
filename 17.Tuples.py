from time import*

print( "\nHello World\n" )
start = time()


# TUPLES
# ordered . unchangeable , allow repitation of any item
tpl = ( "apple" , "banana" , "cherry" , "mango" )
print(tpl)
print( len(tpl) )
print( type(tpl))

tpl_1items = ( "mango" , )
# in a tuple with one item, remember to put comma at last
print( type(tpl_1items) )

tuple1 =  ( "apple" , "banana" , "cherry" )
tuple2 = ( 1 , 5 , 7 , 9 , 3 )
tuple3 = ( True , False , False )

# TUPLE CONSTRUCTOR
constructed_tuple = tuple(( "apple" , 1 , 2 , True , "string" )) #but use double brackets
print( constructed_tuple )

print( tuple[1] ) # can try all slicing methods
# negative indexing can also be used

# For modifying a tuple, you can convert it to a list and then again turn to tuple when modified
# all methods in list do not works in tuples
list1 = list(tuple1)
list1[0] = "apple_x"
del list1[-1] # use any list method
tuple1 = tuple(list1)
print ( tuple1 ) 

# But some methods are there
orange1 = ( "orange" , )
tuple1 += orange1
print( tuple1 )
# and :
del tuple1 # that's it

( red , yellow , orange ) = ( "apple" , "banana" , "orange" )
print(red)
print(yellow)
print(orange)

# LOOPING is same as lists and dictionaries

# Joining two tuples
tuple1 = tuple2 + tuple3
print(tuple1)

tuple1 = tuple2 * 3
print(tuple1)

# INDEX and COUNT also works in tuples
# ---------------------------------------------------------------------------------

end = time()
print( "\nTIME TAKEN  =" , end - start , "\n" )
