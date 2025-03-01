# python program to add two value in a key of a dictionary
my_dcit = {"a":["ranjan"],"b":["sakshi"]}
my_dcit["a"].append("singh")
print(my_dcit)
# what if i want add two key in one value
# no you vcan't do that
# i am performing pr request and codde will be visible in the pycharm

#replace old word with new word
my_string = "ranjan singh is my name and i live in bhagalpur"
old_word = "singh"
new_word = "kumar"
empty_string = ""
for item in my_string.split():
    if item == old_word:
        empty_string = empty_string +" "+ new_word
    else:
        empty_string =empty_string +" " + item
print(empty_string)
print(my_string)

# printng occurrence of number in the given list
my_list = [2,3,4,5,3,4,2,7,6,8,9,6,7,4]
empty_dict = {}
for obj in my_list:
    if obj in empty_dict:
        empty_dict[obj] += 1
    else:
        empty_dict[obj] = 1
print(empty_dict)