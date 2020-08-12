import requests
import bs4


############################################################
# all authors in the entire webpage, all pages in the site #
############################################################
def get_authors():
    url = 'http://quotes.toscrape.com/page/{}/'
    last_page = 0
    page = 1
    Authors = set()
    while last_page == 0:
        res = requests.get(url.format(page))
        # print(url.format(page))
        page += 1
        if "No quotes found!" not in res.text:
            # print("continuing")
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            for i in soup.select('.quote'):
                Authors.add(i.select('.author')[0].getText())
        else:
            last_page = 1
            # print("not continuing")
    return Authors


###############################################################################
# all authors in the entire webpage with their respective count of the quotes #
###############################################################################
def get_authors_quotes_count():
    url = 'http://quotes.toscrape.com/page/{}/'
    last_page = 0
    page = 1
    Authors = {}
    while (last_page == 0):
        res = requests.get(url.format(page))
        # print(url.format(page))
        page += 1
        if "No quotes found!" not in res.text:
            # print("continuing")
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            for i in soup.select('.quote'):
                if i.select('.author')[0].getText() in Authors:
                    Authors[i.select('.author')[0].getText()] += 1
                else:
                    Authors[i.select('.author')[0].getText()] = 1
        else:
            last_page = 1
            # print("not continuing")
    return Authors
