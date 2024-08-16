my_dict={"kit": "1photo1", "cat": "1scratch1", "fox": "1look1"}
print("Dict:",my_dict)
print("Existing value:",my_dict["kit"])
print("Not existing value:", my_dict.get("dog"))
my_dict.update({"neko": "1seen1", "fish": "1caught1"})
data_pop = my_dict.pop("kit")
print("Deleted value:",data_pop)
print("Modified dictionary:",my_dict)

#next, part 3

my_set={1,1,2,2,True, True, "Hi","Hi"}
print("Set:",my_set)
my_set.update({"perfect"}, {7})
my_set.remove(1)
print("Modified set:",my_set)
