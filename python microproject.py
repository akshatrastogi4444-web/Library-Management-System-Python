import datetime

class Library:
    def __init__(self):
        # Pre-loading 9 books with different status
        self.books = {
            101: {"title": "Python Basics", "author": "John Smith", "status": "Available", "borrower": None, "due_date": None, "issued_by": None},
            102: {"title": "Data Science", "author": "Jane Doe", "status": "Issued", "borrower": "Akshat", "due_date": datetime.date.today() - datetime.timedelta(days=10), "issued_by": "Admin"},
            103: {"title": "AI Ethics", "author": "Alan Turing", "status": "Available", "borrower": None, "due_date": None, "issued_by": None},
            104: {"title": "Machine Learning", "author": "Andrew Ng", "status": "Issued", "borrower": "Bhuvan", "due_date": datetime.date.today() - datetime.timedelta(days=5), "issued_by": "Staff_01"},
            105: {"title": "Web Dev 101", "author": "Angela Yu", "status": "Available", "borrower": None, "due_date": None, "issued_by": None},
            106: {"title": "Cyber Security", "author": "Kevin Mitnick", "status": "Available", "borrower": None, "due_date": None, "issued_by": None},
            107: {"title": "Deep Learning", "author": "Ian Goodfellow", "status": "Issued", "borrower": "Riddhi", "due_date": datetime.date.today() - datetime.timedelta(days=12), "issued_by": "Admin"},
            108: {"title": "SQL Masters", "author": "Ben Forta", "status": "Available", "borrower": None, "due_date": None, "issued_by": None},
            109: {"title": "Cloud Computing", "author": "James Bond", "status": "Available", "borrower": None, "due_date": None, "issued_by": None}
        }

    def display_books(self):
        print(f"\n{'ID':<5} {'Title':<18} {'Author':<15} {'Status':<10} {'Borrower':<10} {'Librarian':<10}")
        print("-" * 80)
        for bid, info in self.books.items():
            borr = info['borrower'] if info['borrower'] else "-"
            lib = info['issued_by'] if info['issued_by'] else "-"
            print(f"{bid:<5} {info['title'][:17]:<18} {info['author'][:14]:<15} {info['status']:<10} {borr:<10} {lib:<10}")

    def add_book(self):
        try:
            bid = int(input("Enter New Book ID: "))
            if bid in self.books:
                print("Error: ID already exists!")
                return
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            self.books[bid] = {"title": title, "author": author, "status": "Available", "borrower": None, "due_date": None, "issued_by": None}
            print(f"Successfully added '{title}' to the library.")
        except ValueError:
            print("Invalid input. ID must be a number.")

    def issue_book(self):
        try:
            bid = int(input("Enter Book ID to issue: "))
            if bid in self.books and self.books[bid]['status'] == "Available":
                borrower = input("Enter Borrower Name: ")
                librarian = input("Enter Librarian Name (You): ")
                self.books[bid].update({
                    "status": "Issued",
                    "borrower": borrower,
                    "issued_by": librarian,
                    "due_date": datetime.date.today()
                })
                print(f"Book issued to {borrower} by {librarian}.")
            else:
                print("Book not available or ID wrong.")
        except ValueError:
            print("Invalid ID.")

    def return_book(self):
        try:
            bid = int(input("Enter Book ID to return: "))
            if bid in self.books and self.books[bid]['status'] == "Issued":
                today = datetime.date.today()
                due = self.books[bid]['due_date']
                
                fine = 0
                days_late = (today - due).days
                if days_late > 0:
                    fine = days_late * 5
                
                print(f"\n--- RETURN RECEIPT ---")
                print(f"Book: {self.books[bid]['title']}")
                print(f"Borrower: {self.books[bid]['borrower']}")
                print(f"Issued By: {self.books[bid]['issued_by']}")
                print(f"Fine Calculated: Rs. {fine}")
                print(f"----------------------")
                
                self.books[bid].update({"status": "Available", "borrower": None, "due_date": None, "issued_by": None})
            else:
                print("This book was not issued.")
        except ValueError:
            print("Invalid ID.")

def main():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. View Inventory\n2. Add New Book\n3. Issue Book\n4. Return Book (Check Fine)\n5. Exit")
        choice = input("Action: ")
        if choice == '1': lib.display_books()
        elif choice == '2': lib.add_book()
        elif choice == '3': lib.issue_book()
        elif choice == '4': lib.return_book()
        elif choice == '5': break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()
