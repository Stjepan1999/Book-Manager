import tkinter as tk
import tkinter.filedialog as filedialog
import os
from database import Database
import shutil
from PIL import ImageTk, Image


class Add_Book():
  def __init__(self, master):
    self.master = master

    self.add_book_gui = tk.Toplevel(master)
    self.add_book_gui.title('Add book')
    self.add_book_gui.geometry('310x430')
    self.add_book_gui.minsize(310, 430)
    self.add_book_gui.maxsize(310, 430)
    self.add_book_gui.iconbitmap("images/add_book.ico")

    global add_book_logo
    logo= Image.open('images/add_book.png')
    resized_logo = logo.resize((300, 100))
    add_book_logo = ImageTk.PhotoImage(resized_logo)
    self.logo_label= tk.Label(self.add_book_gui, image=add_book_logo)
    self.logo_label.grid(row=0,column=0, columnspan=2)

    self.add_book_executed = False
    self.summary_file = False
    self.ebook_file = False

    
    self.title_label = tk.Label(self.add_book_gui, text='Title:').grid(row=1, column=0, padx=(35, 0), sticky='W')
    self.title_entry = tk.Entry(self.add_book_gui)
    self.title_entry.grid(row=2, column=0)
    
    self.author_label = tk.Label(self.add_book_gui, text='Author:').grid(row=3, column=0, padx=(35, 0), sticky='W')
    self.author_entry = tk.Entry(self.add_book_gui)
    self.author_entry.grid(row=4, column=0)
    
    self.genre_label = tk.Label(self.add_book_gui, text='Genre:').grid(row=5, column=0, padx=(35, 0), sticky='W')
    self.genre_entry = tk.Entry(self.add_book_gui)
    self.genre_entry.grid(row=6, column=0)
    
    self.rate_label = tk.Label(self.add_book_gui, text='Rate:').grid(row=7, column=0, padx=(35, 0), sticky='W')
    ratings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.rating_var = tk.StringVar(value='Select')
    self.rating_menu = tk.OptionMenu(self.add_book_gui, self.rating_var, *ratings)
    self.rating_menu.config(width=5)
    self.rating_menu.grid(row=8, column=0, padx=(35, 0), sticky='W')

    
    self.summary_label = tk.Label(self.add_book_gui, text='Book Summary (PDF): ').grid(row=9, column=0, padx=(35, 0), sticky='W')
    self.summary_entry = tk.Entry(self.add_book_gui)
    self.summary_entry.insert(0, 'No file chosen')
    self.summary_entry.config(state='disabled')
    self.summary_entry.grid(row=10, column=0)

    
    self.choose_file_button_1 = tk.Button(self.add_book_gui, text='Choose file', command=self.choose_summary).grid(row=10, column= 1, sticky='W')

    
    self.ebook_label = tk.Label(self.add_book_gui, text='eBook (PDF): ').grid(row=11, column=0, padx=(35, 0) , sticky='W')
    self.ebook_entry = tk.Entry(self.add_book_gui)
    self.ebook_entry.insert(0, 'No file chosen')
    self.ebook_entry.config(state='disabled')
    self.ebook_entry.grid(row=12, column=0)
    

    self.choose_file_button_2 = tk.Button(self.add_book_gui, text='Choose file', command=self.choose_ebook).grid(row=12, column= 1, sticky='W')
    


    self.add_button = tk.Button(self.add_book_gui, text = 'Add Book',command=self.add_book, width=20).grid(row=13, column=0, pady=10)

  
  
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

    
    
  
  def add_book(self):
  
    self.title = self.title_entry.get()
    self.author = self.author_entry.get()
    
    
    if self.title and self.author:
      self.title_entry.delete(0, tk.END)
      self.author_entry.delete(0, tk.END)

      
      self.genre = self.genre_entry.get()
      if not self.genre:
        self.genre = 'No genre'
      self.genre_entry.delete(0, tk.END)
  
      if self.rating_var.get() != 'Select':
        self.rating = self.rating_var.get()
        self.rating_var.set('Select')
      else:
        self.rating = 'No rating'
      
      self.summary_file_name = self.summary_entry.get()
      self.ebook_file_name = self.ebook_entry.get()

      
      if self.summary_file: 
        shutil.copy(self.summary_file, self.book_summaries_folder)
  
      if self.ebook_file:
        shutil.copy(self.ebook_file, self.ebooks_folder)
  
      
      self.summary_entry.config(state='normal')
      self.summary_entry.delete(0, tk.END)
      self.summary_entry.insert(0, 'No file chosen')
      self.summary_entry.config(state='disabled')
  
      
      self.ebook_entry.config(state='normal')
      self.ebook_entry.delete(0, tk.END)
      self.ebook_entry.insert(0, 'No file chosen')
      self.ebook_entry.config(state='disabled')
  
      database = Database()
      database = database.add_book(self.title, self.author, self.genre, self.rating, self.summary_file_name, self.ebook_file_name)


      self.add_book_executed = True
      self.add_book_gui.destroy()
    elif not self.title and not self.author:
      tk.messagebox.showerror('No title and author', 'Please enter book title and author name!')
    elif not self.title:
      tk.messagebox.showerror('No title', 'Please enter book title!')
    elif not self.author:
      tk.messagebox.showerror('No author', 'Please enter author name!')

    
  def wait_window(self):
    self.add_book_gui.wait_window()


  def lift(self):
    self.add_book_gui.deiconify()
    self.add_book_gui.focus_force()

  def window_exists(self):
    return self.add_book_gui.winfo_exists()
    


    

    

    

    

    
    