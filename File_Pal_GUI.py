import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

from tkinter import filedialog as fd
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



"""------------------------------------------------------------------------------------
Select_File: 
                -----------------------------------------------
Arguments:

 - : 
                -----------------------------------------------
Returns: 
                -----------------------------------------------
Created by: Cameron Jupp
Date:       
Edited:
------------------------------------------------------------------------------------"""
def Select_Path():
    path = fd.askdirectory(title='Choose folder root path', initialdir='/')
    print(path)
    return path

#
def Add_Subfolder(list_widget, entry_widget):
    #Get the string in the entry widget
    folder_name = entry_widget.get()

    #If there is text in the folder name entry
    if folder_name != "" and folder_name not in fp.dictionary_subfolders:
        #Add the name to the list
        list_widget.insert(tk.END, folder_name)


        #Add the name of the folder to the dictionary
        fp.Add_to_Subfolder_Dict(folder_name)

    # Remove the text from the entry widget
    entry_widget.delete(0, tk.END)


    print(fp.dictionary_subfolders)


def Delete_Subfolder(list_widget):
    #Get the indexes of selected items
    selections = list_widget.curselection()

    #Create list for names
    folder_names = list()

    #Add names to list for every selected index
    for index in selections:
        folder_names.append(list_widget.get(index))

    #Delete all items from dictionary based on name
    for name in folder_names:
        fp.dictionary_subfolders.pop(name)

    #Delete all items in list based on name
    for item in reversed(selections):
        list_widget.delete(item)



def Add_Sub_Subfolder(subfolder_list_widget, sub_subfolder_list_widget, entry_widget):
    #Get the string in the entry widget
    folder_name = entry_widget.get()
    print("Folder name " + folder_name)

    parent_folder = subfolder_list_widget.get(tk.ACTIVE)
    print("Parent folder " + parent_folder)

    #If there is text in the folder name entry
    if folder_name != "" and parent_folder != '':
        #Remove the text from the entry widget
        entry_widget.delete(0, tk.END)

        #Add the name of the folder to the dictionary
        fp.Add_to_Sub_Subfolder_Dict(parent_folder, folder_name)

        #Clear the sub-subfolder list
        Clear_List(sub_subfolder_list_widget)

        #Repopulate with update values
        Populate_Sub_Subfolder_List(parent_folder, sub_subfolder_list_widget)

    print(fp.dictionary_sub_subfolders)


def Delete_Sub_Subfolder():

    return

#Gather all information from the gui and make the folders
def Execute_Folder_Creation():
    return

def Clear_List(list_widget):
    list_widget.delete(0,tk.END)

def Populate_Sub_Subfolder_List(parent_folder, list_widget):
    for folder in fp.dictionary_sub_subfolders[parent_folder]:
        list_widget.insert(tk.END, folder)

def Create_Main_Folders():
    return

def CreateSubfolders():
    return

def Create_Sub_Subfolder():
    return

def Set_Indexing(Index_String):
    print(Index_String)




path = 0
prefix_string = 0
suffix_string = 0
folder_name = 0

folder_count = 0
subfolders = 0

indexing_options = ["Numerical", "Alphabetical"]

# --------------------------------------------------------------------------------------------------------------------
# -------------------------------------  / \/ \      /  \     /_  _/  / \  / /  --------------------------------------
# ------------------------------------  / /\/\ \    / /_\\     / /   / /\\/ /  ---------------------------------------
# -----------------------------------  /_/    \_\  /_/   \\  /___/  /_/  \_/  ----------------------------------------
# --------------------------------------------------------------------------------------------------------------------
#Background colors for the GUI. Change these to change the theme of the GUI
main_background = "light gray"  # config variable to set the main background color
secondary_background = 'light gray'  # sets the accent background colors in the GUI

color_GO_Button = 'Green'


universal_font = "Century Gothic Bold"
fontsize_labelframes = "12"
fontsize_listboxes = "12"
fontsize_entryboxes = "12"
fontsize_subfolder_buttons = "12"
fontsize_spinboxes = "12"
fontsize_GO_Button = "20"

width_subfolder_entry = 12





Main = ThemedTk()
#Name the window
Main.title("Folder Pal")
#Set the size for the window
Main.geometry("750x750")
#main.iconbitmap("GUI Assets\Icon.ico")


