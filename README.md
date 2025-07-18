# Sweet Shop Management System

A simple sweet shop management system implemented in Python with a Flask frontend.  
This project allows users to add, delete, search, sort, purchase, and restock sweets via a web interface.

---

![SweetShop Demo](static/Images/Home-page.png)


## Features

- Add new sweets with id, name, category, price, and stock quantity.
- Delete sweets by ID.
- Search sweets by ID, name, or category.
- Sort sweets by price (ascending or descending).
- Purchase sweets, which reduces stock if enough quantity is available.
- Restock sweets by adding to current stock.
- Simple, clean web UI using Flask and Bootstrap.

---

## Setup and Installation

### Requirements

- Python 3.6+
- Flask

### Install dependencies

```bash
pip install flask

## Running the Project

1. Clone the repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Run the Flask app:

python app.py

3. Open your webpage and navigate to:

http://127.0.0.1:5000/
