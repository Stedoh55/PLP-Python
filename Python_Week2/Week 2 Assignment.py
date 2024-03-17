my_list = []
new = 10, 20,30, 40
for i in new: 
    my_list.append(i)
my_list.insert(1, 15)
other = [50, 60, 70]
my_list.extend(other)
my_list.pop()
sorting = sorted(my_list)

print(my_list.index(30))

