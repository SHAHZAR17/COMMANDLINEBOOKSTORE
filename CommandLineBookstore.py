class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}"

class Bookstore:
    def __init__(self):
        self.books = [
            Book("1984", "George Orwell", 9.99),
            Book("To Kill a Mockingbird", "Harper Lee", 7.99),
            Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99),
            Book("Moby Dick", "Herman Melville", 8.99)
        ]
        self.cart = []
    
    def display_books(self):
        print("\nAvailable Books:")
        for idx, book in enumerate(self.books):
            print(f"{idx + 1}. {book}")

    def add_to_cart(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            self.cart.append(book)
            print(f"Added '{book.title}' to cart.")
        else:
            print("Invalid book index.")

    def display_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\nYour Cart:")
            for idx, book in enumerate(self.cart):
                print(f"{idx + 1}. {book}")

    def checkout(self):
        if not self.cart:
            print("\nYour cart is empty. Add some books before checking out.")
        else:
            total = sum(book.price for book in self.cart)
            print("\nCheckout Summary:")
            self.display_cart()
            print(f"Total: ${total:.2f}")
            self.cart = []  # Empty the cart after checkout


def main():
    bookstore = Bookstore()
    while True:
        print("\nBookstore System")
        print("1. Browse Books")
        print("2. Add Book to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            bookstore.display_books()
        elif choice == '2':
            bookstore.display_books()
            try:
                book_index = int(input("Enter the number of the book to add to cart: ").strip())
                bookstore.add_to_cart(book_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            bookstore.display_cart()
        elif choice == '4':
            bookstore.checkout()
        elif choice == '5':
            print("Exiting bookstore. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()