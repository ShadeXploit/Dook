import asyncio
import os
import re
import requests
from urllib.parse import urlparse, unquote

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def download_first_pdf(query: str, download_dir: str = "downloads"):
    """

                            ____              _     
                            |  _ \  ___   ___ | | __ 
                            | | | |/ _ \ / _ \| |/ / 
                            | |_| | (_) | (_) |   <  
                            |____/ \___/ \___/|_|\_\ 
                            
                                by ShadeXploit
    


    Searches Google for a PDF using a headless browser and downloads the first result.

    Args:
        query (str): The search query (e.g., 'filetype:pdf "The Hobbit"').
        download_dir (str): The directory to save the downloaded file.
    """
    # Ensure the download directory exists
    if not os.path.exists(download_dir):
os.makedirs(download_dir)

async with async_playwright() as p:
        # Launch a headless Chromium browser
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Construct the search URL
        search_url = f"https://www.google.com/search?q={query}"
        print(f"[*] Navigating to: {search_url}")
        await page.goto(search_url)

        # Wait for the search results to load
        await page.wait_for_selector('div#search', timeout=15000)

        # Get the page's HTML content
        html_content = await page.content()
        
        # Parse with BeautifulSoup for easier extraction
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the first search result link container
        # Google wraps main result links in an <a> tag inside an <h3> tag
        first_result_h3 = soup.find('h3')
        
        if not first_result_h3 or not first_result_h3.find('a'):
            print("[!] No search results found. Google may have blocked the request.")
            await browser.close()
            return

        first_result_link_tag = first_result_h3.find('a')
        first_result_url = first_result_link_tag.get('href')

        # Google search result URLs are often redirected. We need to resolve the final URL.
        print(f"[*] Found potential link (redirect): {first_result_url}")
        
        # Resolve the final URL by having the browser navigate to it
        response = await page.goto(first_result_url, wait_until="networkidle")
        
        # Get the final, redirected URL
        final_url = page.url
        print(f"[*] Resolved final URL: {final_url}")

        # Check if the final URL is a direct link to a PDF
        if final_url.endswith('.pdf'):
            pdf_filename = os.path.basename(urlparse(final_url).path)
            if not pdf_filename: # Fallback if path is empty
                 pdf_filename = f"downloaded_{re.sub(r'\W+', '_', query)}.pdf"

            pdf_path = os.path.join(download_dir, pdf_filename)
            print(f"[*] Direct PDF link found. Downloading to: {pdf_path}")

            # Use Playwright's download feature for more reliability
            async with page.expect_download() as download_info:
                # Re-navigate to ensure the download starts
                await page.goto(final_url)
            download = await download_info.value

            # Save the downloaded file
            await download.save_as(pdf_path)
            print(f"[+] Successfully downloaded {pdf_filename}")

        else:
            print("[!] The first result is not a direct PDF link. Downloading as 'downloaded_page.html' for inspection.")
            page_path = os.path.join(download_dir, "downloaded_page.html")
            await page.save_snapshot(path=page_path)
            print(f"[*] Saved the page content to {page_path}. Please check it manually.")

        await browser.close()


# # --- Example Usage ---
# if __name__ == "__main__":
#     # Use the Google dork you wanted
#     book_title = "The Fellowship of the Ring"
#     search_query = f'filetype:pdf "{book_title}"'
    
#     print("--- Starting Book Downloader ---")
#     asyncio.run(download_first_pdf(search_query))
#     print("--- Finished ---")