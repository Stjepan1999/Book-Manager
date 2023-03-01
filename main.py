import tkinter as tk
from completed_books import Completed_Books
from reading_list import Reading_List
from add_book_gui import Add_Book
from PIL import ImageTk, Image

class BookManagerWindow(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Bookie')
    self.geometry('320x400')
    self.minsize(320, 400)
    self.maxsize(320, 400)

    self.iconbitmap("images/bookie.ico")


    
    global new_logo
    logo= Image.open('images/bookie.png')
    resized_logo = logo.resize((360, 110))
    new_logo = ImageTk.PhotoImage(resized_logo)
    self.logo_label= tk.Label(self, image=new_logo)
    self.logo_label.pack(pady=10)

    

    self.treeview = None
    self.to_read = None
    self.add_book_gui = None

    self.completed_books = tk.Button(self, text="Completed Books", command=self.completed_books, font=('Arial',(11)), height=2, width=25).pack(pady=5)
    self.to_read_books = tk.Button(self, text="Reading List",command=self.reading_list, font=('Arial',(11)), height=2, width=25).pack(pady=5)
    self.add_book = tk.Button(self, text="Add Book", command=self.add_book, font=('Arial',(11)), height=2, width=25).pack(pady=5)
    self.exit_button = tk.Button(self, text='Exit', command=self.exit, font=('Arial',(11)), height=2, width=25).pack(pady=5)

  
  def completed_books(self):
    if not hasattr(self, 'treeview') or not self.treeview:
        self.treeview = Completed_Books(self)
    elif self.treeview and self.treeview.window_exists():
        self.treeview.lift()
    else:
      self.treeview = Completed_Books(self)
  
  def reading_list(self):
    if not hasattr(self, 'to_read') or not self.to_read:
      self.to_read = Reading_List(self)
    elif self.to_read and self.to_read.window_exists():
      self.to_read.lift()
    else:
      self.to_read = Reading_List(self)
 

  def add_book(self):
    if not hasattr(self, 'add_book') or not self.add_book_gui:
      self.add_book_gui = Add_Book(self)
    elif self.add_book_gui and self.add_book_gui.window_exists():
      self.add_book_gui.lift()
    else:
      self.add_book_gui = Add_Book(self)
    
  def exit(self):
    self.destroy()


if __name__ == '__main__':
  root = BookManagerWindow()
  root.mainloop()
