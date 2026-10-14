class Book:
    def __init__(self,title,author,available):
        self.title=title
        self.author=author
        self.available=available

    def __str__(self):
        return f"{self.title}:{self.author}"

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self):
        user=input("Enter book title:")
        for book in self.books:
            if user==book.title:
                self.books.remove(book)
                print("Book removed.")
                break
            else:
                print("Book not found.")


    def search_book(self):
        user=input("Enter book title:")
        for book in self.books:
            if user==book.title:
                print("Found")
                break
            else:
                print("Not found.")

    def issue_book(self):
        user=input("Enter book title:")
        for book in self.books:
            if user==book.title:
                if book.available==True:
                    book.availble=False
                    print("Book issued.")
                    break
                else:
                    print("Book is not available.")
                    break
            else:
                print("Book not found.")

    def return_book(self):
        user=input("Enter book title:")
        for book in self.books:
            if user==book.title:
                if book.available==False:
                    book.available=True
                    print("Book returned.")
                    break
                else:
                    print("Book available.")
                    break
            else:
                print("Book not found.")

    def display_book(self):
        for book in self.books:
            print(book,"-","Available" if book.available else "Issued")
               

    def save_books(self):
        with open("book.txt","w") as file:
            for book in self.books:
                file.write(f"{book.title}:{book.author}:{book.available}\n")

    def load_books(self):
        try:
            with open("book.txt","r") as file:
                data=file.readlines()
                for line in data:
                    line=line.strip()
                    parts=line.split(":")

                    if parts[2]=="True":
                        available=True
                    else:
                        available=False

                        b=Book(parts[0],parts[1],available)
                        self.books.append(b)

        except FileNotFoundError:
            print("No previous book file found")
    
library=Library()
library.load_books()

running=True

while running:

    print("\n1.Add books")
    print("2.Remove books")
    print("3.Search books")
    print("4.Issue books")
    print("5.Return books")
    print("6.Display books")
    print("7.Save books")
    print("8.Exit")

    try:
        user=int(input("Enter a number:"))

        if user==1:
            title=input("Enter book name:")
            author=input("Enter author name:")

            b1=Book(title,author,True)
            library.add_book(b1)

        elif user==2:
            library.remove_book()

        elif user==3:
            library.search_book()

        elif user==4:
            library.issue_book()

        elif user==5:
            library.return_book()

        elif user==6:
            print("Option 6 selected.")
            library.display_book()

        elif user==7:
            print("Option 7 selected.")
            library.save_books()
        
        elif user==8:
            running=False
            print("Thankyou")
            
        else:
            print("Invalid number")

    except ValueError:
        print("Please enter only numbers.")

    




