# Extension
# Check out the [python](./python) folder. There's a work file and a test file.
# - Run the tests, all 10 should be green (passing).
# - The implementations though are not quite good.
# - Create tests that'll fail, and will show how the implementations are wrong
# - After creating the tests, fix the implementations
# - Check again, if you can create failing tests
# - Implement if needed

# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

# Returns the median value of a list given as param
def median(pool):
    n = len(pool)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(pool)[n//2]
    return sum(sorted(pool)[n//2-1:n//2+1])/2.0


# Returns true if the param is a vowel
def is_vowel(char):
    return char.lower() in 'aeiouáéíóöőúüű'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = ""
    for char in hungarian:
        if is_vowel(char):
            teve += (char + 'v' + char)
        else:
            teve += char
    return teve