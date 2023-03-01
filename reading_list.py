import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog
from database import Database
import os
import shutil
from PIL import ImageTk, Image

class Reading_List():
  def __init__(self, master):
    self.books = tk.Toplevel(master)
    self.books.title('Reading List')
    self.books.iconbitmap("images/reading_list.ico")
    self.books.geometry('650x360')
    self.books.minsize(650, 360)
    self.books.maxsize(650, 360)

    self.ebook_file = None
    self.edit_book_gui = None
    
    global new_logo
    logo= Image.open('images/reading_list.png')
    resized_logo = logo.resize((370, 110))
    new_logo = ImageTk.PhotoImage(resized_logo)
    self.logo_label= tk.Label(self.books, image=new_logo)
    self.logo_label.grid(row=0,column=1, columnspan=2)


    self.add_book_button = tk.Button(self.books, text = 'Add Book', command=self.add_book_to_read_gui, width=15).grid(row=1, column=0, padx=20)
    self.delete_book_button = tk.Button(self.books, text = 'Delete Book',command=self.delete_book, width=15).grid(row=2, column=0)
    self.edit_book_button = tk.Button(self.books, text = 'Edit Book', command=self.open_edit_book, width=15).grid(row=3, column=0)
    self.open_ebook_button = tk.Button(self.books, text = 'Open eBook', command=self.open_ebook, width=15).grid(row=4,column=0)
    self.exit_button = tk.Button(self.books, text = 'Exit', command=self.exit, width=15).grid(row=5, column=0)
    


    self.columns = ('title', 'author', 'genre')
    self.treeview = ttk.Treeview(self.books, columns=self.columns, show='headings')
    self.treeview.heading('title', text= 'Title')
    self.treeview.heading('author', text= 'Author')
    self.treeview.column('author', width=150)
    self.treeview.heading('genre', text= 'Genre')
    self.treeview.column('genre', width=100)
    
    self.treeview.grid(row=1, column=1, rowspan=5, padx=10)


    self.show_books_to_read()

  
  
  def show_books_to_read(self):

    self.treeview.delete(*self.treeview.get_children())
    self.database = Database()
    self.book_list = self.database.show_books_to_read()
    for book in self.book_list:
      self.treeview.insert('', tk.END, text=book[0], values=book[1:], tags=book[0])


  def add_book_to_read_gui(self):
    self.add_book_gui = tk.Toplevel(self.books)
    self.add_book_gui.title('Add Book To Read')
    self.add_book_gui.geometry('310x330')
    self.add_book_gui.minsize(310, 330)
    self.add_book_gui.maxsize(310, 330)
    self.add_book_gui.iconbitmap("images/add_book.ico")

    global add_book_logo
    logo= Image.open('images/add_book.png')
    resized_logo = logo.resize((300, 100))
    add_book_logo = ImageTk.PhotoImage(resized_logo)
    self.logo_label= tk.Label(self.add_book_gui, image=add_book_logo)
    self.logo_label.grid(row=0,column=0, columnspan=2)

    
    self.title_label = tk.Label(self.add_book_gui, text='Title:').grid(row=1, column=0, padx=35, sticky='W')
    self.title_entry = tk.Entry(self.add_book_gui)
    self.title_entry.grid(row=2, column=0)
    
    self.author_label = tk.Label(self.add_book_gui, text='Author:').grid(row=3, column=0, padx=35, sticky='W')
    self.author_entry = tk.Entry(self.add_book_gui)
    self.author_entry.grid(row=4, column=0)
    
    self.genre_label = tk.Label(self.add_book_gui, text='Genre:').grid(row=5, column=0, padx=35, sticky='W')
    self.genre_entry = tk.Entry(self.add_book_gui)
    self.genre_entry.grid(row=6, column=0)

    self.ebook_label = tk.Label(self.add_book_gui, text='Add eBook (PDF): ').grid(row=11, column=0, padx=35, sticky='W')
    self.ebook_entry = tk.Entry(self.add_book_gui)
    self.ebook_entry.insert(0, 'No file chosen')
    self.ebook_entry.config(state='disabled')
    self.ebook_entry.grid(row=12, column=0)
    
    self.choose_file_button_2 = tk.Button(self.add_book_gui, text='Choose file', command=self.choose_ebook).grid(row=12, column= 1, sticky='W')

    self.add_button = tk.Button(self.add_book_gui, text = 'Add Book',command=self.add_book_to_read, width=20).grid(row=13, column=0, pady=10)


  def choose_ebook(self):
    self.ebooks_folder = "eBooks"
    if not os.path.exists(self.ebooks_folder):
      os.makedirs(self.ebooks_folder)

    self.ebook_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if self.ebook_file:
      self.file_name_2 = os.path.basename(self.ebook_file)
      self.ebook_entry.config(state='normal')
      self.ebook_entry.delete(0, tk.END)
      self.ebook_entry.insert(0, self.file_name_2)
      self.ebook_entry.config(state='disabled')
    else:
      self.ebook_entry.config(state='normal')
      self.ebook_entry.delete(0, tk.END)
      self.ebook_entry.insert(0, 'No file chosen')
      self.ebook_entry.config(state='disabled')


  def open_ebook(self):
    selected_item = self.treeview.item(self.treeview.selection())
    self.id = selected_item["text"]
    
    if self.id:
      self.ebooks_folder = "ebooks"
      database = Database()
      file_name = database.get_ebook_to_read_file_name(self.id)
  
      file_path = os.path.join(self.ebooks_folder, file_name)
      os.startfile(file_path)
    else:
      tk.messagebox.showerror('No book selected', 'No book selected!')


  def add_book_to_read(self):
    self.title = self.title_entry.get()
    self.author = self.author_entry.get()

    if self.title and self.author:
      self.title_entry.delete(0, tk.END)
      self.author_entry.delete(0, tk.END)
      
      self.genre = self.genre_entry.get()
      if not self.genre:
        self.genre = 'No genre'
      self.genre_entry.delete(0, tk.END)
  
      self.ebook_file_name = self.ebook_entry.get()
  
      if self.ebook_file:
        shutil.copy(self.ebook_file, self.ebooks_folder)
  
      self.ebook_entry.config(state='normal')
      self.ebook_entry.delete(0, tk.END)
      self.ebook_entry.insert(0, 'No file chosen')
      self.ebook_entry.config(state='disabled')
  
      database = Database()
      database = database.add_book_to_read(self.title, self.author, self.genre, self.ebook_file_name)
  
      self.show_books_to_read()
      
    elif not self.title and not self.author:
      tk.messagebox.showerror('No title and author', 'Please enter book title and author name!')
    elif not self.title:
      tk.messagebox.showerror('No title', 'Please enter book title!')
    elif not self.author:
      tk.messagebox.showerror('No author', 'Please enter author name!')


  
  def delete_book(self):
    self.database = Database()
    
    selected_item = self.treeview.item(self.treeview.selection())
    self.id = selected_item["text"]
    self.values = selected_item['values']
    
    if self.id:
      msg_box = tk.messagebox.askyesno('Delete book', f'Are you sure you want to delete "{self.values[0]}" book?')
      if msg_box:
        self.database.delete_book_to_read(self.id)
        for book in self.treeview.get_children():
          self.treeview.delete(book)
    
        self.show_books_to_read()
      else:
        pass
    else:
      tk.messagebox.showerror('No book selected', 'No book selected!')


  def edit_book(self):
    database = Database()
    selected_item = self.treeview.item(self.treeview.selection())

    self.id = selected_item["text"]
    self.values = selected_item['values']

    if self.values:
      self.edit_book_gui = tk.Toplevel(self.books)
      self.edit_book_gui.title('Edit book')
      self.edit_book_gui.iconbitmap("images/edit_book.ico")
      self.edit_book_gui.geometry('310x350')
      self.edit_book_gui.minsize(310, 350)
      self.edit_book_gui.maxsize(310, 350)
  
      global edit_book_logo
      logo= Image.open('images/edit_book.png')
      resized_logo = logo.resize((300, 120))
      edit_book_logo = ImageTk.PhotoImage(resized_logo)
      self.edit_logo_label= tk.Label(self.edit_book_gui, image=edit_book_logo)
      self.edit_logo_label.grid(row=0,column=0, columnspan=2)

      
      self.title_label = tk.Label(self.edit_book_gui, text='Title:').grid(row=1, column=0, padx=35, sticky='W')
      self.title_entry = tk.Entry(self.edit_book_gui)
      self.title_entry.insert(0, self.values[0])
      self.title_entry.grid(row=2, column=0)
      
      self.author_label = tk.Label(self.edit_book_gui, text='Author:').grid(row=3, column=0, padx=35, sticky='W')
      self.author_entry = tk.Entry(self.edit_book_gui)
      self.author_entry.insert(0, self.values[1])
      self.author_entry.grid(row=4, column=0)
      
      self.genre_label = tk.Label(self.edit_book_gui, text='Genre:').grid(row=5, column=0, padx=35, sticky='W')
      self.genre_entry = tk.Entry(self.edit_book_gui)
      self.genre_entry.insert(0, self.values[2])
      self.genre_entry.grid(row=6, column=0)
      
      self.ebook_label = tk.Label(self.edit_book_gui, text='Add eBook (PDF): ').grid(row=11, column=0, padx=35, sticky='W')
      self.ebook_entry = tk.Entry(self.edit_book_gui)
      self.ebook_entry.insert(0, database.get_ebook_to_read_file_name(self.id))
      self.ebook_entry.config(state='disabled')
      self.ebook_entry.grid(row=12, column=0)
      
  
      self.choose_file_button = tk.Button(self.edit_book_gui, text='Choose file', command=self.choose_ebook).grid(row=12, column= 1, sticky='W')

      
      self.save_button = tk.Button(self.edit_book_gui, text = 'Save Book',command=self.save_changes, width=20).grid(row=13, column=0, pady=10)
      
    else:
      tk.messagebox.showerror('No book selected', 'No book selected!')

  
  def save_changes(self):
    
    self.title = self.title_entry.get()
    
    self.author = self.author_entry.get()
    
    self.genre = self.genre_entry.get()

    self.ebook_file_name = self.ebook_entry.get()

    if self.ebook_file:
      shutil.copy(self.ebook_file, self.ebooks_folder) 
    
    database = Database()
    database = database.edit_book_to_read(self.title, self.author, self.genre, self.ebook_file_name, self.id)

    self.show_books_to_read()
    self.edit_book_gui.destroy()
    

  def open_edit_book(self): 
    if not hasattr(self, 'edit_book') or not self.edit_book_gui:
      self.edit_book()
    elif self.edit_book_gui and self.edit_book_gui.winfo_exists():
      self.edit_book_gui.deiconify()
      self.edit_book_gui.focus_force()
    else:
      self.edit_book()
  
  
  def lift(self):
    self.books.deiconify()
    self.books.focus_force()

  def window_exists(self):
    return self.books.winfo_exists()

  def exit(self):
    self.books.destroy()