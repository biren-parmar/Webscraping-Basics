import requests
import bs4


#############################################
# Find all the books with given star rating #
#############################################
def get_all_books(stars):
    url = 'http://books.toscrape.com/catalogue/page-{}.html'
    books = []

    for i in range(1, 51):
        res = requests.get(url.format(i))
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        booksall = soup.select('.product_pod')
        for bk in booksall:
            if stars == "Five":
                if bk.select('.star-rating.Five'):
                    books.append(bk.select('a')[1]['title'])
            elif stars == "Four":
                if bk.select('.star-rating.Four'):
                    books.append(bk.select('a')[1]['title'])
            elif stars == "Three":
                if bk.select('.star-rating.Three'):
                    books.append(bk.select('a')[1]['title'])
            elif stars == "Two":
                if bk.select('.star-rating.Two'):
                    books.append(bk.select('a')[1]['title'])
            elif stars == "One":
                if bk.select('.star-rating.One'):
                    books.append(bk.select('a')[1]['title'])
    return books


#######################################################
# Find all the books with given star rating with cost #
#######################################################
def get_all_books_with_prices(stars):
    url = 'http://books.toscrape.com/catalogue/page-{}.html'
    books = {}

    for i in range(1, 51):
        res = requests.get(url.format(i))
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        booksall = soup.select('.product_pod')
        for bk in booksall:
            if stars == "Five":
                if bk.select('.star-rating.Five'):
                    books[bk.select('a')[1]['title']] = bk.select('.price_color')[0].getText()[2:]
            elif stars == "Four":
                if bk.select('.star-rating.Four'):
                    books[bk.select('a')[1]['title']] = bk.select('.price_color')[0].getText()[2:]
            elif stars == "Three":
                if bk.select('.star-rating.Three'):
                    books[bk.select('a')[1]['title']] = bk.select('.price_color')[0].getText()[2:]
            elif stars == "Two":
                if bk.select('.star-rating.Two'):
                    books[bk.select('a')[1]['title']] = bk.select('.price_color')[0].getText()[2:]
            elif stars == "One":
                if bk.select('.star-rating.One'):
                    books[bk.select('a')[1]['title']] = bk.select('.price_color')[0].getText()[2:]
    return books
