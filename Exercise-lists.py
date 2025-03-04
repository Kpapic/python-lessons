favorite_books = ["boook1", "book2", "book3", "book4", "book5"]
print(favorite_books)

#Adding another book to the list and remove book from index position 2nd. If I know the name of the book I can use .remove("Book_name")
favorite_books.append("book6")
favorite_books.pop(1)
print("Lista izgleda sada ovako ", favorite_books)

#Print all books
for book in favorite_books:
    print(book)