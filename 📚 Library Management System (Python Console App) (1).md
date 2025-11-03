# 🧾 **README — Smit’s Modules (helpers.py & storage.py)**

### 👨‍💻 Author: *Smit Vengurlekar*  
**Modules:** `helpers.py` and `storage.py`  
**Project:** Library Management System  
**Team Members:** Manas, Piyush, Smit  

---

## 📁 Overview

These two modules handle the **utility backbone** of the Library Management System —  
ensuring data is safely stored, loaded, and displayed properly in the console.

| File | Description |
|------|--------------|
| **helpers.py** | Contains helper functions for confirmations and UI formatting. |
| **storage.py** | Manages saving and loading book data from a JSON file. |

---

## ⚙️ **1. helpers.py**

This file contains simple functions to improve the user experience — for example, confirming actions and adding visual dividers in the console output.

### 📜 Code:
```python
def confirm_action(message):
    choice = input(f"{message} (y/n): ").lower()
    return choice == 'y'

def display_line():
    print("=" * 40)
