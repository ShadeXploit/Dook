import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from urllib.parse import unquote
import threading
import webbrowser

def google_dork_search(query, filetype):
    """Generate Google search URL with dork syntax"""
    search_url = f"https://www.google.com/search?q={query}+filetype:{filetype}"
    return search_url

def open_in_browser(url):
    """Open URL in default browser"""
    try:
        webbrowser.open(url)
        return True
    except Exception as e:
        raise Exception(f"Failed to open browser: {str(e)}")

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
        
        # Author (Optional)
        tk.Label(search_frame, text="Author (Optional):").grid(row=1, column=0, sticky="w", pady=5)
        self.author_entry = ttk.Entry(search_frame, width=40)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # File Type
        tk.Label(search_frame, text="File Type:").grid(row=2, column=0, sticky="w", pady=5)
        self.filetype_var = tk.StringVar(value="pdf")
        self.filetype_combo = ttk.Combobox(search_frame, textvariable=self.filetype_var, 
                                           values=["pdf", "epub", "txt", "docx", "doc", "odt"], width=37)
        self.filetype_combo.grid(row=2, column=1, padx=5, pady=5)
        
        # Buttons Frame
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        
        self.search_btn = ttk.Button(button_frame, text="Search & Open", command=self.search_and_open)
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
        self.author_entry.delete(0, "end")
        self.output_text.delete("1.0", "end")
        self.status_var.set("Ready")
    
    def search_and_open(self):
        """Search and open first result in browser"""
        query = self.query_entry.get().strip()
        author = self.author_entry.get().strip()
        filetype = self.filetype_var.get()
        
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search query")
            return
        
        # Combine query and author if author is provided
        full_query = f"{query} {author}" if author else query
        
        # Disable button and start progress
        self.search_btn.config(state="disabled")
        self.progress.start()
        self.output_text.delete("1.0", "end")
        
        # Run in background thread
        thread = threading.Thread(target=self._search_open_worker, args=(full_query, filetype))
        thread.start()
    
    def _search_open_worker(self, query, filetype):
        """Worker thread for search and open"""
        try:
            self.status_var.set("Opening search in browser...")
            self.log(f"Searching for: {query} (filetype: {filetype})")
            
            search_url = google_dork_search(query, filetype)
            self.log(f"URL: {search_url}\n")
            
            open_in_browser(search_url)
            self.log(f"✓ Google search opened in browser")
            self.log(f"Click the first link to open the file")
            self.status_var.set("Search opened in browser")
            
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