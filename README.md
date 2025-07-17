# sweetshop
 
A Python-based console application to manage a sweet shop.  
This project follows **Test-Driven Development (TDD)** principles and includes unit tests using `pytest`.

## 🚀 Features

- ➕ Add new sweets with ID, name, category, price, and quantity
- 📋 View all available sweets
- 🗑️ Delete sweets by ID
- 🔍 Search sweets by name, category, or price range
- 🧮 Sort sweets by name or price (ascending/descending)
- 🛒 Purchase sweets (auto-decrease stock)
- 🔁 Restock sweets (increase quantity)
- 🧪 All core features tested using `pytest`
- 🖥️ Clean and interactive terminal menu interface

---
### Technologies Used
- Python 3.10+
- pytest (installed via requirements.txt)
- VS Code

---

## 📁 Files Included

| File              | Description                                |
|-------------------|--------------------------------------------|
| `sweet_shop.py`   | Main logic with all class-based operations |
| `main.py`         | CLI interface to interact with the shop    |
| `test_sweet_shop.py` | Unit tests using `pytest`               |
| `requirements.txt`| Dependencies for this project              |
| `README.md`       | Project documentation                      |

---

## 🛠️ How to Run the Program

### ▶️ Open VS Code Terminal

Ensure you're in the folder where `main.py` exists.

Then run the following command in your terminal:

```bash
python main.py
```

📋 You'll see a CLI menu like this:
======= Sweet Shop Management System =======
1. Add Sweet
2. View Sweets
3. Delete Sweet
4. Purchase Sweet
5. Restock Sweet
6. Search Sweet
7. Sort Sweets
0. Exit
Enter your choice:

---
### 🧪 How to Run Unit Tests
Ensure you're in the project directory and run:
```bash
pytest
```

Make sure pytest is installed using:
```bash
pip install pytest
```

✅ Expected Output (for Tests)
```bash
=================== test session starts ===================
platform win32 -- Python 3.x.x, pytest-x.x.x
collected 10 items

test_sweet_shop.py ..........
==================== 10 passed in 0.03s ====================
```
