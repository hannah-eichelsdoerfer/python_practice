# 1
# Convert a string to upper case
# Example: upper_case("Hello, World!") -> "HELLO, WORLD!"
def upper_case(str):
  return "TO-DO: Implement this function"
  

# 2
# Remove all whitespace around a string
# Example: remove_whitespace("  Hello, World!  ") -> "Hello, World!"
def remove_whitespace(str):
  return "TO-DO: Implement this function"


# 3
# Remove all special characters from a string (advanced: keep whitespace)
# Example: remove_special_characters("@Hello- /Everyone\") -> "HelloEveryone" (advanced: "Hello Everyone")
# Example: remove_special_characters("-Redi School of \Digital @Integration") -> "Redi School of Digital Integration"
# Advanced: Make it robust and get any 
def remove_special_characters(string_to_clean):
  return "TO-DO: Implement this function"


# 4
# Check if a string belongs to a word (advanced: make case insensitive)
# Example: belongs_to("Hello, World!", "Hello") -> True
def belongs_to(str, word):
  return "TO-DO: Implement this function"


# 5
# Count the number of occurrences of each character in a string 
# return a dictionairy with key as the character and its value as its frequency in the given string
# Example: count_character_occurrences("Banana") -> {"B": 1, "a": 3, "n": 2}
def count_character_occurrences(str):
  return "TO-DO: Implement this function"


# --------------------------------------------------
# Do not touch these Lines  
test = upper_case("Hello World")
print(("Passed ✅" if test == "HELLO WORLD" else " Failed ❌") + " Test 1 (upper_case)")

test = remove_whitespace(" Hello World   ")
print(("Passed ✅" if test == "Hello World" else " Failed ❌") + " Test 2 (remove_whitespace)")

test = remove_special_characters("@Hello- /Everyone!")
print(("Passed ✅" if test == "HelloEveryone" else " Failed ❌") + " Test 3 (remove_special_characters)")

test =  belongs_to("Hello, World!", "World")
print(("Passed ✅" if test == True else " Failed ❌") + " Test 4 (belongs_to)")

test = count_character_occurrences("Banana")
print(("Passed ✅" if test == {"B": 1, "a": 3, "n": 2} else " Failed ❌") + " Test 5 (count_character_occurrences)")