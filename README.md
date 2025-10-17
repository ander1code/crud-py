# 🐍 CrudPy

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&color=yellow)
![SQLite3](https://img.shields.io/badge/SQLite3-003B57?logo=sqlite&logoColor=white&color=blue)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-black?logo=linux&logoColor=yellow)
![Last Commit](https://img.shields.io/github/last-commit/ander1code/crud-py?color=yellow&logo=github)

---

## 📄 1. Description

**CrudPy** is a lightweight **command-line CRUD prototype** built entirely in **pure Python**, using **SQLite3** as its database engine. It is designed for managing **natural person records** (individuals), with a focus on **simplicity**, **data integrity**, and **modular architecture**.

This project is ideal for learning or prototyping database-driven applications without relying on external frameworks or GUIs.

---

## 🚀 2. Features

- ✅ **Transactional Support** — Ensures data consistency and rollback on failure  
- ✅ **Encapsulated Models** — Object-oriented design with inheritance and property-based access  
- ✅ **Modular Architecture** — Clean separation of concerns using services, models, and controllers  
- ✅ **Validation Layer** — Input validation for name, email, salary, birthday, and gender  
- ✅ **Singleton Pattern** — Applied to database connection and CRUD service for efficiency  

### 🔧 Core Functionalities

- **Register Person** — Add new records to the database  
- **Edit Person** — Update existing records with optional field preservation  
- **Delete Person** — Remove records by ID  
- **Search by Name** — Retrieve records using partial name matches  
- **Search by ID** — Retrieve a specific record using its unique identifier  

---

## 🗂️ 3. Project Structure

```text
crud-py/
│
├── database/              # SQLite3 database file
│   └── database.sqlite3
│
├── models/                # Domain models with encapsulated attributes
│   └── models.py          # Contains Person and NaturalPerson classes with inheritance
│
├── services/              # Business logic and persistence layer
│   └── connection.py      # Singleton-based database connection factory
│   └── crud.py            # CRUD operations for natural person records
│
├── utils/                 # Input validation and helper functions
│   └── validators.py      # Validation logic for name, email, salary, birthday, gender
│
├── controllers/           # Application flow and user interaction
│   └── controller.py      # Handles user commands and orchestrates service calls
│
├── main.py                # Entry point of the application (located at the root)
│
└── README.md              # Project documentation

---

## 🛠️ 4. Tools and Technologies Used

- **Programming Language:** Python 3.13.7  
- **Database Engine:** SQLite3  
- **Database Management Tool:** HeidiSQL v12.12.0.7122  
- **Platform Compatibility:** Windows & Linux  
- **IDE Recommendation:** Visual Studio Code or PyCharm  

---

## 📌 5. Requirements

- Python 3.10 or higher  
- No external dependencies required (uses only Python standard library)  

---

## 📥 6. How to Run

```bash
# Clone the repository
git clone https://github.com/ander1code/crud-py.git
cd crud-py

# Run the main controller
python main.py


