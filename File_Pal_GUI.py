import tkinter as tk
import File_Pal_Module as fp

#-------------------------------------------------------------------------------------------------------------------- |
#--------------------------------  / \  / /  / __  /  /__ __/  / ___/  / ____/ --------------------------------------- |
#-------------------------------  / /\\/ /  / /_/ /    / /    / __/    \__ \  ---------------------------------------- |
#------------------------------  /_/  \_/  /_____/    /_/    /____/  /_____/ ----------------------------------------- |
#--------------------------------------------------------------------------------------------------------------------- |
# Last left off at:
#
# - Scrollable listbox to hold subfolders
# - Choose folder path after clicking on browse button
# - Subfolders input text box, with button that adds string into new line in listbox
# - Spinbox to select or input number of folders
#
# - Dynamic gui list that will allow creation of sub-subfolders based on which subfolder is selected in the subfolder
# list
#
# - Use list of pairs to keep track of folders; path:subfolder_name US DICTIONARY! - can index based on folder name
# to populate gui list from sub-subfolder list
#
# - Maybe add numbering for subfolders?
#
#--------------------------------------------------------------------------------------------------------------------- */

path = 0
prefix_string = 0
suffix_string = 0
folder_name = 0

folder_count = 0
subfolders = 0

indexing_types = "Numerical", "Alphabetical"

# --------------------------------------------------------------------------------------------------------------------
# -------------------------------------  / \/ \      /  \     /_  _/  / \  / /  --------------------------------------
# ------------------------------------  / /\/\ \    / /_\\     / /   / /\\/ /  ---------------------------------------
# -----------------------------------  /_/    \_\  /_/   \\  /___/  /_/  \_/  ----------------------------------------
# --------------------------------------------------------------------------------------------------------------------
#Background colors for the GUI. Change these to change the theme of the GUI
main_bg = "#373f42"  # config variable to set the main background color
secondary_bg = 'light gray'  # sets the accent background colors in the GUI

Main = tk.Tk()
#Name the window
Main.title("Folder Pal")
#Set the size for the window
Main.geometry("750x750")

#main.iconbitmap("GUI Assets\Icon.ico")

#When the window closes, trigger a function to shut everything down and tie up loose ends
#Main.protocol("WM_DELETE_WINDOW", lambda: Close_Window(Main))

Main_Deco_Frame = tk.LabelFrame(Main, bg = main_bg)
Main_Deco_Frame.pack(expand = "yes", side = tk.LEFT, fill = "both", padx = 10, pady = 10)

#Path
Labelframe_Path = tk.LabelFrame(Main_Deco_Frame, bg = main_bg)
Labelframe_Path.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = 10, pady = 10, sticky = tk.NSEW)




#Subfolders
#Add list of scanned movers
scanned_frame = tk.LabelFrame(main_deco_frame,
                              text="Scanned Movers",
                              font = (universal_font, entry_font_size),
                              bg = primary_bg)
scanned_frame.grid(row = 2, rowspan = 1, column = 1, columnspan = 1, padx = 30, pady = 30, sticky = tk.NSEW)

scanned_list = tk.Listbox(scanned_frame,
font = (universal_font, entry_font_size),
                              width = 50,
                              height = 10)
scanned_list.pack(side = tk.LEFT, expand = "yes", fill = "both")


scanned_list_scroll = tk.Scrollbar(scanned_frame)
scanned_list_scroll.pack(side = tk.LEFT, fill = "y")

scanned_list.config(yscrollcommand=scanned_list_scroll.set)
scanned_list_scroll.config(command = scanned_list.yview)

mover_entry.bind('<Return>', lambda event: append_mover_list(scanned_list, mover_entry, sheets["Sheet1"]))
scanned_list.bind('<Delete>', lambda event: delete_item(scanned_list))


#Sub-Subfolders

Main.mainloop()





















#
def Add_Subfolder(subfolder_name, subfolder_list, gui_list):
    return

def Add_Sub_Subfolder():
    #maybe not needed, could use above function if setup properly
    return

#Gather all information from the gui and make the folders
def Execute_Folder_Creation():
    return

def Clear_Sub_Subfolder_List():
    return

def Populate_Sub_Subfolder_List():
    return

def Create_Main_Folders():
    return

def CreateSubfolders():
    return

def Create_Sub_Subfolder():
    return