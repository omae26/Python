# for loop
# 23.05.2025

for letter in "Giraffe Academy" : # For every letter in giraffe academy...
    print(letter) # It will print out all letters in giraffe academy,a different one each time

# Looping through as array
friends = ["Jim", "Karen", "Kevin"]
print(len(friends))  # Length of the array
for friend in friends:
    print(friend)

# Looping through a series of numbers
for index in range(10):
    print(index)

for index in range(3,10):
    print(index)

friends = ["Ann", "Dave", "Ted"]
len(friends)
for index in range(len(friends)):
    print(friends[index])
    # friends 0.1.2 indices

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")