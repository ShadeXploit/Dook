# 🔨 Compiling Dook from Source

This guide will help you set up and run Dook directly from the source code.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.7 or higher** - [Download here](https://www.python.org/downloads/)
- **Git** (optional, for cloning the repository) - [Download here](https://git-scm.com/)
- **pip** (Python package manager) - Usually comes with Python

## Step 1: Get the Source Code

### Option A: Clone from GitHub (Recommended)

```bash
git clone https://github.com/ShadeXploit/Dook.git
cd Dook
```

### Option B: Download as ZIP

1. Go to the [GitHub repository](https://github.com/ShadeXploit/Dook)
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file to your desired location
5. Open a terminal/command prompt and navigate to the extracted folder

## Step 2: Verify Python Installation

Check that Python is installed and accessible:

```bash
python --version
```

You should see something like: `Python 3.x.x`

## Step 3: Create a Virtual Environment (Optional but Recommended)

Creating a virtual environment keeps your project dependencies isolated:

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt when activated.

## Step 4: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install requests beautifulsoup4
```

### What These Do:
- **requests** - Handles HTTP requests to Google
- **beautifulsoup4** - Parses HTML responses

## Step 5: Run the Application

Launch the Dook GUI:

```bash
python dook.py
```

The GUI window should open immediately. If it doesn't, check the terminal for error messages.

## Troubleshooting

### Python Not Found
- Make sure Python is in your system PATH
- Try using `python3` instead of `python`
- On Windows, use the full path to python.exe

### Module Not Found Errors
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or install individually
pip install requests beautifulsoup4
```

### tkinter Not Found
tkinter usually comes with Python, but some systems require separate installation:

**Windows:** tkinter is included with Python installer

**macOS:**
```bash
brew install python-tk@3.9  # Replace 3.9 with your Python version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-tk
```

**Linux (Fedora):**
```bash
sudo dnf install python3-tkinter
```

### GUI Won't Open
- Ensure you're using the correct Python version (3.7+)
- Try running from the directory containing `dook.py`
- Check for error messages in the terminal

## File Structure

After setup, your directory should look like:

```
Dook/
├── dook.py              # Main application
├── README.md            # User documentation
├── COMPILE.md           # This file
├── requirements.txt     # Python dependencies
└── venv/                # Virtual environment (if created)
```

## Running the Application

### Standard Method:
```bash
python dook.py
```

### With Virtual Environment (Windows):
```bash
venv\Scripts\activate
python dook.py
```

### With Virtual Environment (macOS/Linux):
```bash
source venv/bin/activate
python dook.py
```

## Development

### Modifying the Code

If you want to make changes to the source:

1. Edit `dook.py` with your preferred text editor
2. Save the file
3. Run it again to test your changes

Common areas to modify:
- **File types dropdown** (line ~50): Change supported formats
- **Search function** (line ~9): Modify search behavior
- **GUI layout** (lines 25-85): Adjust window size or colors

### Installing in Editable Mode

For development, you can install the package in editable mode:

```bash
pip install -e .
```

This allows you to test changes without reinstalling each time.

## Building a Standalone Executable

If you want to distribute Dook as a standalone executable, you can use PyInstaller. **Important:** PyInstaller creates executables for the OS it's running on. To create a Windows `.exe`, you must run these commands on a Windows machine. To create a Linux executable, run them on Linux, etc.

### For Windows (.exe):

Run these commands on a **Windows machine**:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico dook.py
```

The `.exe` file will be created in the `dist/` folder.

### For Linux/macOS:

Run these commands on a **Linux or macOS machine**:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed dook.py
```

The executable will be created in the `dist/` folder.

### PyInstaller Options Explained:
- `--onefile` - Creates a single executable file (instead of a folder)
- `--windowed` - Hides the console window on startup (Windows only, recommended)
- `--icon=icon.ico` - Sets a custom icon for the executable (Windows only, optional)
- `dook.py` - The main Python file to compile

### Cross-Platform Notes:
- **Windows executables (.exe):** Only runnable on Windows
- **Linux executables:** Only runnable on Linux
- **macOS executables:** Only runnable on macOS
- You **cannot** create a Windows executable from Linux, or vice versa

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.7 | 3.10+ |
| RAM | 512 MB | 2 GB |
| Disk Space | 100 MB | 500 MB |
| OS | Windows 7+ / macOS 10.9+ / Linux | Modern OS |

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Review error messages in the terminal carefully
3. Open an issue on [GitHub Issues](https://github.com/ShadeXploit/Dook/issues)
4. Include:
   - Your Python version (`python --version`)
   - Your operating system
   - The error message you're seeing
   - Steps you took to reproduce the issue

## Tips for Success

- ✅ Use a virtual environment to avoid conflicts
- ✅ Keep your Python installation up to date
- ✅ Verify all dependencies are installed before running
- ✅ Run from the command line to see error messages
- ✅ Check GitHub Issues before reporting a bug

## Next Steps

Once Dook is running successfully:

1. Read the [README.md](README.md) for usage instructions
2. Try searching for your favorite books
3. Explore Google dork operators for advanced searches
4. Contribute improvements back to the project!

---

**Happy searching! 📚**

*Last Updated: January 2026*
