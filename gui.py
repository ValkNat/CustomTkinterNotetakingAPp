#imports
import customtkinter
import tkinter as tk
from tkinter import simpledialog, filedialog
import datetime
import os

#initialize appearance for customtkinter window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#initializing customtkinter root
root = customtkinter.CTk()
root.geometry("900x900")
root.grid_columnconfigure(0, weight=1)

#to-do list list
to_do_list = []

#adds entry to list
def add_entry(entry):
    to_do_list.append(entry)
    print(to_do_list)
    checkbox = customtkinter.CTkCheckBox(master = frame, text=entry)
    checkbox.grid(sticky="w", pady=2, padx=10)
    to_do_entry.delete(0, 'end')

#saves list of entries to Obsidian
def saveToObsidian():
    with open('vault_location.txt', 'r') as file:
        vault_location = file.read()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = os.path.join(vault_location, 'to-do ' + timestamp + '.md')
        saveToFile(file_path, to_do_list)

def saveToFile(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write('- [ ] '+ str(item) + '\n')
    

#connecting to Obsidian functionality
def connectObsidian():
    vault_location = filedialog.askdirectory()
    open('vault_location.txt', 'w').close()
    with open('vault_location.txt', 'w') as file:
        file.write(str(vault_location))
    
#customtkinter frame setup
frame = customtkinter.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#Tkinter Main Frame Widget Setup
label = customtkinter.CTkLabel(master=frame, text="To-Do List", font=("Roboto", 24))
label.grid(row=0, column=0, pady=12, padx=10)
to_do_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Add New Entry")
to_do_entry.grid(row = 0, column=2, pady=12, padx=10)
to_do_entry_submission = customtkinter.CTkButton(master=frame, text="Add Entry", command= lambda: add_entry(to_do_entry.get()))
to_do_entry_submission.grid(row=0, column=3, pady=2, padx=10)
save_file_button = customtkinter.CTkButton(master=frame, text="Save to file", command=saveToObsidian)
save_file_button.grid(row=0, column=4, pady=5, padx=10)

#syncing with obsidian widget setup
obsidian_setup = customtkinter.CTkButton(master=frame, text="Connect to obsidian vault", command=connectObsidian)
obsidian_setup.grid(row=0, column=5, pady=5, padx=10)


#runs main customtkinter loop
root.mainloop()

