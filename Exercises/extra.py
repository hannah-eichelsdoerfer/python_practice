# Step 1: Create a function called `allowed_to_vote` that takes in a `age` as an argument
# TODO: return (not print!) a boolean stating whether `age` is old enough to vote (18+)
# NOTE: Use an if/else statment

def allowed_to_vote(age):
  if age >= 18:
    return True
  else:
    return False

# Step 2: Ask the user for their age
age = int(input("How old are you? "))

# Step 3: Call the function with the age they entered
check = allowed_to_vote(age)

# Depending on the restult, print out whether they are allowed to vote or not
print("You are allowed to vote!" if check == True else "You are not allowed to vote!")