from time import*

print( "\nHello World\n")
start = time()

x = [ "apple" , "banana" , "mango" ]
print( '1. All Items In The List :' )
for i in x :
        print(i)
# ---------------------------------------------------------------------------------

length = len(x)
print( '\n2. All Items In The List #2 :' )
for i in range( length ) :
        print( x[i])
# ---------------------------------------------------------------------------------

print( "\n3. Using ENUMERATE :" )
a = enumerate(x) 
print(a)
for i in a :
        print(i)

for i,j in enumerate(x) :  # don't use a variable instead of enumerate(x) while using double iterators
        print( f"{i} : {j}" )  # will print with indexes

for i , j in enumerate( x , 100 ) :  # will start index from 100
        print( f"{i} : {j}")        
# ---------------------------------------------------------------------------------

print( "\n4. While Loops :" )

i = 0
while i < length :
        print( x[i] )
        i+=1
# ---------------------------------------------------------------------------------
end = time()
print( "\nTIME TAKEN  =" , end - start , "\n" )