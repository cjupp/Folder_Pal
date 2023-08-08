import os as os

#Other indexing ideas:
# - date
# - days of week
# -



#Creates an alphabetical numbering system in the format "ABC"
def Get_Index_Alphabetical(number_index, letter_case = 1):
    return_string = ""
    modulo = 0
    floor_result = 0
    ascii_offset = 65

    #If number is non zero
    if number_index > 0:
        number_index -= 1
        # If the letter_case is 0 ir false, use lower case
        if not letter_case:
            ascii_offset = 97

        # Check if the number is divisible by 26
        floor_result = number_index // 26
        if floor_result:

            # Get the modulus from the division
            modulo = number_index % 26

            # If it is, recursively call itself with the floor division result
            return_string += Get_Index_Alphabetical(floor_result, letter_case)


            return_string += chr(ascii_offset + modulo)


        # Otherwise, simply return the string based on the original argument
        else:
            return_string += chr(ascii_offset + number_index)

        # Return the resulting string
        return return_string

    else:
        return "Invalid Number"



def Create_Folders(path, number, prefix, suffix, indexing, subfolders):

    #Change the directory to the given path
    os.chdir(path)

    #Repeat for the number of folders given
    for num in range(1, number + 1):

        index = 0

        if indexing == "Numeric":
            index = str(num)

        elif indexing == "Alphabetic":
            index = Get_Index_Alphabetical(num)

        else:
            index = str(num)

        # Create folder name string
        folder_name = prefix + index + suffix

        # Create folder with that name
        os.makedirs(folder_name, exist_ok=True)

        # Add subfolders if applicable
        for folder in subfolders:

            subfolder_path = folder_name + "/" + folder
            os.makedirs(subfolder_path, exist_ok=True)