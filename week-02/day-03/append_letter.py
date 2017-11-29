# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs(list1, text):
    new_verbs = []
    for i in list1:
        i = text + i
        new_verbs.insert(len(new_verbs), str(i))
    return new_verbs

