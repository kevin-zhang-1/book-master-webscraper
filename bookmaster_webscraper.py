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

from bs4 import BeautifulSoup
import requests



def fetch_by_category():
    #get categories info  

    html_categories = requests.get("http://books.toscrape.com/").text
    soup = BeautifulSoup(html_categories,"lxml")

    sector = soup.find("ul", class_ = "nav nav-list")
    list_of_categories = sector.li.ul

    for category in list_of_categories:
        category_name = category.a.text
        link_to_category = category.a["href"]

        print(f"Category Name: {category_name}")
        print(f"link:{link_to_category}")



def fetch_books():
    html_books = requests.get(link_to_category).text
    soup = BeautifulSoup(html_books,"lxml")

    books = soup.find("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
    
    for book in books:
        book_title = book.find("h3").a.text
        book_link = book.find("h3").a["href"]


        print(f"Book Title: {book_title}:")
        print(f'Book link:{book_link}')

        fetch_book_info()

def fetch_book_info():
    html_info = requests.get(book_link).text
    soup = BeautifulSoup(html_info,"lxml")

if __name__ == "__main__":
    fetch_by_category()
