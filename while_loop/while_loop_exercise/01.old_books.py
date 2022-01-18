
book_name = input()

book_counter = 0
is_book_found = False
current_book = input()
while current_book != "No More Books":

    if current_book == book_name:
        is_book_found = True
        print(f"You checked {book_counter} books and found it.")
        break
    current_book = input()
    book_counter += 1


if not is_book_found:
    print(f"The book you search is not here!\n"
          f"You checked {book_counter} books.")
