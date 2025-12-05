# By Alex Pagac

# Install these dependices 
# none so far

# Dependincies ====----
# pip install google

# Modules ====---- 
from google import search

# Web Browser ====----
ip=raw_input("What would you like to search for? ")

for url in search(ip, stop=20):
     print(url)


# Art ====----
def art(): 
    """
    
  ____              _     
 |  _ \  ___   ___ | | __ 
 | | | |/ _ \ / _ \| |/ / 
 | |_| | (_) | (_) |   <  
 |____/ \___/ \___/|_|\_\ 
 
    by ShadeXplot

    
    """
print(art.__doc__)

# ----==== Still working on this below ====----

import requests
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    return response.text

def process_search_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    book_links = []
    for link in links:
        href = link.get('href')
        if href and 'book' in href:
            book_links.append(href)
    return book_links

def download_book(url, file_type):
    response = requests.get(url)
    with open(f"book.{file_type}", 'wb') as file:
        file.write(response.content)
    print(f"Book downloaded as book.{file_type}")

def on_search():
    query = search_entry.get()
    file_type = file_type_var.get()
    results = google_search(query)
    book_links = process_search_results(results)
    for link in book_links:
        download_book(link, file_type)

# Create the main window
root = tk.Tk()
root.title("Dook - Book Search and Download")

# Create and place the search entry
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=10)

# Create and place the search button
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack(pady=5)

# Create and place the file type dropdown
file_type_var = tk.StringVar(value="PDF")
file_type_menu = ttk.OptionMenu(root, file_type_var, "PDF", "PDF", "EPUB", "MOBI")
file_type_menu.pack(pady=5)

# Run the application
root.mainloop()

