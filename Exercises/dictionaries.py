# 1 
# Access values in nested dictionaries (practice understanding how to locate nested keys and values)
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

# Question 1 
# 1.1 How do you access the value of the key history in the dictionary?
# Store your answer in the variable answer_1
answer1 = ...
# 1.2 How do you access the value of the key name in the dictionary?
# Store your answer in the variable answer_2
answer2 = ...


# 2 
# Check if a value exists in a dictionary
# EXAMPLE: value_exists({"name": "Karla", "age": 25, "city": "Berlin" "hobbies": ["coding", "meeting friends", "sports"]}, "Berlin") -> True
def value_exists(dict, value):
    return "TO-DO: Implement this function"


# 3
# Delete a specific key from a dictionary
# Example: delete_key({"name": "Karla", "age": 25, "city": "Berlin" "hobbies": ["coding", "meeting friends", "sports"]}, "age") -> {"name": "Karla", "city": "Berlin", "hobbies": ["coding", "meeting friends", "sports"]}
def delete_key(dict, key):
    return "TO-DO: Implement this function"


# 4
# Merge two dictionaries
# Example: merge_dictionaries({'January': 1, 'February': 2, 'March': 3}, {'March': 3, 'April': 4, 'May': 5}) -> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
def merge_dictionaries(dict1, dict2):
    return "TO-DO: Implement this function"





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


