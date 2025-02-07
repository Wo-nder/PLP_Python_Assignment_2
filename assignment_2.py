#creating an empty list
my_list = []

#Appending [10, 20, 30, 40]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting 15 at position 2
my_list.insert(1, 15)

# Extending my list with [50, 60, 70]
my_list.extend([50, 60, 70])
# removing the last element in my_list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

#Finding the index of 30
index_of_30 = my_list.index(30)
print(index_of_30)
