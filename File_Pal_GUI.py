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
def Select_Path(stringvar_path):
    path = fd.askdirectory(title='Choose folder root path', initialdir='/')
    print(path)
    stringvar_path.set(path)

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


def Delete_Subfolder(subfolder_list_widget, sub_subfolder_list_widget):
    #Get the indexes of selected items
    folder_name = subfolder_list_widget.get(tk.ACTIVE)
    list_index = subfolder_list_widget.curselection()
    subfolder_list_widget.delete(list_index)

    #Delete the folder from the dictionary
    fp.Delete_from_Subfolder_Dict(folder_name)

    #Remove old values from sub-subfolder listbox
    Clear_List(sub_subfolder_list_widget)


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
        Populate_Sub_Subfolder_List_by_Name(parent_folder, sub_subfolder_list_widget)

    print(fp.dictionary_sub_subfolders)


def Delete_Sub_Subfolder(subfolder_list_widget, sub_subfolder_list_widget):
    parent_selection_index = subfolder_list_widget.curselection()
    child_selection_index = sub_subfolder_list_widget.curselection()

    if parent_selection_index and child_selection_index:
        parent_folder = subfolder_list_widget.get(parent_selection_index)
        child_folder = sub_subfolder_list_widget.get(child_selection_index)

        fp.Delete_Child_from_Sub_Subfolder_Dict(parent_folder, child_folder)

        Clear_List(sub_subfolder_list_widget)

        #Clear selection from subfolder list
        subfolder_list_widget.selection_clear(0, tk.END)

        #Find next item

        Populate_Sub_Subfolder_List_by_Name(parent_folder, sub_subfolder_list_widget)

#Gather all information from the gui and make the folders
def Execute_Folder_Creation(path_variable, prefix_entry_widget, suffix_entry_widget, number_spinbox_widget, indexing_variable):
    #Get all necessary data from GUI interface
    path = path_variable.get()
    prefix_string = prefix_entry_widget.get()
    suffix_string = suffix_entry_widget.get()
    folder_number = int(number_spinbox_widget.get())
    indexing_type = indexing_variable.get()

    print("Path: " + path)
    print("Prefix: " + prefix_string)
    print("Suffix: " + suffix_string)
    print("Number: " + str(folder_number))
    print("Indexing Type: " + indexing_type)

    #Pass it on to module function
    fp.Create_Folders(path, folder_number, prefix_string, suffix_string, indexing_type)

def Clear_List(list_widget):
    list_widget.delete(0, tk.END)

def Populate_Sub_Subfolder_List_by_Name(parent_folder, sub_subfolder_list_widget):
    Clear_List(sub_subfolder_list_widget)

    if parent_folder != '' and parent_folder in fp.dictionary_sub_subfolders:
            for folder in fp.dictionary_sub_subfolders[parent_folder]:
                sub_subfolder_list_widget.insert(tk.END, fp.dictionary_sub_subfolders[parent_folder][folder])


def Populate_Sub_Subfolder_List_by_Selection(subfolder_list_widget, sub_subfolder_list_widget):
    Clear_List(sub_subfolder_list_widget)
    selection_index = subfolder_list_widget.curselection()
    print(selection_index)

    if selection_index:
        parent_folder = subfolder_list_widget.get(selection_index)

        if parent_folder != '' and parent_folder in fp.dictionary_sub_subfolders:
            for folder in fp.dictionary_sub_subfolders[parent_folder]:
                sub_subfolder_list_widget.insert(tk.END, fp.dictionary_sub_subfolders[parent_folder][folder])


def Set_Indexing(Index_String):
    print(Index_String)

def Set_Path_Variable(path, path_entry_widget):
    path.set(path_entry_widget.get())


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

fontsize_main_labelframes = 20
fontsize_labelframes = 12
fontsize_listboxes = 12
fontsize_entryboxes = 12
fontsize_subfolder_buttons = 12
fontsize_spinboxes = 12
fontsize_GO_Button = 20

width_subfolder_entry = 22
width_path_entry = 50
width_subfolder_button = 2
width_number_spinbox = 5

padding_x_main_labelframes = 5
padding_y_main_labelframes = 5

padding_x_sub_labelframes = 5
padding_y_sub_labelframes = 5


text_add_button = "+"





Main = ThemedTk()
#Name the window
Main.title("Folder Pal")
#Set the size for the window
Main.geometry("750x750")
#main.iconbitmap("GUI Assets\Icon.ico")


