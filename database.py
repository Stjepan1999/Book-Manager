import sqlite3

class Database:
  def __init__(self):
    self.conn = sqlite3.connect('books.db')
    self.cur = self.conn.cursor()
    self.cur.execute('''CREATE TABLE IF NOT EXISTS completed_books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            genre TEXT,
            rating INTEGER,
            book_summary_file TEXT,
            ebook_file TEXT)''')

    self.cur.execute('''CREATE TABLE IF NOT EXISTS books_to_read(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            genre TEXT,
            ebook_file TEXT)''')

    self.conn.commit()
    self.show_books()


  def add_book(self, title, author, genre, rating, book_summary_file, ebook_file):
    
    self.cur.execute('INSERT INTO completed_books (title, author, genre, rating, book_summary_file, ebook_file) VALUES(:title, :author, :genre, :rating, :book_summary_file, :ebook_file)',
                {
                  'title':title,
                  'author':author,
                  'genre':genre,
                  'rating':rating,
                  'book_summary_file':book_summary_file,
                  'ebook_file':ebook_file
                })

    self.conn.commit()
    print(f'Book "{title}" successfully added to database!')

  
  def add_book_to_read(self, title, author, genre, ebook_file):

    self.cur.execute('INSERT INTO books_to_read (title, author, genre, ebook_file) VALUES(:title, :author, :genre, :ebook_file)',
                {
                  'title':title,
                  'author':author,
                  'genre':genre,
                  'ebook_file':ebook_file
                })
    
    self.conn.commit()
    print(f'Book "{title}" successfully added to database!')
    

  def show_books(self):

    self.cur.execute('SELECT id, title, author, genre, rating FROM completed_books')
    self.completed_books = []
    for book in self.cur:
      self.completed_books.append(book)

    return self.completed_books


  def show_books_to_read(self):

    self.cur.execute('SELECT id, title, author, genre FROM books_to_read')
    self.books_to_read = []
    for book in self.cur:
      self.books_to_read.append(book)

    return self.books_to_read

    
  def delete_book(self, id):
    
    self.cur.execute('DELETE FROM completed_books WHERE id = ?', (id,))
    self.conn.commit()
    
    self.show_books()
    print(f"Book ID '{id}' deleted successfully!")
  
  def delete_book_to_read(self, id):
    
    self.cur.execute('DELETE FROM books_to_read WHERE id = ?', (id,))
    self.conn.commit()
    
    self.show_books_to_read()
    print(f"Book ID '{id}' deleted successfully!")

  def edit_book(self, title, author, genre, rating, book_summary_file, ebook_file, id):

    self.cur.execute('UPDATE completed_books SET title=?, author=?, genre=?, rating=? , book_summary_file=?, ebook_file=? WHERE id=?',(title, author, genre, rating, book_summary_file, ebook_file, id))
    self.conn.commit()

    print(f"Book '{title}' updated successfully!")

  def edit_book_to_read(self, title, author, genre, ebook_file, id):

    self.cur.execute('UPDATE books_to_read SET title=?, author=?, genre=? , ebook_file=? WHERE id=?',(title, author, genre, ebook_file, id))
    self.conn.commit()

    print(f'Book "{title}" updated successfully!')


    
  def get_summary_file_name(self, id):
    self.cur.execute('SELECT book_summary_file FROM completed_books WHERE id=?', (id,))
    return self.cur.fetchone()[0]

  
  def get_ebook_file_name(self, id):
    self.cur.execute('SELECT ebook_file FROM completed_books WHERE id=?', (id,))
    return self.cur.fetchone()[0]

  
  def get_ebook_to_read_file_name(self, id):
    self.cur.execute('SELECT ebook_file FROM books_to_read WHERE id=?', (id,))
    return self.cur.fetchone()[0]



if __name__ == '__main__':
  database = Database()
    