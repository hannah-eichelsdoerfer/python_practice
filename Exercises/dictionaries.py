# 1 
# Access values in nested dictionaries
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# understand how to locate nested keys
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# Question 1 
# 1.1 How do you access the value of the key history in the dictionary?
# Store your answer in the variable answer_1
answer1 = sampleDict['class']['student']['marks']['history']
# 1.2 How do you access the value of the key name in the dictionary?
# Store your answer in the variable answer_2
answer2 = sampleDict['class']['student']['name']


# 2 
# Check if a value exists in a dictionary
# EXAMPLE: value_exists({"name": "Karla", "age": 25, "city": "Berlin" "hobbies": ["coding", "meeting friends", "sports"]}, "Berlin") -> True
def value_exists(dict, value):
    return value in dict.values()


# 3
# Delete a specific key from a dictionary
# Example: delete_key({"name": "Karla", "age": 25, "city": "Berlin" "hobbies": ["coding", "meeting friends", "sports"]}, "age") -> {"name": "Karla", "city": "Berlin", "hobbies": ["coding", "meeting friends", "sports"]}
def delete_key(dict, key):
    del dict[key]
    return dict


# 4
# Merge two dictionaries
# Example: merge_dictionaries({'January': 1, 'February': 2, 'March': 3}, {'March': 3, 'April': 4, 'May': 5}) -> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries into one."""
    # dict3 = dict1.copy()
    # dict3.update(dict2)
    # return dict3
    return {**dict1, **dict2}





# --------------------------------------------------
# Do not touch these Lines  
test_dictionary = { "name": "Karla", "age": 25, "city": "Berlin", "hobbies": ["coding", "meeting friends", "sports"]}

print(("Passed ✅" if answer1 == sampleDict['class']['student']['marks']['history'] else "Failed ❌") + " Test 1.1 (Path to value that's stored in history key)")
print(("Passed ✅" if answer2 == sampleDict['class']['student']['name'] else "Failed ❌") + " Test 1.2 (Path to value that's stored in name key)")

test = value_exists(test_dictionary, "Berlin")
print(("Passed ✅" if test == True else "Failed ❌") + " Test 2 (value_exists)")

test = delete_key(test_dictionary, 'age')
print(("Passed ✅" if test == {'name': 'Karla', 'city': 'Berlin', "hobbies": ["coding", "meeting friends", "sports"]} else "Failed ❌") + " Test 3 (delete_key)")

test = merge_dictionaries({'January': 1, 'February': 2, 'March': 3}, {'March': 3, 'April': 4, 'May': 5})
print(("Passed ✅" if test == {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5} else "Failed ❌") + " Test 4 (merge_dictionaries)")


