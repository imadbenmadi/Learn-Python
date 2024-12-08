# input_string = input("Enter a string: ").lower()
# alphebet = "abcdefghijklmnopqrstuvwxyz"
# voils = "aeiou"
# for char in input_string:
#     for v in voils:
#         if char == v :
#             break
#         print(char, end=" ")
    


input_string = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for char in input_string:
    
    is_vowel = False
    for v in vowels:
        if char == v:
            is_vowel = True
            break
    
    if not is_vowel:
        print(char)


# input_string = input("Enter a string: ").lower()

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# vowels = "aeiou"

# for letter in input_string:  
#     is_letter = False
#     is_vowel = False
    
#     for a in alphabet:
#         if letter == a:
#             is_letter = True
#             break

#     for v in vowels:
#         if letter == v:
#             is_vowel = True
#             break
    
#     if is_letter and not is_vowel:  # If it's a letter and not a vowel
#         print(letter, end=" ")
