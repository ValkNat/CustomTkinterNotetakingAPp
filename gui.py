#imports
import customtkinter

#initialize appearance for customtkinter window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#initializing customtkinter root
root = customtkinter.CTk()
root.geometry("500x350")

#to-do list list
to_do_list = []

#adds entry to list
def add_entry(entry):
    to_do_list.append(entry)
    print(to_do_list)
    checkbox = customtkinter.CTkCheckBox(master = frame, text=entry)
    checkbox.pack(pady=2)
    to_do_entry.delete(0, 'end')

#saves list of entries to file
def saveToFile(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
    
#customtkinter frame setup
frame = customtkinter.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#Tkinter Main Frame Widget Setup
label = customtkinter.CTkLabel(master=frame, text="To-Do List", font=("Roboto", 24))
label.pack(pady=12, padx=10)
to_do_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Add New Entry")
to_do_entry.pack(pady=12, padx=10)
to_do_entry_submission = customtkinter.CTkButton(master=frame, text="Add Entry", command= lambda: add_entry(to_do_entry.get()))
to_do_entry_submission.pack(pady=2, padx=10)
save_file_button = customtkinter.CTkButton(master=frame, text="Save to file", command= lambda: saveToFile('todo.txt', to_do_list))
save_file_button.pack(pady=5, padx=10)

#runs main customtkinter loop
root.mainloop()
