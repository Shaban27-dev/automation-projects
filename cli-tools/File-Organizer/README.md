# File Organizer

Automatically sorts files in a folder into categorized subfolders based on
file extension. Run it once and a cluttered directory becomes organized.

---

## How to run
```bash
# No dependencies required — uses Python standard library only
python main.py
```

When prompted, enter the full path to the folder you want to organize.

## Sample output
```
📁 Scanning: C:/Users/Shaban/Downloads
------------------------------------------
✔ Moved: resume.pdf        → PDF/
✔ Moved: photo.png         → Images/
✔ Moved: notes.txt         → Text/
✔ Moved: song.mp3          → Music/
------------------------------------------
4 files organized successfully.
```

---

## Features

- 🔍 Scans target folder and detects all files by extension
- 📂 Creates category subfolders automatically if they don't exist
- 📥 Moves each file into its correct subfolder
- 🚫 Skips subfolders and already-organized files safely
- 📊 Reports total files moved at the end

## Supported categories

| Extension | Folder |
|---|---|
| `.txt`, `.docx`, `.md` | Text |
| `.jpg`, `.jpeg`, `.png`, `.gif` | Images |
| `.mp3`, `.wav` | Music |
| `.mp4`, `.mov` | Videos |
| `.pdf` | PDF |
| Anything else | Misc |

## Stack
```
Python 3  ·  os  ·  shutil
```

---

## Author

Shaban Alam · [shabandev27@gmail.com](mailto: shabandev27@gmail.com)
Available for freelance Python automation work.