from time import*

print( "\nHello World\n" )
start = time()

print( "LIST COMPREHENSION :" )
# Syntax :
# newlist = [ *expression* for *item* in *iterable* if *condition* == *True*]
# true means that it is available when the condition is true
# item is like the i used before

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#         if "a" in x:
#                 newlist.append(x)
# print(newlist)

#  alternative for above :
newlist = [ i for i in fruits if "a" in i ]
# puts the new element if a letter is in it
print(newlist)

newlist = [ i for i in fruits if i != "apple" ] # can't be pushed, only replaces every item with new element
print(newlist)

newlist = [ x if x != "banana" else "orange" for x in fruits ]
# "Return the item if it is not banana, if it is banana return orange".
# the difference here is that condition is written before loop if has multiple conditional statements 
print(newlist)
#  you can try many things with this shorthand
# ---------------------------------------------------------------------------------

print( "\n2. Sort List Alphabetically" )
fruits.sort()
print( fruits )
# Sometimes it puts strings with first capital letter before than small letters

print( "\n3. Sort List Numerically" )
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# any function can be put like : list.sort( key = function )
# if the func returns a number then it would be according to the value of items, like :
def myfunc(n):
        return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# functions can be replaced by methods too like "key = str.lower" makes every item small before sorting
# ---------------------------------------------------------------------------------
print("\n4. Extend :")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
# ---------------------------------------------------------------------------------
print("\nCounting An Item :")
list3 = [ 1 , 1 , 1 , 1 ]
print( list3.count(1) )
# ---------------------------------------------------------------------------------

end = time()
print( "\nTIME TAKEN  =" , end - start , "\n" )