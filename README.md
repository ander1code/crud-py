# CrudPy

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&color=yellow)

![SQLite3](https://img.shields.io/badge/SQLite3-003B57?logo=sqlite&logoColor=white&color=blue)

![Platform: Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-black?logo=linux&logoColor=yellow)

![Last Commit](https://img.shields.io/github/last-commit/ander1code/crud-py?color=yellow&logo=github) 


## 1. Description
A **prototype CRUD application** developed in **pure Python**, utilizing an **SQLite3 database** for individual registration. This lightweight project focuses on simplicity, functionality, and transactional integrity.

## 2. Features
- **Transactional Support:** Ensures data consistency and reliability during operations.
- **Core Functions:**
  - **Registration:** Add new records to the database.
  - **Search by Name:** Retrieve records based on the name field.
  - **Search by Code:** Retrieve records using the unique code field.

## 3. Project Structure

### 3.1. CrudPy Folder (Project's Source)
- Developed using **Visual Studio with PTVS 2.2**.
- Contains the following key components:
  - **Classes**: Encapsulated logic for CRUD operations.
  - **SQLite3 DLLs**: Required binary files for database interaction.
  - **Database File:** `db.sqlite3`, used for storing project data.

### 3.2. BIN Folder (Binary Files)
- Contains essential files for execution:
  - **Python Class Files:** `.py` files with project logic.
  - **Libraries:** `.dll` files for database connectivity.
  - **Database File:** `db.sqlite3` (used for data storage).
  - **Executable File:** `crudpy.exe`, which invokes the execution of the `main.py` file in a Python runtime environment for Windows.

## 4. Tools and Technologies Used
- **Programming Language:** Python 3
- **Database:** SQLite3
- **IDE:** Visual Studio 2013 with **Python Tools for Visual Studio (PTVS 2.2)**
- **Database Management Tool:** SQLiteStudio v3.1.1

---
