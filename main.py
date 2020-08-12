from authors_quotes import *
from get_books import *

if __name__ == '__main__':
    print("Please select the data you want to scrape: \n1) Authors \n2) Books\n")
    sel_wb = input("Please enter the scraping you want to do:")
    print("Selected Scraping: ", sel_wb)

    if sel_wb == "Authors":
        print("Please select if you want the total quotes count for each author: \na) 1 = Authors with quotes count \nb) 2 = Authors without quotes count")
        sel_author_choice = int(input("Please enter your choice:"))
        if sel_author_choice == 1:
            authors_with_quotes_count = get_authors_quotes_count()
            print(authors_with_quotes_count)
        elif sel_author_choice == 2:
            authors_list = get_authors()
            print(authors_list)
        else:
            print("Error! incorrect choice. Please re-run with choices available\n")
    elif sel_wb == "Books":
        print("Please select if you want the price along with books: \na) 1 = Books with prices \nb) 2 = Books without prices")
        sel_book_choice = int(input("Please enter your choice:"))
        if sel_book_choice == 1:
            print("Please select the rating of the books: \na) One = One star \nb) Two = Two star \nc) Three = Three star \nd) Four = Four star \ne) Five = Five star")
            sel_book_star = input("Please enter your choice:")
            books_with_prices = get_all_books_with_prices(sel_book_star)
            print(books_with_prices)
        elif sel_book_choice == 2:
            print("Please select the rating of the books: \na) One = One star \nb) Two = Two star \nc) Three = Three star \nd) Four = Four star \ne) Five = Five star")
            sel_book_star = input("Please enter your choice:")
            books = get_all_books(sel_book_star)
            print(books)
        else:
            print("Error! incorrect choice. Please re-run with choices available\n")
