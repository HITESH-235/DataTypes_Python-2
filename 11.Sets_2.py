print( "\nHello World\n" )


print( "BONUS FUNCTIONS AND METHODS :\n" )
st1 = { 1 , 2 , 3 , 5 , 7 , 8 , 9 }
st2 = { 1 , 2 , 4 , 5 , 6 , 8 , 9 , 10 }
st3 = { 1 , 2 , 5 }

dummy = st1.copy()
print( "A. COPY() :" , dummy )

print( "B. DIFFERENCE() (b/w st1 & st2) :" , st1.difference(st2) )

dummy0 = st1.copy()
dummy.add( 72 )
dummy0.difference_update(dummy) # switches all items of dummy0 with the items that **dummy0 has but dummy doesn't**
print( "C. DIFFERENCE_UPDATE() :" , st1 ) # since dummy0 has nothing more than dummy, so dummy0 is now empty, but -
dummy1 = st1.copy()
dummy.difference_update(dummy1) # situation reversed, now we know that dummy has 72 more than dummy1
print( "                        " , dummy )

 # ***INTERSECTION_UPDATE()*** does the same as above but with similarities b/w two sets
print( "D. ISDISJOINT() :" , st1.isdisjoint(st2) ) # false if st2 has any intersections with st1
print( "E. ISSUBSET() :" , st3.issubset(st1) )
print( "F. SYMMETRIC_DIFFERENCE :" , st1.symmetric_difference( st2 ) , "\n" ) # gives all different element which don't intersects
# try "SYMMETRIC_DIFFERENCE_UPDATE()" in the same way as other updates suffixes functions