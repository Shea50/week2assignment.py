my_list=[]
print("before Append:", my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("after Append:", my_list)

my_list.insert(2,15)
print(my_list)

list2=[50, 60, 70]
my_list.extend(list2)

print("List after extend:", my_list)

my_list.remove(70)
print(my_list)

my_list.sort()
print(my_list)

x=my_list.index(30)
print(x)