Menu_Style = ttk.Style()
Menu_Style.theme_use('alt')
Menu_Style.configure('alt.TButton', font = (universal_font))
Menu_Style.configure('alt.TEntry', font = (universal_font))
Menu_Style.configure('alt.TLabelframe', font = (universal_font))




#When the window closes, trigger a function to shut everything down and tie up loose ends
#Main.protocol("WM_DELETE_WINDOW", lambda: Close_Window(Main))

Main_Deco_Frame = tk.LabelFrame(Main)
Main_Deco_Frame.pack(side = tk.TOP, expand = "yes", fill = "both", padx = 10, pady = 10)


#Path ---------------------------------------------------------------------------------------------------------
gui_path = tk.StringVar()

Labelframe_Path = ttk.LabelFrame(Main_Deco_Frame, text="Path", style = "alt.TLabelframe")
Labelframe_Path.grid(row = 2, rowspan = 1, column = 1, columnspan = 2, padx = 0, pady = 0, sticky = tk.NSEW)

Button_Choose_Path = ttk.Button(Labelframe_Path, text = "Browse", command=lambda: Select_Path(), style = "alt.TButton")
Button_Choose_Path.grid(row = 2, rowspan = 1, column = 1, columnspan = 2, padx = 0, pady = 0, sticky = tk.NSEW)

Entry_Path = ttk.Entry(Labelframe_Path, text = "Path name", width = width_subfolder_entry, style = 'alt.TEntry', textvariable = gui_path)
#Input_Add_Subfolder.bind("<Return>", (lambda event: AngleCodesCommandSend("moveAngle", s_ang_enter, s_ang_dir, e_ang_enter, e_ang_dir)))
Entry_Path.grid(row = 2, rowspan = 1, column = 1, columnspan = 2, padx = 0, pady = 0, sticky = tk.NSEW)


#Folder Names ---------------------------------------------------------------------------------------------------------
Labelframe_Folder_Text = ttk.LabelFrame(Main_Deco_Frame, text="Folder Names")
Labelframe_Folder_Text.grid(row = 2, rowspan = 1, column = 1, columnspan = 2, padx = 0, pady = 0, sticky = tk.NSEW)

#Prefix
gui_prefix = tk.StringVar()

Labelframe_Name_Prefix = ttk.LabelFrame(Labelframe_Folder_Text, text="Prefix")
Labelframe_Name_Prefix.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Entry_Name_Prefix = ttk.Entry(Labelframe_Name_Prefix, text = "Prefix", width = width_subfolder_entry, font = (universal_font, fontsize_entryboxes), textvariable = gui_prefix)
Entry_Name_Prefix.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

#Suffix
gui_suffix = tk.StringVar()

