'''
Web Scraping Excercise
'''
import requests
import bs4
import math

result = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(result.text,'lxml')

def get_author_names(html_page):
    '''
    get author names
    '''
    set_authors=set()
    authors=html_page.select('.author')
    for author in authors:
        set_authors.add(author.text)
    return set_authors
    
print("Authors")
print(get_author_names(soup))

def get_text_quotes(html_page):
    '''
    get text quotes
    '''
    set_quotes=set()
    quotes=html_page.select('.text')
    for quote in quotes:
        set_quotes.add(quote.getText())

    print(*set_quotes)
print("Quotes")
get_text_quotes(soup)

def get_top_ten_tags(html_page):
    '''
    get top ten tags
    '''
    set_top_ten_tags=set()
    top_ten_tags=html_page.select('.tag-item')
    for top_ten_tag in top_ten_tags:
        top_ten_tag=top_ten_tag.select('.tag')[0].getText()
        set_top_ten_tags.add(top_ten_tag)

    print(*set_top_ten_tags)

print("Top ten tags")
get_top_ten_tags(soup)

def get_unigue_authors():
    page=1
    unique_authors=set()
    authors=[]
    while page<=math.inf:
        base_url='http://quotes.toscrape.com/page/{}/'
        result=requests.get(base_url.format(page))
        soup=bs4.BeautifulSoup(result.text,'lxml')
        authors.extend(get_author_names(soup))
        if 'No quotes found!' in result.text:
            break
        page+=1
    unique_authors=set(authors)
    sorted(unique_authors)
    unique_authors=list(unique_authors)
    unique_authors.sort()
    print(*unique_authors)       

print("Unique authors")
get_unigue_authors()
