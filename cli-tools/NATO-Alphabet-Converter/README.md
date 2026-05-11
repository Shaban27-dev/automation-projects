# NATO Phonetic Alphabet Converter

Converts any word or sentence into its NATO phonetic alphabet equivalent.
Reads the alphabet data from a CSV file using Pandas — no hardcoded lookups.

---

## How to run
```bash
pip install pandas
python main.py
```

You will be prompted to enter a word or sentence. The converter handles
uppercase and lowercase input automatically.

## Sample output
```
Enter a word or sentence: Python

P → Papa
Y → Yankee
T → Tango
H → Hotel
O → Oscar
N → November

Letters entered : 6
Unique letters  : 6
NATO output     : ['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

---

## Features

- ⌨️ Accepts any word or sentence as input
- 🔠 Converts to uppercase automatically before processing
- 📂 Loads NATO alphabet from a CSV file — easily updatable
- 🔁 Converts each letter to its phonetic code word
- 📊 Displays total letter count and unique letter count
- 📢 Prints clean formatted output

## Stack
```
Python 3  ·  Pandas  ·  CSV
```

---

## Author

Shaban Alam · [shabandev27@gmail.com](mailto: shabandev27@gmail.com)
Available for freelance Python automation work.