Labelframe_Name_Suffix = ttk.LabelFrame(Labelframe_Folder_Text, text="Suffix")
Labelframe_Name_Suffix.grid(row = 2, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Entry_Name_Suffix = ttk.Entry(Labelframe_Name_Suffix, text = "Suffix", width = width_subfolder_entry, font = (universal_font, fontsize_entryboxes), textvariable = gui_suffix)
Entry_Name_Suffix.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

#Indexing Type
gui_indexing = tk.StringVar(value = indexing_options[0])

Labelframe_Name_Indexing = ttk.LabelFrame(Labelframe_Folder_Text, text="Indexing")
Labelframe_Name_Indexing.grid(row = 1, rowspan = 2, column = 3, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Optionmenu_Indexing = ttk.OptionMenu(Labelframe_Name_Indexing, gui_indexing, *indexing_options, command = lambda event: Set_Indexing(gui_indexing.get()))
Optionmenu_Indexing.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

#Folder Number
folder_number = tk.StringVar(value = 1)
folder_values = 1

Labelframe_Folder_Number = ttk.LabelFrame(Labelframe_Folder_Text, text="Number")
Labelframe_Folder_Number.grid(row = 1, rowspan = 2, column = 2, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Spinbox_Folder_Number = ttk.Spinbox(Labelframe_Folder_Number, from_= 1, to = 999999999, font = (universal_font, fontsize_spinboxes), textvariable = folder_number)
Spinbox_Folder_Number.grid(row = 1, rowspan = 2, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)



#Subfolders ---------------------------------------------------------------------------------------------------------
add_subfolder_name = tk.StringVar()

Labelframe_Subfolder = ttk.LabelFrame(Main_Deco_Frame, text="Subfolders")
Labelframe_Subfolder.grid(row = 3, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Entry_Add_Subfolder = ttk.Entry(Labelframe_Subfolder, text = "Enter a subfolder name", width = width_subfolder_entry, font = (universal_font, fontsize_entryboxes), textvariable = add_subfolder_name)
Entry_Add_Subfolder.bind("<Return>", lambda event: Add_Subfolder(Listbox_Subfolders, Entry_Add_Subfolder))
Entry_Add_Subfolder.grid(row=1, rowspan=1, column=1, columnspan=1, sticky=tk.NSEW, pady=0, padx=0)

Button_Add_Subfolder = ttk.Button(Labelframe_Subfolder, text = "Add", command = lambda: Add_Subfolder(Listbox_Subfolders, Entry_Add_Subfolder))
Button_Add_Subfolder.grid(row = 1, rowspan = 1, column = 2, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Listbox_Subfolders = tk.Listbox(Labelframe_Subfolder, font = (universal_font, fontsize_listboxes), width = 30, height = 6)
Listbox_Subfolders.grid(row = 2, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Scrollbar_Subfolders = tk.Scrollbar(Labelframe_Subfolder)
Scrollbar_Subfolders.grid(row = 2, rowspan = 1, column = 2, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Listbox_Subfolders.config(yscrollcommand= Scrollbar_Subfolders.set)
Scrollbar_Subfolders.config(command = Listbox_Subfolders.yview)

Listbox_Subfolders.bind('<Delete>', lambda event: Delete_Subfolder(Listbox_Subfolders))


#Sub-Subfolders ---------------------------------------------------------------------------------------------------------
add_sub_subfolder_name = tk.StringVar()

Labelframe_Sub_Subfolder = ttk.LabelFrame(Main_Deco_Frame, text="Subfolders")
Labelframe_Sub_Subfolder.grid(row = 3, rowspan = 1, column = 2, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Entry_Add_Sub_Subfolder = ttk.Entry(Labelframe_Sub_Subfolder, text = "Enter a subfolder name", width = width_subfolder_entry)
Entry_Add_Sub_Subfolder.bind("<Return>", lambda event: Add_Sub_Subfolder(Listbox_Subfolders, Listbox_Sub_Subfolders, Entry_Add_Sub_Subfolder))
Entry_Add_Sub_Subfolder.grid(row=1, rowspan=1, column=1, columnspan=1, sticky=tk.NSEW, pady=0, padx=0)

Button_Add_Sub_Subfolder = ttk.Button(Labelframe_Sub_Subfolder, text = "Add", command = lambda: Add_Sub_Subfolder(Listbox_Subfolders, Listbox_Sub_Subfolders, Entry_Add_Sub_Subfolder))
Button_Add_Sub_Subfolder.grid(row = 1, rowspan = 1, column = 2, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Listbox_Sub_Subfolders = tk.Listbox(Labelframe_Sub_Subfolder, font = (universal_font, fontsize_listboxes), width = 30, height = 6)
Listbox_Sub_Subfolders.grid(row = 2, rowspan = 1, column = 1, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Scrollbar_Sub_Subfolders = tk.Scrollbar(Labelframe_Sub_Subfolder)
Scrollbar_Sub_Subfolders.grid(row = 2, rowspan = 1, column = 2, columnspan = 1, padx = 0, pady = 0, sticky = tk.NSEW)

Listbox_Sub_Subfolders.config(yscrollcommand= Scrollbar_Sub_Subfolders.set)
Scrollbar_Sub_Subfolders.config(command = Listbox_Sub_Subfolders.yview)

#Listbox_Sub_Subfolders.bind('<Delete>', lambda event: Delete_Sub_Subfolder)

#GO Button -------------------------------------------------------------------------------------------------------------
Button_GO = ttk.Button(Main_Deco_Frame, text = "GO", command = lambda: Execute_Folder_Creation())
Button_GO.grid(row = 4, rowspan = 1, column = 1, columnspan = 2, padx = 0, pady = 0, sticky = tk.NSEW)

Main.mainloop()















