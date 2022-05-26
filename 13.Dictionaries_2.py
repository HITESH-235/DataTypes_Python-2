import time

print( "\nHello World\n" )
start = time.time()

x = {
        "key_1" : "value_1" ,
        "key_2" : "value_2" ,
        "key_3" : "value_3" ,
        "key_4" : "value_4"
}
print( "A. LOOPS :\n")
# ---------------------------------------------------------------------------------
print( "1. All Keys :" )
for i in x :
        print(i)
# ---------------------------------------------------------------------------------
print( "1.1. All Keys Method-2 :" ) 
for i in x.keys() :
        print(i)
# ---------------------------------------------------------------------------------
print( "\n2. All Values :" )
for i in x :
        print( x[i] )
# ---------------------------------------------------------------------------------
print( "2.1. All Values Method-2 :" ) 
for i in x.values() :
        print(i)
# ---------------------------------------------------------------------------------
print( "\n3. All Items :" )
for i in x.items() :
        print(i)
# ---------------------------------------------------------------------------------
print( "3.1. All Items Method-2 :" ) 
for i , j in x.items() :
        print( i , ":" , j )
# ---------------------------------------------------------------------------------

print( "\nB. COPIED :\n")

y = x.copy()
print( "1. COPY :" , y )

z = dict(x)
print( "2. Using DICT :" , z )
# ---------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------

end = time.time()
print( "\nTIME TAKEN  =" , end - start , "\n" )