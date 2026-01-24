import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from urllib.parse import unquote
import threading

def google_dork_search(query, filetype):
    """Search Google with dork syntax and return first result URL"""
    try:
        search_url = f"https://www.google.com/search?q={query}+filetype:{filetype}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first search result link
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'url?q=' in href:
                try:
                    url = href.split('url?q=')[1].split('&sa=U')[0]
                    decoded_url = unquote(url)
                    # Validate it's a real URL
                    if decoded_url.startswith('http'):
                        return decoded_url
                except:
                    continue
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Search error: {e}")
        return None

def download_file(url, filename, callback=None):
    """Download file from URL with progress callback"""
    try:
        response = requests.get(url, stream=True, timeout=15, allow_redirects=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    downloaded += len(chunk)
                    if callback and total_size:
                        progress = (downloaded / total_size) * 100
                        callback(progress)
        return True
    except requests.exceptions.RequestException as e:
        raise Exception(f"Download failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Download failed: {str(e)}")

class DookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dook - Google Dorking Tool")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Title
        title = tk.Label(root, text="Dook", font=("Arial", 24, "bold"), bg='#f0f0f0')
        title.pack(pady=10)
        
        subtitle = tk.Label(root, text="Google Dorking Search Tool", font=("Arial", 10), bg='#f0f0f0', fg='#666')
        subtitle.pack()
        
        # Search Frame
        search_frame = ttk.LabelFrame(root, text="Search Settings", padding=10)
        search_frame.pack(pady=10, padx=10, fill="both", expand=False)
        
        # Query
        tk.Label(search_frame, text="Search Query:").grid(row=0, column=0, sticky="w", pady=5)
        self.query_entry = ttk.Entry(search_frame, width=40)
        self.query_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # File Type
        tk.Label(search_frame, text="File Type:").grid(row=1, column=0, sticky="w", pady=5)
        self.filetype_var = tk.StringVar(value="pdf")
        self.filetype_combo = ttk.Combobox(search_frame, textvariable=self.filetype_var, 
                                           values=["pdf", "epub", "mobi", "azw3", "txt", "docx"], width=37)
        self.filetype_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons Frame
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        
        self.search_btn = ttk.Button(button_frame, text="Search & Download", command=self.search_and_download)
        self.search_btn.pack(side="left", padx=5)
        
        self.clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_fields)
        self.clear_btn.pack(side="left", padx=5)
        
        # Output Frame
        output_frame = ttk.LabelFrame(root, text="Status", padding=10)
        output_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Progress Bar
        self.progress = ttk.Progressbar(output_frame, mode='indeterminate')
        self.progress.pack(fill="x", pady=5)
        
        # Output Text
        self.output_text = tk.Text(output_frame, height=12, width=70, wrap="word")
        self.output_text.pack(fill="both", expand=True, pady=5)
        
        scrollbar = ttk.Scrollbar(self.output_text)
        scrollbar.pack(side="right", fill="y")
        self.output_text.config(yscrollcommand=scrollbar.set)
        
        # Status Bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief="sunken")
        status_bar.pack(fill="x")
    
    def log(self, message):
        """Log message to output text"""
        self.output_text.insert("end", message + "\n")
        self.output_text.see("end")
        self.root.update()
    
    def clear_fields(self):
        """Clear input fields"""
        self.query_entry.delete(0, "end")
        self.output_text.delete("1.0", "end")
        self.status_var.set("Ready")
    
    def search_and_download(self):
        """Search and download file in background thread"""
        query = self.query_entry.get().strip()
        filetype = self.filetype_var.get()
        
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search query")
            return
        
        # Disable button and start progress
        self.search_btn.config(state="disabled")
        self.progress.start()
        self.output_text.delete("1.0", "end")
        
        # Run in background thread
        thread = threading.Thread(target=self._search_download_worker, args=(query, filetype))
        thread.start()
    
    def _search_download_worker(self, query, filetype):
        """Worker thread for search and download"""
        try:
            self.status_var.set("Searching...")
            self.log(f"Searching for: {query} (filetype: {filetype})")
            self.log(f"Search URL: https://www.google.com/search?q={query}+filetype:{filetype}")
            
            url = google_dork_search(query, filetype)
            
            if not url:
                self.log("❌ No results found. Try a different search query or file type.")
                self.log("Tips:")
                self.log("  - Make sure the file type matches what's available online")
                self.log("  - Try more specific search terms")
                self.log("  - Use quotes for exact phrases: \"the exact title\"")
                self.status_var.set("No results found")
            else:
                self.log(f"✓ Found result: {url}\n")
                self.log("Downloading...")
                self.status_var.set("Downloading...")
                
                filename = f"{query.replace(' ', '_').replace('\"', '')}.{filetype}"
                
                def progress_callback(percent):
                    self.status_var.set(f"Downloading... {percent:.1f}%")
                
                try:
                    download_file(url, filename, progress_callback)
                    self.log(f"✓ Downloaded successfully: {filename}")
                    self.log(f"Saved to: {os.path.abspath(filename)}")
                    self.status_var.set("Download complete")
                    messagebox.showinfo("Success", f"File downloaded:\n{filename}\n\nLocation: {os.path.abspath(filename)}")
                except Exception as e:
                    self.log(f"❌ Download failed: {str(e)}")
                    self.status_var.set("Download failed")
        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
            self.status_var.set("Error occurred")
        finally:
            self.progress.stop()
            self.search_btn.config(state="normal")

def main():
    root = tk.Tk()
    app = DookGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()