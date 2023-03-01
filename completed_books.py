import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import ttk
import os
from add_book_gui import Add_Book
from database import Database
from PIL import ImageTk, Image
import shutil


class Completed_Books():
  def __init__(self, master):
    
    self.books = tk.Toplevel(master)
    self.books.title('Completed Books')
    self.books.iconbitmap("images/completed_books.ico")
    self.books.geometry('740x370')
    self.books.minsize(740, 370)
    self.books.maxsize(740, 370)


    self.add_book_gui = None
    self.edit_book_gui = None
    
    
    global new_logo
    logo= Image.open('images/completed_books.png')
    resized_logo = logo.resize((370, 110))
    new_logo = ImageTk.PhotoImage(resized_logo)
    self.logo_label= tk.Label(self.books, image=new_logo)
    self.logo_label.grid(row=0,column=0, columnspan=2)
    


    self.add_book_button = tk.Button(self.books, text = 'Add Book',command=self.add_book, width=15).grid(row=1, column=0, padx=20)
    self.delete_book_button = tk.Button(self.books, text = 'Delete Book', command=self.delete_book, width=15).grid(row=2, column=0)
    self.edit_book_button = tk.Button(self.books, text = 'Edit Book', command=self.open_edit_book, width=15).grid(row=3, column=0)
    self.open_summary_button = tk.Button(self.books, text = 'Open Summary', command=self.open_summary, width=15).grid(row=4, column=0)
    self.open_book_button = tk.Button(self.books, text = 'Open eBook', command=self.open_ebook, width=15).grid(row=5, column=0)
    self.exit_button = tk.Button(self.books, text = 'Exit', command=self.exit, width=15).grid(row=6, column=0)
    


    self.columns = ('title', 'author', 'genre', 'rating')
    self.treeview = ttk.Treeview(self.books, columns=self.columns, show='headings')
    self.treeview.heading('title', text= 'Title')
    self.treeview.heading('author', text= 'Author')
    self.treeview.column('author', width=150)
    self.treeview.heading('genre', text= 'Genre')
    self.treeview.column('genre', width=100)
    self.treeview.heading('rating', text= 'Rating')
    self.treeview.column('rating', width=70)
    
    self.treeview.grid(row=1, column=1, rowspan=6, padx=10)
  
    self.show_books()
  
  def add_book(self):
    if not hasattr(self, 'add_book') or not self.add_book_gui:
      self.add_book_gui = Add_Book(self.books)
    elif self.add_book_gui and self.add_book_gui.window_exists():
      self.add_book_gui.lift()
    else:
      self.add_book_gui = Add_Book(self.books)

    self.add_book_gui.wait_window()
    self.show_books()

  

  def show_books(self):

    self.treeview.delete(*self.treeview.get_children())
    self.database = Database()
    self.book_list = self.database.show_books()
    for book in self.book_list:
      self.treeview.insert('', tk.END, text=book[0], values=book[1:], tags=book[0])

  
  def delete_book(self):
    self.database = Database()

    selected_item = self.treeview.item(self.treeview.selection())
    self.id = selected_item["text"]
    self.values = selected_item['values']
    if self.id:
      msg_box = tk.messagebox.askyesno('Delete book', f'Are you sure you want to delete "{self.values[0]}" book?')
      if msg_box:
        self.database.delete_book(self.id)
        for book in self.treeview.get_children():
          self.treeview.delete(book)
        self.show_books()
      else:
        pass
    else:
      tk.messagebox.showerror('No book selected', 'No book selected!')
      

  def choose_summary(self):
    self.book_summaries_folder = "Books Summaries"
    if not os.path.exists(self.book_summaries_folder):
      os.makedirs(self.book_summaries_folder)

    self.summary_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    if self.summary_file:
      self.file_name = os.path.basename(self.summary_file)
      self.summary_entry.config(state='normal')
      self.summary_entry.delete(0, tk.END)
      self.summary_entry.insert(0, self.file_name)
      self.summary_entry.config(state='disabled')
    else:
      self.summary_entry.config(state='normal')
      self.summary_entry.delete(0, tk.END)
      self.summary_entry.insert(0, 'No file chosen')
      self.summary_entry.config(state='disabled')

    
  
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
  
  def open_edit_book(self): 
    if not hasattr(self, 'edit_book') or not self.edit_book_gui:
      self.edit_book()
    elif self.edit_book_gui and self.edit_book_gui.winfo_exists():
      self.edit_book_gui.deiconify()
      self.edit_book_gui.focus_force()
    else:
      self.edit_book()


  
  def edit_book(self):
    database = Database()
    selected_item = self.treeview.item(self.treeview.selection())
    self.id = selected_item["text"]
    self.values = selected_item['values']

    if self.id:
      self.edit_book_gui = tk.Toplevel(self.books)
      self.edit_book_gui.title('Edit book')
      self.edit_book_gui.geometry('310x450')
      self.edit_book_gui.minsize(310, 450)
      self.edit_book_gui.maxsize(310, 450)
      self.edit_book_gui.iconbitmap("images/edit_book.ico")
  
      global edit_book_logo
      logo= Image.open('images/edit_book.png')
      resized_logo = logo.resize((300, 120))
      edit_book_logo = ImageTk.PhotoImage(resized_logo)
      self.edit_logo_label= tk.Label(self.edit_book_gui, image=edit_book_logo)
      self.edit_logo_label.grid(row=0,column=0, columnspan=2)
    
      self.title_label = tk.Label(self.edit_book_gui, text='Title:').grid(row=1, column=0, padx=(40,0), sticky='W')
      self.title_entry = tk.Entry(self.edit_book_gui)
      self.title_entry.insert(0, self.values[0])
      self.title_entry.grid(row=2, column=0)
      
      self.author_label = tk.Label(self.edit_book_gui, text='Author:').grid(row=3, column=0, padx=(40,0), sticky='W')
      self.author_entry = tk.Entry(self.edit_book_gui)
      self.author_entry.insert(0, self.values[1])
      self.author_entry.grid(row=4, column=0)
      
      self.genre_label = tk.Label(self.edit_book_gui, text='Genre:').grid(row=5, column=0, padx=(40,0), sticky='W')
      self.genre_entry = tk.Entry(self.edit_book_gui)
      self.genre_entry.insert(0, self.values[2])
      self.genre_entry.grid(row=6, column=0)
      
      self.rate_label = tk.Label(self.edit_book_gui, text='Rate:').grid(row=7, column=0, padx=(40,0), sticky='W')
      ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      self.rating_var = tk.StringVar()
      self.rating_var.set(self.values[3])
      self.rating_menu = tk.OptionMenu(self.edit_book_gui, self.rating_var, *ratings)
      self.rating_menu.config(width=6)
      self.rating_menu.grid(row=8, column=0, padx=(40,0), sticky='W')

      self.summary_label = tk.Label(self.edit_book_gui, text='Add Book Summary (PDF): ').grid(row=9, column=0, padx=(40,0), sticky='W')
      self.summary_entry = tk.Entry(self.edit_book_gui)
      self.summary_entry.insert(0, database.get_summary_file_name(self.id))
      self.summary_entry.config(state='disabled')
      self.summary_entry.grid(row=10, column=0)
  
      self.choose_file_button_1 = tk.Button(self.edit_book_gui, text='Choose file', command=self.choose_summary).grid(row=10, column= 1, sticky='W')

  
      
      self.ebook_label = tk.Label(self.edit_book_gui, text='Add eBook (PDF): ').grid(row=11, column=0, padx=(45,0), sticky='W')
      self.ebook_entry = tk.Entry(self.edit_book_gui)
      self.ebook_entry.insert(0, database.get_ebook_file_name(self.id))
      self.ebook_entry.config(state='disabled')
      self.ebook_entry.grid(row=12, column=0)
      
  
      self.choose_file_button_2 = tk.Button(self.edit_book_gui, text='Choose file', command=self.choose_ebook).grid(row=12, column= 1, sticky='W')
      
      
      self.save_button = tk.Button(self.edit_book_gui, text = 'Save Book', command=self.save_changes, width=20).grid(row=13, column=0, pady=10)
    else:
      tk.messagebox.showerror('No book selected', 'No book selected!')


  def save_changes(self):
    self.title = self.title_entry.get()
    
    self.author = self.author_entry.get()
    
    self.genre = self.genre_entry.get()
    
    if self.rating_var.get() != 'Select':
      self.rating = self.rating_var.get()
      self.rating_var.set('Select')
    else:
      self.rating = 'No rating'
    
    self.summary_file_name = self.summary_entry.get()
    self.ebook_file_name = self.ebook_entry.get()

    try:
      if self.summary_file:
        shutil.copy(self.summary_file, self.book_summaries_folder)
  
      if self.ebook_file:
        shutil.copy(self.ebook_file, self.ebooks_folder) 
    except:
      pass
    
    database = Database()
    database = database.edit_book(self.title, self.author, self.genre, self.rating, self.summary_file_name, self.ebook_file_name, self.id)

    self.show_books()
    self.edit_book_gui.destroy()

  
  def open_summary(self):
    selected_item = self.treeview.item(self.treeview.selection())
    self.id = selected_item["text"]

    database = Database()

    try:
      file_name = database.get_summary_file_name(self.id)

      if self.id and file_name != 'No file chosen':
        self.ebooks_folder = "book_summaries"
        file_path = os.path.join(self.ebooks_folder, file_name)
        os.startfile(file_path)
      elif file_name == 'No file chosen':
        tk.messagebox.showerror("Can't open summary", 'No book summary found!')
  
    except:
      tk.messagebox.showerror('No book selected', 'No book selected!')

  
  def open_ebook(self):
    selected_item = self.treeview.item(self.treeview.selection())
    self.id = selected_item["text"]
    database = Database()

    try: 
      file_name = database.get_ebook_file_name(self.id)

      if self.id and file_name != 'No file chosen':
        self.ebooks_folder = "ebooks"
        file_path = os.path.join(self.ebooks_folder, file_name)
        os.startfile(file_path)
      elif file_name == 'No file chosen':
          tk.messagebox.showerror("Can't open ebook", 'No ebook found!')

    except:
      tk.messagebox.showerror('No book selected', 'No book selected!')


  
      
  
  def lift(self):
    self.books.deiconify()
    self.books.focus_force()

  def window_exists(self):
    return self.books.winfo_exists()
    
    
    
  def exit(self):
    self.books.destroy()
    

