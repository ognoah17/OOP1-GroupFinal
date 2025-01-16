# **Library Management System**

**Developers:** Noah, Steven, Rubal  
**Date:** April 20, 2024  

---

## **Overview**
The Library Management System is a Python-based application for managing books, allowing users and librarians to handle catalog operations such as borrowing, returning, and organizing books.

---

## **Features**

- **User Functions:**
  - Search books by title, author, ISBN, or genre.
  - View all books and their availability.
  - Borrow and return books with real-time status updates.

- **Librarian Functions:**
  - Add or remove books from the catalog.
  - Access full inventory management with secret code `2130`.

- **System Features:**
  - Persistent storage using `library.txt`.
  - Input validation for data like ISBN and genre.

---

## **How to Run**

1. Ensure the `library.txt` file is in the same directory as the program, formatted as:
   ```plaintext
   ISBN,Title,Author,GenreCode,Availability
   ```
   Example:
   ```plaintext
   978-0060000000,To Kill a Mockingbird,Harper Lee,3,True
   978-0140000000,Pride and Prejudice,Jane Austen,0,False
   ```

2. Run the script using Python:
   ```bash
   python lms.py
   ```

3. Follow the terminal prompts:
   - Enter `2130` to access Librarian Mode.

---

## **Menu Options**

### **Main Menu**
1. Search for books
2. Show all books
3. Borrow a book
4. Return a book
0. Exit the system
2130. Librarian Mode

### **Librarian Menu**
1. Search for books
2. Borrow a book
3. Return a book
4. Add a book
5. Remove a book
6. Show all books
7. Print catalog
0. Exit the system

---

## **File Format**

### **Data Example:**
```plaintext
978-0060000000,To Kill a Mockingbird,Harper Lee,3,True
978-0140000000,Pride and Prejudice,Jane Austen,0,False
```

### **Genre Codes:**
| Code | Genre               |
|------|---------------------|
| 0    | Romance             |
| 1    | Mystery             |
| 2    | Science Fiction     |
| 3    | Thriller            |
| 4    | Young Adult         |
| 5    | Children's Fiction  |
| 6    | Self-help           |
| 7    | Fantasy             |
| 8    | Historical Fiction  |
| 9    | Poetry              |

### **Availability:**
- **True**: Available
- **False**: Borrowed

---

## **Class Structure**

### **Book Class**

- **Attributes:** ISBN, title, author, genre code, availability.
- **Key Methods:**
  - `borrow_it()`: Mark as borrowed.
  - `return_it()`: Mark as available.
  - `get_*()`: Access book details.

---

## **Contributing**
Contributions are welcome! Open issues or submit pull requests.

---

## **License**
This project is licensed under the MIT License.

