# sweetshop
 
A Python-based console application to manage a sweet shop.  
This project follows **Test-Driven Development (TDD)** principles and includes unit tests using `pytest`.

# 🍬 Sweet Shop Management System

A Python-based console application to manage a sweet shop.  
This project follows **Test-Driven Development (TDD)** principles and includes unit tests using `pytest`.

---

## 📦 Features

- ✅Add new sweets
- ✅ View all sweets
- ✅ Delete sweets by ID
- ✅ Sort sweets by name or price (ascending/descending)
- ✅ Search sweets by:
  - Name
  - Category
  - Price Range
- ✅ Purchase sweets (decrease stock)
- ✅ Restock sweets (increase stock)
- ✅ Clean CLI interface for easy use

---
## 📁 Project Structure

sweet_shop_project/
├── sweet_shop.py # Business logic (SweetShop class)
├── main.py # CLI program (user menu)
├── test_sweet_shop.py # Unit tests (pytest)
├── requirements.txt # Project dependencies
└── README.md # This file

bash
Copy
Edit

## ▶️ How to Run

### 1. Open Terminal and Go to Project Folder

```bash
cd path/to/sweet_shop_project

2. Install Required Packages

pip install -r requirements.txt
(Installs pytest for testing)

3. Run the CLI App
python main.py

📋 You’ll see a menu like:

======= Sweet Shop Menu =======
1. Add Sweet
2. View Sweets
3. Delete Sweet
4. Purchase Sweet
5. Restock Sweet
6. Search Sweet
7. Sort Sweets
0. Exit
Then follow on-screen instructions.

🧪 Run Tests (TDD)
To run all tests written using pytest:

pytest
✅ All unit tests will run from test_sweet_shop.py.

🛠 Requirements
Python 3.8 or above
pytest (already listed in requirements.txt)