Menu_Style = ttk.Style()
Menu_Style.theme_use('alt')
Menu_Style.configure('alt.TButton', font = (universal_font))
Menu_Style.configure('alt.TEntry', font = (universal_font, fontsize_GO_Button))
Menu_Style.configure('alt.TLabelframe', font = (universal_font), background = main_background)


Add_Subfolder_Button_Style = Menu_Style
Add_Subfolder_Button_Style.configure
#When the window closes, trigger a function to shut everything down and tie up loose ends
#Main.protocol("WM_DELETE_WINDOW", lambda: Close_Window(Main))

Main_Deco_Frame = tk.LabelFrame(Main, bg = main_background)
Main_Deco_Frame.pack(side = tk.TOP, expand = "yes", fill = "both", padx = 10, pady = 10)


#Path ---------------------------------------------------------------------------------------------------------
gui_path = tk.StringVar()

Labelframe_Path = ttk.LabelFrame(Main_Deco_Frame, text="Path", style = "mainlabel.TLabelframe")
Labelframe_Path.grid(row = 1, rowspan = 1, column = 1, columnspan = 2, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

Button_Choose_Path = ttk.Button(Labelframe_Path, text = "Browse", command=lambda: Select_Path(gui_path))
Button_Choose_Path.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Entry_Path = ttk.Entry(Labelframe_Path, text = "Path name", width = width_path_entry, style = 'alt.TEntry', textvariable = gui_path)
Entry_Path.bind("<Return>", (lambda event: Set_Path_Variable(gui_path, Entry_Path)))
Entry_Path.grid(row = 1, rowspan = 1, column = 2, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)


#Folder Names ---------------------------------------------------------------------------------------------------------
Labelframe_Folder_Text = ttk.LabelFrame(Main_Deco_Frame, text="Folder Names", style = "alt.TLabelframe")
Labelframe_Folder_Text.grid(row = 2, rowspan = 1, column = 1, columnspan = 2, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

#Prefix
gui_prefix = tk.StringVar()

Labelframe_Name_Prefix = ttk.LabelFrame(Labelframe_Folder_Text, text="Prefix", style = "alt.TLabelframe")
Labelframe_Name_Prefix.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

Entry_Name_Prefix = ttk.Entry(Labelframe_Name_Prefix, text = "Prefix", width = width_subfolder_entry, font = (universal_font, fontsize_entryboxes), textvariable = gui_prefix)
Entry_Name_Prefix.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

#Suffix
gui_suffix = tk.StringVar()

Labelframe_Name_Suffix = ttk.LabelFrame(Labelframe_Folder_Text, text="Suffix", style = "alt.TLabelframe")
Labelframe_Name_Suffix.grid(row = 1, rowspan = 1, column = 4, columnspan = 1, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

Entry_Name_Suffix = ttk.Entry(Labelframe_Name_Suffix, text = "Suffix", width = width_subfolder_entry, font = (universal_font, fontsize_entryboxes), textvariable = gui_suffix)
Entry_Name_Suffix.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

#Indexing Type
gui_indexing = tk.StringVar(value = indexing_options[0])

Labelframe_Name_Indexing = ttk.LabelFrame(Labelframe_Folder_Text, text="Indexing", style = "alt.TLabelframe")
Labelframe_Name_Indexing.grid(row = 1, rowspan = 2, column = 3, columnspan = 1, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

Optionmenu_Indexing = ttk.OptionMenu(Labelframe_Name_Indexing, gui_indexing, *indexing_options, command = lambda event: Set_Indexing(gui_indexing.get()))
Optionmenu_Indexing.grid(row = 1, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

#Folder Number
folder_number = tk.StringVar(value = 1)
folder_values = 1

Labelframe_Folder_Number = ttk.LabelFrame(Labelframe_Folder_Text, text="Number", style = "alt.TLabelframe")
Labelframe_Folder_Number.grid(row = 1, rowspan = 2, column = 2, columnspan = 1, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

Spinbox_Folder_Number = ttk.Spinbox(Labelframe_Folder_Number, from_= 1, to = 999999999, width = width_number_spinbox, font = (universal_font, fontsize_spinboxes), textvariable = folder_number)
Spinbox_Folder_Number.grid(row = 1, rowspan = 2, column = 1, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)



#Subfolders ---------------------------------------------------------------------------------------------------------
add_subfolder_name = tk.StringVar()

Labelframe_Subfolder = ttk.LabelFrame(Main_Deco_Frame, text="Subfolders", style = "alt.TLabelframe")
Labelframe_Subfolder.grid(row = 3, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

Entry_Add_Subfolder = ttk.Entry(Labelframe_Subfolder, text = "Enter a subfolder name", width = width_subfolder_entry, font = (universal_font, fontsize_entryboxes), textvariable = add_subfolder_name)
Entry_Add_Subfolder.bind("<Return>", lambda event: Add_Subfolder(Listbox_Subfolders, Entry_Add_Subfolder))
Entry_Add_Subfolder.grid(row=1, rowspan=1, column=1, columnspan=1, sticky=tk.NSEW, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes)

Button_Add_Subfolder = ttk.Button(Labelframe_Subfolder, text = text_add_button, width = width_subfolder_button, command = lambda: Add_Subfolder(Listbox_Subfolders, Entry_Add_Subfolder))
Button_Add_Subfolder.grid(row = 1, rowspan = 1, column = 2, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Listbox_Subfolders = tk.Listbox(Labelframe_Subfolder, font = (universal_font, fontsize_listboxes), width = 30, height = 6, exportselection = False)
Listbox_Subfolders.grid(row = 2, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Scrollbar_Subfolders = tk.Scrollbar(Labelframe_Subfolder)
Scrollbar_Subfolders.grid(row = 2, rowspan = 1, column = 2, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Listbox_Subfolders.config(yscrollcommand= Scrollbar_Subfolders.set)
Scrollbar_Subfolders.config(command = Listbox_Subfolders.yview)

Listbox_Subfolders.bind('<Delete>', lambda event: Delete_Subfolder(Listbox_Subfolders, Listbox_Sub_Subfolders))
Listbox_Subfolders.bind('<<ListboxSelect>>', lambda event: Populate_Sub_Subfolder_List_by_Selection(Listbox_Subfolders, Listbox_Sub_Subfolders))


#Sub-Subfolders ---------------------------------------------------------------------------------------------------------
add_sub_subfolder_name = tk.StringVar()

Labelframe_Sub_Subfolder = ttk.LabelFrame(Main_Deco_Frame, text="Sub-Subfolders", style = "alt.TLabelframe")
Labelframe_Sub_Subfolder.grid(row = 3, rowspan = 1, column = 2, columnspan = 1, padx = padding_x_main_labelframes, pady = padding_y_main_labelframes, sticky = tk.NSEW)

Entry_Add_Sub_Subfolder = ttk.Entry(Labelframe_Sub_Subfolder, text = "Enter a subfolder name", width = width_subfolder_entry)
Entry_Add_Sub_Subfolder.bind("<Return>", lambda event: Add_Sub_Subfolder(Listbox_Subfolders, Listbox_Sub_Subfolders, Entry_Add_Sub_Subfolder))
Entry_Add_Sub_Subfolder.grid(row=1, rowspan=1, column=1, columnspan=1, sticky=tk.NSEW, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes)

Button_Add_Sub_Subfolder = ttk.Button(Labelframe_Sub_Subfolder, text = text_add_button, width = width_subfolder_button, command = lambda: Add_Sub_Subfolder(Listbox_Subfolders, Listbox_Sub_Subfolders, Entry_Add_Sub_Subfolder))
Button_Add_Sub_Subfolder.grid(row = 1, rowspan = 1, column = 2, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Listbox_Sub_Subfolders = tk.Listbox(Labelframe_Sub_Subfolder, font = (universal_font, fontsize_listboxes), width = 30, height = 6, exportselection = False)
Listbox_Sub_Subfolders.grid(row = 2, rowspan = 1, column = 1, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Scrollbar_Sub_Subfolders = tk.Scrollbar(Labelframe_Sub_Subfolder)
Scrollbar_Sub_Subfolders.grid(row = 2, rowspan = 1, column = 2, columnspan = 1, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Listbox_Sub_Subfolders.config(yscrollcommand= Scrollbar_Sub_Subfolders.set)
Scrollbar_Sub_Subfolders.config(command = Listbox_Sub_Subfolders.yview)

Listbox_Sub_Subfolders.bind('<Delete>', lambda event: Delete_Sub_Subfolder(Listbox_Subfolders, Listbox_Sub_Subfolders))

#GO Button -------------------------------------------------------------------------------------------------------------
Button_GO = ttk.Button(Main_Deco_Frame, text = "GO", command = lambda: Execute_Folder_Creation(gui_path, Entry_Name_Prefix, Entry_Name_Suffix, Spinbox_Folder_Number, gui_indexing))
Button_GO.grid(row = 4, rowspan = 1, column = 1, columnspan = 2, padx = padding_x_sub_labelframes, pady = padding_y_sub_labelframes, sticky = tk.NSEW)

Main.mainloop()















