# **Book Manager**
The Book Manager is a Python application that helps you store completed books and manage your reading list. With Book Manager, you can add PDF files for book summaries and e-books, rate books, and edit saved books. All data is stored in a local database and the application creates new folders in your directory for book summaries and e-books.


# **Requirements**

- Python 3.x
- Tkinter
- SQLite3
- Pillow


Note that Book Manager has only been tested on Windows, and may not work correctly on other operating systems.


# **Installation**

1.	Clone the repository to your local machine:

`$ git clone https://github.com/Stjepan1999/Book-Manager`

2.	Install the required Python library:

`$ pip install Pillow`


3.	Run the Book Manager application:

`$ python main.py`


# **Usage**
When you launch the Book Manager application, you will see the main window with three buttons: 'Completed books', 'Reading list' and 'Add Book'

![Book Manager GUI](https://i.imgur.com/dKxx30d.png)

## Completed Books
The "Books" tab shows a list of all completed books. You can add new books by clicking the "Add Book" button, and you can edit existing books by selecting them from the list and clicking the "Edit Book" button. To delete a book, select it from the list and click the "Delete Book" button. You can open book summary pdf or ebook pdf with buttons.

![Completed Books GUI](https://i.imgur.com/AYYqYba.png)

## Reading List
The "Reading List" tab shows a list of books that you want to read in the future. You can add new books by clicking the "Add Book" button, and you can edit existing books by selecting them from the list and clicking the "Edit Book" button. To delete a book, select it from the list and click the "Delete Book" button. You can open ebook file by clicking on „Open eBook“ button.

![Reading List GUI](https://i.imgur.com/qiU76v8.png)


## Adding a Book
When you click the "Add Book" button, a new window will appear where you can enter the details of the book. You can enter the book title, author, rating, and upload PDF files for the book summary and e-book. When you click the "Save" button, the book will be added to the Books or Reading List tab depending on which one you were on when you clicked the "Add Book" button.

![Add Book GUI](https://i.imgur.com/ppabspC.png)

## Editing a Book
When you click the "Edit Book" button, a new window will appear where you can edit the details of the selected book. You can change the book title, author, rating, and upload new PDF files for the book summary and e-book. When you click the "Save" button, the book will be updated with the new details.

![Edit Book GUI](https://i.imgur.com/GBinfYP.png)

# **License**

Desktop Assistant is licensed under the MIT License. See the LICENSE file for more information.
