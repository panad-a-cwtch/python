books = {"Miguel de Cervantes" : ["Don Quixote"], "Charles Dickens" : ["A Tale of Two Cities"], "J.R.R Tolkien" : ["The Lord of the Rings", "The Hobbit"], "Antoine de Saint-Exupery" : ["The Little Prince"]}

# author = input("Enter an author: ")
# bookKeys = books.keys()
# for bookKeys in (books):
#     if author == bookKeys:
#         print(sorted(books[author]))

author = input("Enter an author: ")
if author in books.keys():
     print(sorted(books[author]))
else:
    print(f"{author} is not in our database, sorry.")