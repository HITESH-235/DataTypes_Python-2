import time

print( "\nHello World\n" )
start = time.time()

# ---------------------------------------------------------------------------------
print( "DICTIONARIES :\n" )
# These store data values in key:value pairs.
# Its ordered, changeable, and does not allow the same item multiple times

newdict = { 
        "Name" : "Hitesh" ,
        "Age" : 16 ,
        "Language" : "Python" ,
        "Grade" : 9 ,
        "Year" : 2022 ,
        "Year" : 2022
}
print( "1. Example :" , newdict )
print( "2. Type :" , type(newdict) )

print( "3. Length of the dictionary :" , len(newdict) , "\n" )
# ---------------------------------------------------------------------------------

print( "Accessing and Changing Items :\n" )

newdict['Grade'] = 10
print( "4. Updated value for the key 'Grade' :" , newdict["Grade"] )
print( "5. GET :" , newdict.get("Year") )

keylist = newdict.keys() # Forms a list
valuelist = newdict.values()
itemlist = newdict.items()
newdict["Rank"] = 2 #Forms new item
print( "6. Keys' list :" , keylist ) # It also changes
print( "7. Values' list :" , valuelist ) 
print( "\n8. Items' list :" , itemlist ) # But as tuples as its items

if "Name" in newdict :
        newdict.update( { "Name" : "HîTESH" } )
        print( "\n9." , newdict["Name"] )
# ---------------------------------------------------------------------------------

print( "\nAdding Items :\n" )

newdict[ "Country" ] = "India"
print( "10. By Normal Method :" , newdict )
newdict.update( { "Number" : 235 } ) # if number does not exists, a new item will be formed
print( "\n11. By Update Method :" , newdict )
# ---------------------------------------------------------------------------------

print( "\nRemoving Items :\n" )

# CLEARING METHOD
# newdict.clear() # Clears the dictionary
# print( newdict ) # returns "{}"(an empty one)

newdict.pop("Country") # **pop()** always takes a single argument 
print( "12. POP :" , newdict )

newdict.popitem() # **popitem()** doesn't takes any argument, it just removes the last item
print( "\n13. POPITEM :" , newdict )

del newdict["Rank"]
print( "\n14. DEL :" , newdict )

print( "15. GET :" , newdict.get( "Rank" , 1 ) ) 
# if the key is present, then its own value would be returned
# but if it is not present, it will return the specified value like above
# and in case its not present, the neither the dict gets any item added
# you may give just 1 argument if the key exists 
print( "\n16. FINAL :" , newdict )
# ---------------------------------------------------------------------------------

end = time.time()
print( "\nTIME TAKEN  =" , (end - start) , "\n" )