import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

# Folders/files to ignore
IGNORE = {"node_modules", ".git", ".DS_Store", "__pycache__"}

# Create tree string recursively
def generate_tree(dir_path, prefix=""):
    tree_str = ""
    try:
        entries = [e for e in os.listdir(dir_path) if e not in IGNORE]
    except PermissionError:
        return prefix + "Permission Denied\n"

    entries.sort()

    for i, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        tree_str += prefix + connector + entry + "\n"

        if os.path.isdir(path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            tree_str += generate_tree(path, new_prefix)

    return tree_str

# GUI App
class FolderTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📁 Folder Tree Viewer")
        self.root.geometry("800x600")

        self.select_button = tk.Button(root, text="Select Folder", command=self.select_folder, font=("Segoe UI", 12))
        self.select_button.pack(pady=10)

        self.output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier New", 10))
        self.output_box.pack(expand=True, fill='both', padx=10, pady=10)

        self.save_button = tk.Button(root, text="💾 Save Output", command=self.save_output, font=("Segoe UI", 11))
        self.save_button.pack(pady=5)

    def select_folder(self):
        folder = filedialog.askdirectory(title="Choose a folder")
        if folder:
            self.output_box.delete('1.0', tk.END)
            tree = generate_tree(folder)
            self.output_box.insert(tk.END, f"Folder Tree for: {folder}\n\n{tree}")

    def save_output(self):
        content = self.output_box.get('1.0', tk.END).strip()
        if not content:
            messagebox.showwarning("No Output", "Nothing to save.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Saved", f"Tree saved to:\n{save_path}")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = FolderTreeApp(root)
    root.mainloop()
