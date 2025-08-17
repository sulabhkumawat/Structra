📁 Folder Tree Generator (GUI)

A simple Python GUI app to generate a visual folder structure (tree) for any selected directory. Useful for quickly understanding project structure or sharing folder layouts (e.g., with ChatGPT or collaborators).

<!-- Replace with actual screenshot if available -->

✨ Features

GUI-based folder picker (no command-line needed)

Ignores clutter like node_modules, .git, __pycache__, etc.

Displays folder tree in a scrollable window

Save output to .txt file for sharing

Built with tkinter, no extra dependencies

📦 Installation

Clone this repository:



Run the app:

main.py


✅ Requirements:

Python 3.x

Works on Windows, macOS, and Linux (no extra libraries required)

🖥️ Usage

Launch the app:

python folder_tree_gui.py


Click "Select Folder" and choose any directory on your system.

The folder tree will be displayed in the window.

Click "Save Output" to export it as a .txt file.

📂 Example Output
Folder Tree for: /Users/example/react-app

├── public
│   └── index.html
├── src
│   ├── App.js
│   ├── components
│   │   └── Header.js
├── package.json
└── README.md

🛠️ Customization

You can modify the following in folder_tree_gui.py:

Ignore list: Add/remove folders in the IGNORE set:

IGNORE = {"node_modules", ".git", ".DS_Store", "__pycache__"}


Font and theme (inside tkinter widgets)

Output formatting (Markdown, plain text, etc.)

📦 Convert to EXE (Optional)

If you want to make this app double-clickable on Windows:

pip install pyinstaller
pyinstaller --onefile --windowed folder_tree_gui.py


The .exe will be generated in the dist/ folder.

📄 License

MIT License – free for personal and commercial use.

🙌 Author

Made by sulabh kumawat
Feel free to contribute or suggest improvements!
