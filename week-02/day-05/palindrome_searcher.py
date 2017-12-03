# Exercise
# Create a function named search palindrome following your current language's style guide. It should take a string, 
# search for palindromes that at least 3 characters long and return a list with the found palindromes.
# Examples
# input	                                                  output
# "dog goat dad duck doodle never"	["og go", "g g", " dad ", "dad", "d d", "dood", "eve"]
# "apple"	                                                     []
# "racecar"	                                     ["racecar", "aceca", "cec"]
# ""	                                                          []

def search_palindrome(string1):
    alist = []
    palindrome = ""
    for i in range(len(string1)):
        palindrome = string1[i]
        for j in range(i+1, len(string1)):
            palindrome += string1[j] 
            if palindrome == palindrome[: :-1] and len(palindrome) > 2:
                alist.append(palindrome) 
    return alist

print(search_palindrome("dog goat dad duck doodle never"))
