# Exercise
# Create a function named create palindrome following your current language's style guide. 
# It should take a string, create a palindrome from it and then return it.
# Examples
# input	output
# ""	""
# "greenfox"	"greenfoxxofneerg"
# "123"	"123321"

def create_palindrome(string1):
    palindrome = string1
    for i in range(len(string1)-1, -1, -1):
        palindrome += string1[i]
    return palindrome
