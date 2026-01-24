# 🔍 Dook - Google Dorking Tool

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A powerful and user-friendly Google dorking search tool with an intuitive GUI. Search for specific file types across the web and download them instantly.

## ✨ Features

- 🎯 **Advanced Google Dorking** - Search using filetype dorks to find specific documents
- 💻 **Modern GUI** - Clean, responsive tkinter interface
- 📥 **One-Click Download** - Find and download files automatically
- 📊 **Progress Tracking** - Real-time progress bar and status updates
- 🔒 **Robust Error Handling** - Handles timeouts, connection errors, and invalid URLs
- 📝 **Multiple File Types** - Support for PDF, DOC, DOCX, XLS, XLSX, PPT, TXT
- 🧵 **Non-Blocking UI** - Background threading prevents GUI freezing
- 📍 **File Location Display** - Shows exact save path for downloaded files

## 📋 Requirements

- Python 3.7+
- tkinter (included with Python on Windows)

## 📦 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/ShadeXploit/Dook.git
cd Dook
```

### Step 2: Install Dependencies and Make Executable
```bash
pip install requests beautifulsoup4
chmode +x dook.py
```

Or using requirements:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Simply run the script to launch the GUI:

```bash
python dook-v4.py
```

### Using the GUI

1. **Enter Search Query** - Type what you're looking for (e.g., "confidential reports", "internal memos")
2. **Select File Type** - Choose from the dropdown (PDF, DOC, DOCX, XLS, XLSX, PPT, TXT)
3. **Click "Search & Download"** - The tool will search Google and download the first result
4. **Monitor Status** - Watch the progress bar and status messages in real-time
5. **Find Your File** - Downloaded files are saved in the current directory

### Example Searches

```
Query: "Financial Reports"
Filetype: PDF

Query: "Employee Directory"
Filetype: XLSX

Query: "Budget Planning"
Filetype: DOCX
```

## 📋 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `requests` | Latest | HTTP requests for web scraping |
| `beautifulsoup4` | Latest | HTML parsing and link extraction |
| `tkinter` | Built-in | GUI framework |

## 🎨 Interface

The GUI includes:
- **Search Settings Panel** - Configure query and file type
- **Status Display** - Real-time search and download status
- **Progress Bar** - Visual feedback during operations
- **Output Log** - Detailed information about searches and downloads
- **Control Buttons** - Search, Download, and Clear functions

## 🔍 How It Works

1. **Search Phase**: Sends a Google search with filetype dork syntax
2. **Parse Phase**: BeautifulSoup extracts the first relevant result
3. **Download Phase**: Downloads the file with progress tracking
4. **Save Phase**: Saves file with formatted name in current directory

## ⚙️ Technical Details

- **User-Agent Rotation** - Uses modern Chrome user agent to avoid blocks
- **Timeout Protection** - 10-second timeout on all requests
- **URL Decoding** - Properly handles encoded URLs from Google results
- **Chunk Streaming** - Efficient memory usage for large files
- **Thread Safety** - Background worker threads prevent UI blocking

## 📝 File Structure

```
Dook/
├── dook-v4.py       # Main application file
├── README.md        # This file
└── requirements.txt # Python dependencies
```

## ⚠️ Important Notes

- **Ethical Use Only** - Use this tool responsibly and legally
- **Respect robots.txt** - Don't overwhelm servers
- **Google ToS** - This tool complies with Google's terms of service
- **File Permissions** - Only download files you have permission to access

## 🐛 Troubleshooting

### "No results found"
- Try a different search query
- Verify the file type exists online
- Check your internet connection

### "Download failed"
- The file might be too large or temporarily unavailable
- Try downloading again
- Check that you have write permissions in the directory

### GUI not appearing
- Ensure tkinter is installed: `python -m tkinter`
- On Linux, you may need: `sudo apt-get install python3-tk`

## 🤝 Contributing

Found a bug or have a feature request? Feel free to open an issue or submit a pull request!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Original Author

Created with ❤️ by ShadeXploit

## 🔗 Links

- [GitHub Repository](https://github.com/yourusername/Dook)
- [Report Issues](https://github.com/yourusername/Dook/issues)

---

**⭐ If you find this tool helpful, please consider giving it a star!**

*Last Updated: January 2026*  
