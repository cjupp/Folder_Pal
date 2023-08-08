import os as os

path = r"C:\Users\camer\Desktop\Folder_Pal_Tests"
prefix_string = "Prefix "
suffix_string = " Suffix"
folder_name = ""

subfolders = "Subfolder 1", "Subfolder 2"

folder_count = 0




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


folder_count = 20

os.chdir(path)

for i in range(1, folder_count+1):
    #Create folder name string
    folder_name = prefix_string + Get_Index_Alphabetical(i) + suffix_string

    #Create folder with that name
    os.makedirs(folder_name, exist_ok = True)

    #Add subfolders if applicable
    for folder in subfolders:
        os.makedirs(folder_name + "/" + folder, exist_ok = True)




#Alphabet test
#print(Get_Index_Alphabetical(72380))


