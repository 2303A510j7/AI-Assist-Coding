#Task-1 (AI-Based Code Completion for Conditional Eligibility Check)
def check_voting_eligibility(age, is_citizen):
    if age >= 18 and is_citizen:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
age = int(input("Enter age: "))
citizenship = input("Are you a citizen? (yes/no): ").lower()
is_citizen = True if citizenship == "yes" else False
result = check_voting_eligibility(age, is_citizen)
print(result)


#Task-2 (AI-Based Code Completion for Loop-Based string processing)
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():  # Check only letters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(string)
print("Vowels:", vowels)
print("Consonants:", consonants)


#Task-3 (AI-Assisted Code Completion Reflection task)
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' added to library.")
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print("-", book)
    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"'{book_name}' removed from library.")
        else:
            print("Book not found in the library.")
library = Library()
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Remove Book")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        name = input("Enter book name: ")
        library.add_book(name)
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        name = input("Enter book name to remove: ")
        library.remove_book(name)
    elif choice == "4":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


#Task-4 (AI-Assisted Code Completion for Class-Based Attendance System)
class Attendance:
    def __init__(self):
        self.students = {}
    def mark_attendance(self, name, status):
        self.students[name] = status
        print(f"Attendance marked for {name}.")

    def display_attendance(self):
        if not self.students:
            print("No attendance records found.")
        else:
            print("\nAttendance Report:")
            for name, status in self.students.items():
                print(f"{name}: {status}")
attendance = Attendance()
while True:
    print("\nAttendance Management System")
    print("1. Mark Attendance")
    print("2. Display Attendance")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        student_name = input("Enter student name: ")
        status = input("Enter status (Present/Absent): ")
        if status.lower() in ["present", "absent"]:
            attendance.mark_attendance(student_name, status.capitalize())
        else:
            print("Invalid status. Please enter Present or Absent.")
    elif choice == "2":
        attendance.display_attendance()
    elif choice == "3":
        print("Exiting Attendance System.")
        break
    else:
        print("Invalid choice. Try again.")


#Task-5 (AI-Based Code Completion for ConditionalMenu Navigation)
balance = 5000
while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        print(f"Your current balance is ₹{balance}")
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid option. Please try again.")

