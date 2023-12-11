from customtkinter import*
from tkinter import*
from datetime import datetime
import webbrowser


date = datetime.now()
dateP = date.strftime("%d/%m/%Y")

app = CTk()
app.geometry("1920x1080")
app.title("To-do list-By SKAFRAG")
app.iconbitmap("todo-list.ico")

topFrame = CTkFrame(master=app, width=1920, height=75,)
topFrame.place(relx=0.5, rely=0.05, anchor="center")

current_y = 0.23
check_var = StringVar(value="off")
checkbox_vars = []


# Initialisation de l'état actuel de l'interface
mode = "system"
set_appearance_mode(mode)

def toggle_mode():
    global mode
    if mode == "light":
        mode = "dark"
        set_appearance_mode("Dark")
        btn.configure(text="Switch to a light interface")
        print("Dark interface")
    else:
        mode = "light"
        set_appearance_mode("Light")
        btn.configure(text="Switch to a Dark interface")
        print("light interface")


def champ():
    global mode, current_y, check_var, checkbox_vars

    cadre_taches = CTkFrame(master=app, width=1920, height=1005, fg_color="transparent")
    cadre_taches.place(relx=0.5, rely=current_y, anchor="center")

    frame_checkBox = CTkFrame(master=app, width=1920, height=1005, fg_color="transparent")
    frame_checkBox.place(relx=0.4, rely=current_y, anchor="center")

    tache = CTkEntry(master=cadre_taches, placeholder_text="Inscribe your task", corner_radius=50, border_width=2)
    tache.pack(pady=12, anchor="center")

    checkbox_var = StringVar(value="off")
    checkbox_vars.append(checkbox_var)

    # Fonction pour mettre à jour le texte de la case à cocher
    def update_checkbox_text(var, checkbox):
        text = "Not done" if var.get() == "off" else "Done"
        checkbox.configure(text=text)

    text_CheckBox = "Not done" if checkbox_var.get() == "off" else "done"
    checkBox = CTkCheckBox(master=frame_checkBox, text=text_CheckBox, variable=checkbox_var, onvalue="on", offvalue="off")
    checkBox.pack(padx=5)

    # Lier l'événement de changement d'état de la case à cocher à la fonction de mise à jour du texte
    checkBox.configure(command=lambda: update_checkbox_text(checkbox_var, checkBox))

    current_y += 0.07

def github():
    link = "https://github.com/SKAFRAG"    
    webbrowser.open(link)

initial_text = "Switch to a dark interface" if mode == "light" else "Switch to a light interface"
btn = CTkButton(master=topFrame, text=initial_text, corner_radius=50, 
                border_width=2, command=toggle_mode)
btn.place(relx=0.5, rely=0.3, anchor="center")


textDate = "Ma Todo list du", date
print(textDate)
todoList = CTkLabel(master=topFrame, text=f"My to-do list for : {dateP}")
todoList.place(relx=0.5, rely=0.7, anchor="center")

mg = CTkButton(master=topFrame, text="My Github for others projects",corner_radius=50,border_width=2, command=github)
mg.place(relx=0.4, rely=0.3, anchor="center")

bug = CTkLabel(master=app, text="If you encounter a bug, you can report it on my GitHub.")
bug.place(relx=0.11, rely=0.99, anchor="center")

make = CTkLabel(master=app, text="Make by SKAFRAG")
make.place(relx=0.5, rely=0.99, anchor="center")


btn2 = CTkButton(master=app, text="Add an item to the to-do list.", corner_radius=50,border_width=2, command=champ, )
btn2.place(relx=0.5, rely=0.15, anchor="center")


app.mainloop()