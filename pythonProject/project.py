from multiprocessing.sharedctypes import Value

exit = False
found = False
books = {"Miguel de Cervantes" : ["Don Quixote"], "Charles Dickens" : ["A Tale of Two Cities"], "J.R.R Tolkien" : ["The Lord of the Rings", "The Hobbit"], "Antoine de Saint-Exupery" : ["The Little Prince"]}

while not exit:
    print("""
    1. Display available books by authors
    2. Find books by author name 
    3. Find authors by book name
    4. Add a book to our systems
    5. Remove an author from our system
    6. Remove a book from our system
    7. Exit
    """)

    try:
        option = int(input("Enter an option number: "))
    except ValueError:
            print("\nERROR: The option entered has to be a number!")
    else:
        if option == 1:
            for key, value in books.items():
                print(f"{key} : {value}")

        elif option == 2:
            author = str(input("Enter the authors name: "))
            if author in books.keys():
                print(sorted(books[author]))
            else:
                print(f"\n{author} is not in our database, sorry.")
        
        elif option == 3:
            title = input("Enter the books name: ")
            for key, value in books.items():
                if title in value:
                    print(f"\nThe author of {title} is {key}.")
                    found = True

            if not found:
                print(f"\nThe book {title} is not in our system.")
            
        elif option == 4:
            author = input("Enter the authors name: ")
            title = input("Enter the books name: ")
            books[author] = [title]
            print(f"\nThe book {title}, by {author} has been added to the system.")

        elif option == 5:
            author = str(input("Enter the authors name: "))
            if author in books.keys():
                del books[author]
                print(f"\n{author} has been removed from our system.")
                found = True
            
            if not found:
                print(f"\n{author} is not on our system and therefore cannot be removed.")

        elif option == 6:
            title = input("Enter the books name: ")
            for value in books.values():
                if title in value:
                    value.remove(title)
                    print(f"\n{title} has been removed from our system.")
                    found = True
            
            if not found:
                print(f"\n{title} is not on our system and therefore cannot be removed")
            
        elif option == 7:
            exit = True

        found = False