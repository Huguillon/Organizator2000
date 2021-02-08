
# ------------------------------------- LISTS -------------------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3, "a"]

list3 = list1 + list2
print(list3)

print("b" in list1)
# OUTPUT
# ['a', 'b', 'c', 1, 2, 3, 'a']

list2.insert(0, "caca")
print(list2)

# # ------------------------------------- SETS -------------------------------------
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3, "a"}
#
# set3 = set1.union(set2)
# print(set3)
#
# # OUTPUT
# # {'c', 1, 2, 3, 'b', 'a'}

# # ------------------------------------- TUPLETS -------------------------------------
# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3, "a")
#
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# # OUTPUT
# # ('a', 'b', 'c', 1, 2, 3, 'a')