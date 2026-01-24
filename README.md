# Dook - Find and Read Any Book on the Internet

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A powerful and user-friendly Google dorking search tool with an intuitive GUI. Search for specific file types across the web - perfect for finding ebooks and documents using advanced Google dork queries.

## Features

- **Advanced Google Dorking** - Search using filetype dorks and advanced operators
- **Modern GUI** - Clean, responsive tkinter interface
- **Browser Integration** - Opens searches directly in your default browser
- **Ebook Focused** - Pre-configured file types for common ebook formats
- **Non-Blocking UI** - Background threading prevents GUI freezing
- **Multiple File Types** - Support for PDF, EPUB, TXT, DOCX, DOC, ODT

## Requirements

- Python 3.7+
- tkinter (included with Python on Windows)

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/ShadeXploit/Dook.git
cd Dook
```

### Step 2: Install Dependencies
```bash
pip install requests beautifulsoup4
```

Or using requirements:
```bash
pip install -r requirements.txt
```

> **Want to compile from source?** Check out [COMPILE.md](COMPILE.md) for detailed instructions on building Dook directly from the source code.

## Usage

Simply run the script to launch the GUI:

```bash
python dook.py
```

### Using the GUI

1. **Enter Search Query** - Type what you're looking for (e.g., "Harry Potter", "Python Programming")
2. **Select File Type** - Choose from ebook formats (PDF, EPUB, TXT, DOCX, DOC, ODT)
3. **Click "Search & Open"** - Your default browser opens with the Google search results
4. **Click the first link** - Download or view the file directly

### Supported Ebook File Types

| Format | Description | Best For |
|--------|-------------|----------|
| **PDF** | Portable Document Format | Universal ebook format, works everywhere |
| **EPUB** | Electronic Publication | Standard ebook format, compatible with most readers |
| **TXT** | Plain Text | Simple text-based books and documents |
| **DOCX** | Microsoft Word | Modern word documents and formatted texts |
| **DOC** | Legacy Word Format | Older Microsoft Word documents |
| **ODT** | OpenDocument Text | LibreOffice/OpenOffice documents |

### Example Searches

**Basic ebook search:**
```
Query: "The Great Gatsby"
Filetype: PDF
```

**Author search:**
```
Query: "George Orwell 1984"
Filetype: EPUB
```

**Technical documentation:**
```
Query: "Python Programming Guide"
Filetype: PDF
```

## Google Dork Operators

This tool supports Google's powerful dork operators. Here are the most useful ones:

| Operator | Description | Example |
|----------|-------------|---------|
| `filetype:` | Search for specific file types | `filetype:pdf` |
| `intitle:` | Search in page titles | `intitle:"book title"` |
| `intext:` | Search in page content | `intext:"chapter"` |
| `site:` | Search specific websites | `site:archive.org` |
| `"phrase"` | Exact phrase match | `"exact book title"` |
| `OR` | Either term | `PDF OR EPUB` |
| `-` | Exclude term | `-site:amazon.com` |

### Advanced Dork Examples for Books

```
"The Bible" filetype:pdf

"Harry Potter" intitle:"index.of" filetype:epub

Stephen King filetype:txt

"Programming in C" site:archive.org filetype:pdf
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `requests` | Latest | HTTP requests for web searches |
| `beautifulsoup4` | Latest | HTML parsing |
| `tkinter` | Built-in | GUI framework |

## Interface

The GUI includes:
- **Search Query Input** - Enter your search terms
- **File Type Dropdown** - Select from common ebook formats
- **Search & Open Button** - Launch your search
- **Clear Button** - Reset the search fields
- **Output Log** - View search information
- **Status Bar** - Real-time operation status

## Important Notes

- **Ethical Use Only** - Use this tool responsibly and legally
- **Respect Copyright** - Only download files you have permission to access
- **Browser Based** - The tool opens searches in your browser for you to manually select results
- **No Automatic Downloads** - You control what gets downloaded

## Troubleshooting

### Browser won't open
- Check if your default browser is properly configured
- Try manually opening the search URL in your browser
- Ensure you have an internet connection

### No results found
- Try different search terms or file types
- Use more specific titles or author names
- Check that the book exists in that format online

### GUI not launching
- Ensure tkinter is installed: `python -m tkinter`
- On Linux: `sudo apt-get install python3-tk`
- On macOS: tkinter should be included with Python

## Contributing

Found a bug or have a feature request? Feel free to open an issue or submit a pull request!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Original Author

Created with love by ShadeXploit

## Links

- [GitHub Repository](https://github.com/ShadeXploit/Dook)
- [Report Issues](https://github.com/ShadeXploit/Dook/issues)
- [Google Dork Cheat Sheet](https://www.exploit-db.com/google-hacking-database)

---

**If you find this tool helpful, please consider giving it a star!**

*Last Updated: January 2026*
- **URL Decoding** - Properly handles encoded URLs from Google results
- **Chunk Streaming** - Efficient memory usage for large files
- **Thread Safety** - Background worker threads prevent UI blocking

## File Structure

```
Dook/
├── dook-v4.py       # Main application file
├── README.md        # This file
└── requirements.txt # Python dependencies
```

## Important Notes

- **Ethical Use Only** - Use this tool responsibly and legally
- **Respect robots.txt** - Don't overwhelm servers
- **Google ToS** - This tool complies with Google's terms of service
- **File Permissions** - Only download files you have permission to access

## Troubleshooting

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

## Contributing

Found a bug or have a feature request? Feel free to open an issue or submit a pull request!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Original Author

Created with love by ShadeXploit

## Links

- [GitHub Repository](https://github.com/yourusername/Dook)
- [Report Issues](https://github.com/yourusername/Dook/issues)

---

**If you find this tool helpful, please consider giving it a star!**

*Last Updated: January 2026*  
