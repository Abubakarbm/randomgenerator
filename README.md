# Practice Papers Downloader

An automated tool that scrapes and downloads practice papers from the university portal with built-in duplicate detection to maintain a clean, unique archive.

## 🎯 Project Purpose

This tool was created to eliminate the tedious and time-consuming process of manually retrieving practice papers from the university portal. By automating the download process, it saves hours of manual retrieval work while ensuring a well-organized collection of unique documents.

## ✨ Features

- **Automated Scraping**: Intelligently discovers and retrieves practice papers from the university portal
- **Duplicate Detection**: Prevents duplicate downloads by checking if files already exist before saving
- **Configurable Parameters**: 
  - Custom maximum attempts to discover files
  - Adjustable patience level for stopping when no new files are found
- **User-Friendly Interface**: 
  - Interactive command-line prompts
  - Optional file browser GUI for folder selection
  - Real-time progress tracking
- **Reliable & Minimal Dependencies**: Built with only essential libraries for maximum compatibility

## 🛠️ How It Works

1. **Discovery Phase**: Makes repeated POST requests to the university portal URL to discover all available practice papers
2. **Duplicate Check**: Tracks unique files and stops searching after a configurable number of attempts without finding new papers
3. **Save Phase**: Downloads and saves discovered files to your selected folder, skipping duplicates automatically
4. **Statistics**: Provides detailed feedback on successful saves, skipped duplicates, and any failures

## 📋 Requirements

- Python 3.x
- `requests` library

## 📥 Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip install requests
   ```

## 🚀 Usage

Run the script:
```bash
python randomgeneratorscript.py
```

Then follow the interactive prompts:

1. **Enter the file generation URL**: Provide the university portal URL that generates practice papers
   ```
   Enter the file generation URL: https://your-university-portal.edu/generate-papers
   ```

2. **Configure discovery parameters**:
   ```
   Maximum attempts to make? (default: 100): 100
   Stop after how many attempts without new files? (default: 20): 20
   ```

3. **Review discovered files**: The tool will display each file as it's discovered and inform you when it's complete

4. **Save files**: 
   ```
   Save all [X] files to disk? (yes/no): yes
   Browse for folder using file explorer? (yes/no): yes
   ```
   - Choose to browse for a folder using the GUI, or
   - Enter a folder path manually

5. **Results**: The tool will display:
   - Number of files successfully saved
   - Number of duplicates skipped
   - Any files that failed to save
   - Location where files were saved

## 📊 Example Output

```
============================================================
Random PDF File Downloader
============================================================

Discovering files from: https://your-university-portal.edu/...
This may take a while...

[Attempt 1] Found NEW file: practice_paper_001.pdf (Total: 1)
[Attempt 2] Found NEW file: practice_paper_002.pdf (Total: 2)
[Attempt 3] Duplicate: practice_paper_001.pdf (No new files for 1 attempts)
...
✓ No new files found in 20 attempts. Discovery complete!

============================================================
DISCOVERY COMPLETE
============================================================

Total files found: 45

============================================================
SAVE COMPLETE
============================================================
Successfully saved: 45
Skipped (already exist): 0
Failed: 0
Location: /path/to/downloads
```

## 💡 Real-World Application

This tool demonstrates practical automation thinking and the ability to build reliable, real-world tooling with minimal external dependencies. It's an effective solution for:

- Students who need to collect all practice papers from their university portal
- Educators maintaining archives of practice materials
- Anyone automating repetitive document retrieval tasks

## 🔧 Technical Highlights

- **Smart Duplicate Detection**: Uses file names to detect duplicates without storing everything in memory
- **Configurable Patience Algorithm**: Intelligently stops searching when diminishing returns suggest all files have been found
- **Error Handling**: Gracefully handles network timeouts and file system errors
- **Cross-Platform**: Works on Windows, macOS, and Linux

## ⚠️ Important Notes

- Ensure you have permission to download files from the university portal
- Some university portals may require authentication or have rate-limiting policies
- The script respects a 0.5-second delay between requests to avoid overloading the server
- Files that already exist in the target folder will be skipped to maintain data integrity

## 📝 License

This project is open source and available for personal and educational use.

## 👤 Author

Created as a practical automation solution to streamline the process of managing university study materials.

---

**Built with minimal dependencies, maximum reliability.**
