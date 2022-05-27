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

print( "\nB. COPIES :\n")

y = x.copy()
print( "1. COPY :" , y )

z = dict(x)
print( "2. Using DICT :" , z )
# ---------------------------------------------------------------------------------

print( "\nC. NESTED DICTIONARIES :\n")

dictx = {
        "dict1" : { 
                "key_11" : "value_11" ,
                "key_12" : "value_12" ,
                "key_13" : "value_13"
        } ,
        "dict2" : {
                "key_21" : "value_11" ,
                "key_22" : "value_12" ,
                "key_23" : "value_23" 
        } ,
        "dict3" : {
                "key_31" : "value_31" ,
                "key_32" : "value_32" ,
                "key_33" : "value_33" 
        }
}
print( "1." , dictx )
print( "\n   A. dict 1st, value 3rd :" , ( dictx["dict1"] )["key_13"] )
print( "\n   B. dict 3rd, value 2nd :" , ( dictx["dict3"] )["key_32"] )

a = dictx["dict2"].keys()
j = 0
for i in a :
        if j == 1 :
                b = i
        j+=1
print( "\n   C. dict 2nd, key 2nd :" , b )
# ---------------------------------------------------------------------------------

dict1 = { 
        "key_11" : "value_11" ,
        "key_12" : "value_12" ,
        "key_13" : "value_13"
}
dict2 = {
        "key_21" : "value_21" ,
        "key_22" : "value_22" ,
        "key_23" : "value_23" 
}
dict3 = {
        "key_31" : "value_31" ,
        "key_32" : "value_32" ,
        "key_33" : "value_33" 
}

dicty = {
        "dict1" : dict1 ,
        "dict2" : dict2 ,
        "dict3" : dict3
}

print( "\n2." , dicty )
# ---------------------------------------------------------------------------------

end = time.time()
print( "\nTIME TAKEN  =" , end - start , "\n" )