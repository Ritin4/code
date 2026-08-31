'''
Problem: Given a string, return true if the string is a palindrome flase if it is not.
Input: string  
Output: True if string  is a palindrome, False if not
'''


''' Valid Plindrome using loops and zip() method'''

# def valid_palindrome(text):
#     if not isinstance(text, str):
#         raise ValueError( "Not a string instance" )

#     clean_text = "".join(char for char in text if char.isalnum()).lower()
#     print("clean_text", clean_text)
#     reverse_text = clean_text[::-1]
    
#     for letter, c_letter in zip(clean_text, reverse_text):
#         print("letter", letter)
#         print("c_letter", c_letter)
#         print(letter == c_letter)
        
#         if letter == c_letter:
#             continue
#         else:
#             return False

#     return True


''' Valid Plindrome using slice'''


# def valid_palindrome(text):

#     if not isinstance(text, str):
#         raise ValueError( "Not a string instance" )

#     clean_text = "".join(char for char in text if char.isalnum()).lower()
    
#     return clean_text == clean_text[::-1]



''' Valid Plindrome using the Two Pointer'''

def valid_palindrome(text):

    if not isinstance(text, str):
        raise ValueError( "Not a string instance" )

    left = 0
    right = len(text) - 1

    while left < right:

        if not text[left].isalnum():
            left += 1
            continue

        if not text[right].isalnum():
            right -= 1
            continue

        if text[left].lower() != text[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True



print(valid_palindrome("palap"))
print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))
print(valid_palindrome("#race a! car77"))
print(valid_palindrome("p!al$a_p"))
