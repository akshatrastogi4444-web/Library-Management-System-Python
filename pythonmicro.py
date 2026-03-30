import datetime

class Library:
    def __init__(self):
        self.books = {
            101: {"title": "Python Basics", "author": "John Smith", "status": "Available", "borrower": None, "due_date": None},
            102: {"title": "Data Science", "author": "Jane Doe", "status": "Available", "borrower": None, "due_date": None}
        }

    def display_books(self):
        print(f"\n{'ID':<6} {'Title':<20} {'Author':<20} {'Status':<12}")
        print("-" * 60)
        for bid, info in self.books.items():
            print(f"{bid:<6} {info['title'][:18]:<20} {info['author'][:18]:<20} {info['status']:<12}")

    def issue_book(self):
        try:
            bid = int(input("Enter Book ID: "))
            if bid in self.books and self.books[bid]['status'] == "Available":
                name = input("Enter Borrower Name: ")
                self.books[bid]['status'] = "Issued"
                self.books[bid]['borrower'] = name
                
                # FOR TESTING: Set due date to 1 day ago so you see a fine immediately
                self.books[bid]['due_date'] = datetime.date.today() - datetime.timedelta(days=1)
                
                print(f"Book issued. (Due date set to yesterday for fine testing)")
            else:
                print("Book not available.")
        except ValueError:
            print("Invalid ID.")

    def return_book(self):
        try:
            bid = int(input("Enter Book ID: "))
            if bid in self.books and self.books[bid]['status'] == "Issued":
                today = datetime.date.today()
                due = self.books[bid]['due_date']
                fine = 0
                
                if today > due:
                    days_late = (today - due).days
                    fine = days_late * 5  # 5 rupees per day
                
                self.books[bid]['status'] = "Available"
                print(f"Book Returned! Days Late: {max(0, (today-due).days)}")
                print(f"Total Fine to Pay: Rs. {fine}")
            else:
                print("Book was not issued.")
        except ValueError:
            print("Invalid ID.")

def main():
    lib = Library()
    while True:
        print("\n1. Display | 2. Issue | 3. Return | 4. Exit")
        choice = input("Select: ")
        if choice == '1': lib.display_books()
        elif choice == '2': lib.issue_book()
        elif choice == '3': lib.return_book()
        elif choice == '4': break

if __name__ == "__main__":
    main()