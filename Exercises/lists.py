# 1
# Sort a list in ascending order
# Example: sort_ascending([3, 2, 5, 4, 2]) -> [1, 2, 3, 4, 5]
def sort_ascending(list_of_numbers):
  return "TO-DO: Implement this function"


# 2
# Sort a list by length of the strings
# Example: sort_by_length(["Hello", "Redi", "!"]) -> ["!", "Redi", "Hello"]
def sort_by_length(list_of_strings):
  return "TO-DO: Implement this function"


# 3
# Square each number in a list of numbers
# Example: square_numbers([1, 2, 3, 4, 5]) -> [1, 4, 9, 16, 25]
def square_numbers(list_of_numbers):
  return "TO-DO: Implement this function"


# 4
# Remove empty strings from a list of strings
# Example: remove_empty_strings(["", "Hello", "", "World", "!"]) -> ["Hello", "World", "!"]
def remove_empty_strings(list_of_strings):
  return "TO-DO: Implement this function"


# 5
# Filter a list of numbers to only those that are divisible by 5
# Example: numbers_divisible_by_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> [5, 10]
def numbers_divisible_by_five(lsit_of_numbers):
  return "TO-DO: Implement this function"


# --------------------------------------------------
# Do not touch these Lines  
# To run the tests, run this file either with the play button in the top right corner or by typing "python3 lists.py" in the terminal.
test = sort_ascending([3, 1, 5, 4, 2])
print(("Passed ✅" if test == [1, 2, 3, 4, 5] else "Failed ❌") + " Test 1 (sort_ascending)")

test = sort_by_length(["Hello", "Redi", "!"])
print(("Passed ✅" if test == ["!", "Redi", "Hello"] else "Failed ❌") + " Test 2 (sort_by_length)")

test = square_numbers([1, 2, 3, 4, 5])
print(("Passed ✅" if test == [1, 4, 9, 16, 25] else "Failed ❌") + " Test 3 (square_numbers)")

test = remove_empty_strings(["", "Hello", "", "World", "!"])
print(("Passed ✅" if test == ["Hello", "World", "!"] else "Failed ❌") + " Test 4 (remove_empty_strings)")

test = numbers_divisible_by_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(("Passed ✅" if test == [5, 10] else "Failed ❌") + " Test 5 (numbers_divisible_by_five)")