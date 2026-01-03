import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog

def clean_folder(path):
    try:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Non posso eliminare {file_path}. Motivo: {e}")
        messagebox.showinfo("Pulizia completata", f"Cartella {path} pulita con successo!")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la pulizia: {e}")

def choose_and_clean():
    folder_selected = filedialog.askdirectory(title="Scegli la cartella da pulire")
    if folder_selected:
        clean_folder(folder_selected)

def main():
    root = tk.Tk()
    root.title("Pulitore Cartella")
    root.geometry("300x150")

    label = tk.Label(root, text="Premi il pulsante per scegliere la cartella da pulire")
    label.pack(pady=10)

    clean_btn = tk.Button(root, text="Scegli Cartella e Pulisci", command=choose_and_clean, width=25, height=2)
    clean_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
