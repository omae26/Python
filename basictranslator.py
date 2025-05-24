# Building a simple translator 
# Basic rules of the language, any vowel is translated to g

# translator function
def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter in "AEIOUaeiou": # to check if the letter is a vowel. We can specify the case
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
         
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: " )))