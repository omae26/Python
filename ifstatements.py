# 24/04/2025
# If statements help programs to make decisions based on conditions
# Example: Boolean

is_male = True
if is_male: 
    print("You are a male")
else:
    print("You are not a male")
    print("You are not a male") 
#if statements help programs to make decisions based on conditions

sunday = True
if sunday:
    print("I'll go to church")
else:
    print("I'll go to school")

is_male = True
is_tall = False
# If both are true, it will print 'You are a tall male'
# If is_male is false, it will print 'You are not a male but tall'
# If is_male is true, and is_tall false ,it will print 'You are a short male'
# If both are false, it will print 'You are not male and not tall'

# 29/04/2025
# OR operator 
if is_male or is_tall:
    print("You are male or tall or both ")
else:
    print("You are neither male or tall")

# AND operator. It works when both conditions are true    
is_male = True
is_tall = True
# OR operator 
if is_male or is_tall:
    print("You are a tall male ")

# Adding another condition using else if (elif)
# To check if they are male but not tall
elif is_male and not(is_tall): # not function negates what comes after it
    print("You are a short male")
# Another condition to check if they are not male but tall
elif not(is_male) and (is_tall): # not function negates what comes after it
    print("You are not a male but tall")
else:
    print("You are not male and not tall ")