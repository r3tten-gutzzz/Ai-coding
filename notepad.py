import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")
current_file = None

def new_file():
    global current_file
    text_area.delete(1.0, tk.END)
    current_file = None
    root.title("Untitled - Text Editor")

def open_file():
    global current_file
    file = filedialog.askopenfilename(defaultextension=".txt",
                                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        current_file = file
        with open(file, "r") as f:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f.read())
        root.title(file + "  - Text Editor")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as f:
            f.write(text_area.get(1.0, tk.END))

    else:
        save_as_file()
def save_as_file():
        global current_file
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            current_file = file
            with open(file, "w") as f:
                f.write(text_area.get(1.0, tk.END))
            root.title(file + " - Text Editor")

def exit_app():
    root.quit()

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+O")
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(fill="both", expand=True)


scroll = tk.Scrollbar(text_area)
scroll.pack(side="right", fill="y")
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)

root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())

root.mainloop()





