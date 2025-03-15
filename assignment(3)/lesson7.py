# The Set Data Type:

#The set is unordered

my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add (6)
print(my_set)
my_set.remove(3)
print(my_set)
 
#The set is Unchangeable

my_set: set = {1, 2, 3, 4, 5,6}
print(my_set)

#Unique Elements:
# List with duplicate elements
elements = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# Convert to a set to remove duplicates
unique_elements = set(elements)
print("Unique elements:", unique_elements)

#Discard Method:
my_set = {1, 2, 3, 4, 5}

# Remove an existing element
my_set.discard(3)
print("After discarding 3:", my_set)  
# Try to discard a non-existent element
my_set.discard(10)  
print("After discarding 10:", my_set)  

#Remove Method:
my_set = {1, 2, 3, 4, 5}

# Remove an existing element
my_set.remove(3)
print("After removing 3:", my_set)  

# Try to remove a non-existent element
try:
    my_set.remove(10)  
except KeyError as e:
    print("Error:", e)  

# Frozen set
my_set = frozenset([1, 2, 3, 4, 5])


# Example operations
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# Union
print(fs1 | fs2)  

# Intersection
print(fs1 & fs2)  

# Difference
print(fs1 - fs2)  

# Symmetric Difference
print(fs1 ^ fs2)  

# Membership Testing
print(2 in fs1) 

# garbeg collection:

import gc
gc.collect()  
print(gc.get_count())