# 24/05/2025
# An exponent fuction allows us to take a certain number and raise it to a certain number

def raise_to_power(base_num, pow_num):  #takes 2 numbers
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))