#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:23:43 2023

@author: zhanghaoqi
"""

#book-master web scraping program

#three layers of scraping
#1st: scrape the categories
#2nd: scrape the books
#3rd: scrape the info of the books

#return a list of dictionaries, each dictionary contain the information of each book

from bs4 import BeautifulSoup
import requests

main_url = "http://books.toscrape.com/"
main_page = requests.get(main_url).text
main_soup = BeautifulSoup(main_page,"html.parser")




def fetch_categories():
    side_categories = main_soup.find_all("div", class_="side_categories")[0]
    categories_list = side_categories.findChild().ul.find_all("li")
    
    global categories
    categories = list(
        map(
            lambda name: name.replace("\n", "").strip(),
            list(map(lambda tag: tag.a.getText(), categories_list)),
        ),
    )

    global category_links
    category_links = []


    for category_item in categories_list:
        category_link = category_item.find("a")["href"]
        category_links.append(category_link)


def fetch_links_of_categories():
    fetch_categories()
    
    global urls_of_categories
    urls_of_categories = []

    for link in category_links:
        url = main_url + link
        urls_of_categories.append(url)
    


def fetch_books():
    fetch_links_of_categories()

    global books_total_titles
    books_total_titles = []

    global books_total_links
    books_total_links =[]
    

    category_index = 0
    
    for link in urls_of_categories:

        category_page = requests.get(link).text
        category_soup = BeautifulSoup(category_page,"html.parser")
        books_list = category_soup.find_all("article", class_="product_pod")

        each_category_titles = []
        each_category_links = []
        

        for book in books_list:
            book_title = book.h3.a.text
            book_link = book.h3.a["href"]
            each_category_titles.append(book_title)
            each_category_links.append(book_link)


        books_total_titles.append(each_category_titles)
        books_total_links.append(each_category_links)

def organize_book_info():
    fetch_books()
    
    all_books_info = []



    for books_by_categories in books_total_titles:

        flag = 0
        
        for book_title in books_by_categories:
            book_index = book_title.index(book_title)

            book_info ={}
            
            book_info["Title: "] = book_title
            book_info["Category: "] = categories[flag]
            book_info["Link: "] = books_total_links[flag][book_index]

            flag += 1

            all_books_info.append(book_info)

        print(all_books_info)

organize_book_info()
            
            
