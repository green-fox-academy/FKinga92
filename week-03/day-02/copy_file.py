# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful


def copy_file(file_name1, file_name2):
    success = True
    try:
        filecontent = ""
        with open(file_name1) as f1:
            filecontent = f1.read()
        with open(file_name2, "w") as f2:
            f2.write(filecontent)
    except:
        success = False
    return success
