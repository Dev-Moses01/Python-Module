my_list = [1,2,3,4,5]
my_tuple = ("Moses", "Mose", "Mos", "Mo", "M")
print(my_list)
print(my_tuple)
print(my_tuple[2:])
print(my_tuple[:1])

set1 = {1,2,3,4,5}
set2 = {2,4,6,8,10}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

#After class project
my_list = list(my_tuple)
print("Tuple: ", my_tuple)
print("List: ", my_list)
print(my_list.pop())