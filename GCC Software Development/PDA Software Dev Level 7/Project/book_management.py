# Import necessary libraries
from array import array
import csv
import json


# Function to add a book to the collection
def add_book(books, title, author, genre, year, price):
    # Create a dictionary to store book details
    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "price": price
    }
    # Append the book to the books list
    books.append(book)
    # Save the updated book list to the JSON file
    save_books(books)


# Function to search for a book by title
def search_book(books, title):
    # Loop through the list of books to find the matching title
    for book in books:
        # Case insensitive comparison
        if book["title"].lower() == title.lower():
            return book
    return None  # Return None if the book is not found


# Function to sort books by title in alphabetical order
def sort_books(books):
    # Sort the books list by the title in alphabetical order
    return sorted(books, key=lambda x: x["title"].lower())


# Function to find the oldest book in the collection
def find_oldest_book(books):
    # Find the book with the minimum year
    return min(books, key=lambda x: x["year"])


# Function to find the newest book in the collection
def find_newest_book(books):
    # Find the book with the maximum year
    return max(books, key=lambda x: x["year"])


# Function to export book titles to a CSV file
def export_titles_to_csv(books, filename):
    # Extract titles from the books list
    titles = [book["title"] for book in books]  # List of book titles
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for title in titles:
            writer.writerow([title])  # Write each title to a new row


# Function to export book publication years to a CSV file
def export_years_to_csv(books, filename):
    # Extract years from the books list
    years = array('i', [book["year"] for book in books])  # Array of book years
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for year in years:
            writer.writerow([year])  # Write each year to a new row
    print(f"Book publication years exported to {filename} using an array.")


# Function to count the number of books by a specific author
def count_titles_by_author(books, author):
    # Count the number of books by the specified author
    return sum(1 for book in books if book["author"].lower() == author.lower())


# Function to load books from a JSON file
def load_books(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)  # Load the books list from the JSON file
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found


# Function to save books to a JSON file
def save_books(books, filename='books.json'):
    with open(filename, 'w') as file:
        json.dump(books, file, indent=4)  # Save the books list to the JSON file


# Main function to run the Book Management System
def main():
    books = load_books('books.json')  # Load books from the JSON file
    while True:
        # Display the menu options to the user
        print("\nBook Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Sort Books")
        print("4. Find Oldest Book")
        print("5. Find Newest Book")
        print("6. Export Titles to CSV")
        print("7. Export Years to CSV")
        print("8. Count Titles by Author")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Get book details from the user and add the book to the collection
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            year = int(input("Enter publication year: "))
            price = float(input("Enter price: "))
            add_book(books, title, author, genre, year, price)
            print("Book added successfully")

        elif choice == '2':
            # Search for a book by title and display the result
            title = input("Enter title to search: ")
            book = search_book(books, title)
            if book:
                print(f"\nSearch results\n\n"
                      f"Title: {book['title']}\n"
                      f"Author: {book['author']}\n"
                      f"Genre: {book['genre']}\n"
                      f"Year: {book['year']}\n"
                      f"Price: {book['price']}")
            else:
                print("Book not found.")

        elif choice == '3':
            # Sort books by title and display the sorted list
            sorted_books = sort_books(books)
            print("Books sorted by title:")
            for book in sorted_books:
                print(book["title"])

        elif choice == '4':
            # Find and display the oldest book
            oldest_book = find_oldest_book(books)
            if oldest_book:
                print(f"The oldest book is {oldest_book['title']} "
                      f"({oldest_book['year']}) by "
                      f"{oldest_book['author']}")

        elif choice == '5':
            # Find and display the newest book
            newest_book = find_newest_book(books)
            if newest_book:
                print(f"The newest book is {newest_book['title']} ("
                      f"{newest_book['year']}) by "
                      f"{newest_book['author']}")

        elif choice == '6':
            # Export book titles to a CSV file
            filename = input("Enter filename for CSV export: ")
            export_titles_to_csv(books, filename)
            print(f"Titles exported to {filename}")

        elif choice == '7':
            # Export book publication years to a CSV file
            filename = input("Enter filename for CSV export: ")
            export_years_to_csv(books, filename)
            print(f"Years exported to {filename}")

        elif choice == '8':
            # Count and display the number of books by a specific author
            author = input("Enter author's name: ")
            count = count_titles_by_author(books, author)
            if count == 1:
                print(f"{author} has {count} book in the collection.")
            else:
                print(f"{author} has {count} books in the collection.")

        elif choice == '9':
            break  # Exit the program

        else:
            print("Invalid choice. Please try again.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
