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
Python 3.10+
pytest (installed via requirements.txt)
VS Code

---
## ▶️ How to Run the Application

### 1. Clone the Repo or Download ZIP
git clone https://github.com/your-username/sweet-shop.git
cd sweet-shop

### 2. Install Dependencies
pip install -r requirements.txt                                                                                                          
This installs pytest (used for testing).

### 3. Run the CLI Program
python main.py

## You’ll see an interactive menu like:

======= Sweet Shop Menu =======
1. Add Sweet
2. View Sweets
3. Delete Sweet
4. Purchase Sweet
5. Restock Sweet
6. Search Sweet
7. Sort Sweets
0. Exit

## 🧪 Run Tests
To verify functionality using TDD tests:
pytest

