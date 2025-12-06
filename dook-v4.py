import requests
from bs4 import BeautifulSoup
import os

def google_dork_search(query, filetype):
    search_url = (f"https://www.google.com/search?q={query}+filetype:{filetype}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first search result link
    for link in soup.find_all('a', href=True):
        if 'url?q=' in link['href']:
            return link['href'].split('url?q=')[1].split('&sa=U')[0]
    return None

def download_file(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Downloaded {filename}") 

def main():
    while True:
        menu = '''
                _____              _     
                |  _ \  ___   ___ | | __ 
                | | | |/ _ \ / _ \| |/ / 
                | |_| | (_) | (_) |   <  
                |____/ \___/ \___/|_|\_\ 

                                by ShadeXploit
        =========================================
        1. Find Book
        2. Search and download another file type
        3. Exit
        =========================================
        '''
        print(menu)
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            query = input("Enter your search query: ")
            filetype = 'pdf'
            url = google_dork_search(query, filetype)
            if url:
                filename = f"{query.replace(' ', '_')}.pdf"
                download_file(url, filename)
            else:
                print("No results found.")
        elif choice == '2':
            query = input("Enter your search query: ")
            filetype = input("Enter the file type (e.g., doc, xls): ")
            url = google_dork_search(query, filetype)
            if url:
                filename = f"{query.replace(' ', '_')}.{filetype}"
                download_file(url, filename)
            else:
                print("No results found.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
