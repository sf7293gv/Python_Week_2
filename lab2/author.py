class Author:
    def __init__(self, name): #initiate the Author class with...
        self.name = name
        self.books = []
    
    # This Author method will appened books to the empty books list
    def publish(self, book_title): 
        counter = 0 # counter for checking if the book is duplicate

        for b in self.books: # loop over books published by the author
            # I will check if the book to be added is already published. Ignoring the case.
            if book_title.lower() == b.lower(): 
                print(f'{book_title} is already published by the author.') # If book was found, print this, and add 1 to the counter
                counter = counter + 1
        else:
            if counter == 0: # if the counter is 0, that means that the book was not published before.
                self.books.append(book_title) # add the book to the list
                counter = 0 # make sure counter is 0
 
    def __str__(self): # This method will return a string that explains the Author's details.
         # If list contains books, join the books together, and assign to list.
        if len(self.books) > 0:
            book_list = ', '.join(self.books)
        else: # if not, assign this value instead
            book_list = 'No books.'
        # or
        # book_list = ', '.join(self.books) or 'No books.' 
        return f'Author: {self.name}, books: {book_list}'
        
def main(): # Store authors in the Author class using the main mehod
    
    Mohammad = Author('Mohammad')
    Mohammad.publish('Book_one')
    Mohammad.publish('Book_2')
    

    clara = Author('Clara')
    print(Mohammad)
    print(clara)
    Mohammad.publish('Book_one')
    Mohammad.publish('Book_2')
    Mohammad.publish('Book_one')
    print(Mohammad)



    

if __name__ == '__main__':
    main() # Call main method to store in the Author Class